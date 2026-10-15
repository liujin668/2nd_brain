"""Build and run execution. No automatic cache reuse or opaque shell command strings."""
from pathlib import Path
import re
import sys
import os
from flow_common import (ROOT, RESERVED, FlowError, read, write, unique, integer, timeout,
                         profile, ready, adapter, values, snapshot, verify, sha, expand, execute, negative_contract)
from flow_result import evaluate, log_errors


def build(name, simulator, output, site=None, dry_run=False):
    p = profile(name)
    ready(p)
    a = adapter(p, simulator, site)
    directory = unique(Path(output) / "builds", "build")
    vals = values(build_dir=directory, name=name)
    scripts = [str(x) for x in (ROOT / "script").glob("*.py")]
    sources = scripts + [str(ROOT / "config" / "profiles.json")]
    if p["kind"] != "mock":
        sources += a["build_inputs"]
    data = dict(schema_version=1, profile_name=name, profile=p, adapter=a,
                build_id=directory.name, build_dir=str(directory),
                simulator="mock" if p["kind"] == "mock" else simulator,
                source_snapshot=snapshot(sources, vals), artifacts={}, commands=[],
                cache_reused=False, cache_policy="OFF_NO_DEPENDENCY_CLOSURE",
                status="PLANNED", validation_level=p["validation_level"])
    if p["kind"] != "mock":
        for phase, field in (("compile", "build_argv"), ("elaborate", "elaborate_argv")):
            if a.get(field):
                data["commands"].append(dict(phase=phase, argv=expand(a[field], vals),
                    cwd=expand([a.get("build_cwd", "{project_root}")], vals)[0]))
    write(directory / "build.json", data)
    if dry_run:
        return data
    if p["kind"] == "mock":
        path = directory / "mock_build.json"
        write(path, {"validation_level": "FLOW_MOCK", "not_hdl_simulation": True})
        data["artifacts"][str(path)] = sha(path)
    else:
        for command in data["commands"]:
            process = execute(command["argv"], command["cwd"], directory / (command["phase"] + ".log"),
                              a.get("build_timeout_s", 3600), a.get("environment"))
            command["process"] = process
            if (process["state"] != "EXITED" or process["returncode"] != 0 or
                    log_errors(directory / (command["phase"] + ".log"), a.get("native_error_patterns", []), {})):
                data.update(status="BUILD_ERROR", error=process)
                write(directory / "build.json", data)
                return data
        for item in a["build_artifacts"]:
            path = Path(expand([item], vals)[0])
            path = (directory / path).resolve() if not path.is_absolute() else path.resolve()
            if directory not in path.parents or not path.is_file():
                data.update(status="BUILD_ERROR", error="Missing/nonlocal artifact: " + str(path))
                write(directory / "build.json", data)
                return data
            data["artifacts"][str(path)] = sha(path)
    data["status"] = "READY"
    write(directory / "build.json", data)
    return data


def check_build(data, name):
    if data.get("status") != "READY" or data.get("profile_name") != name:
        raise FlowError("Build is not READY or profile mismatched", "BLOCKED")
    verify(data["source_snapshot"])
    verify(data["artifacts"])
    if data["profile"] != profile(name):
        raise FlowError("Profile changed after build", "BLOCKED")


def worker(manifest_path):
    m = read(manifest_path)
    directory = Path(m["run_dir"])
    # A scheduler worker must also enforce profile readiness.
    p = profile(m["profile_name"])
    ready(p)
    if p != m["profile"]:
        raise FlowError("Profile snapshot changed", "BLOCKED")
    check_build(m["build"], m["profile_name"])
    if directory.resolve() != Path(manifest_path).resolve().parent:
        raise FlowError("Manifest/run directory mismatch")
    with (directory / "worker.claim").open("x", encoding="utf-8") as stream:
        stream.write(str(os.getpid()) + "\n")
    if (directory / "tb_result.json").exists() or (directory / "result.json").exists():
        raise FlowError("Refusing a run with pre-existing results")
    process = execute(m["argv"], m["cwd"], directory / "sim.log", m["timeout_s"],
                      m["adapter"].get("environment"))
    write(directory / "process.json", process)
    result = evaluate(m, process, directory / "tb_result.json", directory / "sim.log")
    write(directory / "result.json", result)
    return result


def run(name, simulator, output, test=None, seed=666, seconds=60, scenario="pass",
        site=None, previous_build=None, dry_run=False, scheduler="local",
        expected=None, suite_kind="normal", case_name=None, parent_run=None, extra=None, on_planned=None,
        expected_counts=None, expected_log_counts=None):
    integer(seed, "seed", 1, 2147483647)
    timeout(seconds)
    p = profile(name)
    ready(p, scheduler)
    expected, extra = expected or [], extra or []
    counts, logs = expected_counts or {}, expected_log_counts or {}
    negative_contract(suite_kind, expected, counts, logs)
    if expected and suite_kind != "negative_selftest":
        raise FlowError("Expected failures only allowed in negative_selftest suite")
    if any(not isinstance(x, str) or not x for x in expected):
        raise FlowError("Invalid expected error ID")
    if any(not isinstance(x, str) or any(x.startswith(k) for k in RESERVED) for x in extra):
        raise FlowError("Invalid/reserved extra argument")
    b = previous_build or build(name, simulator, output, site, dry_run)
    if not dry_run:
        check_build(b, name)
    if p["kind"] != "mock" and b["simulator"] != simulator:
        raise FlowError("Requested simulator differs from build backend", "BLOCKED")
    if b["profile"] != p:
        raise FlowError("Profile/build snapshot mismatch", "BLOCKED")
    test = test or p["default_test"]
    if not isinstance(test, str) or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_$:]*", test):
        raise FlowError("Invalid test class name")
    directory = unique(Path(output) / "runs", "run")
    vals = values(b["build_dir"], directory, directory.name, name, test, seed)
    if p["kind"] == "mock":
        argv = [sys.executable, str(ROOT / "script" / "mock_sim.py"),
                "--scenario", scenario, "--run-id", directory.name,
                "--result-file", vals["result_file"], "--profile", name,
                "--test", test, "--seed", str(seed)]
        cwd = str(directory)
    else:
        argv = expand(b["adapter"]["run_argv"], vals) + [
            "+SOC_RUN_ID=" + directory.name, "+SOC_RESULT_FILE=" + vals["result_file"],
            "+SOC_SEED=" + str(seed), "+UVM_TESTNAME=" + test, "+SOC_PROFILE=" + name] + extra
        cwd = expand([b["adapter"].get("run_cwd", "{run_dir}")], vals)[0]
    m = dict(schema_version=1, run_id=directory.name, run_dir=str(directory),
             profile_name=name, profile=p, adapter=b["adapter"], build=b, test=test,
             seed=seed, timeout_s=float(seconds), argv=argv, cwd=cwd, scheduler=scheduler,
             simulator=b["simulator"], source_root=str(ROOT), scenario=scenario,
             suite_kind=suite_kind, expected_failures=expected, expected_counts=counts,
             expected_log_counts=logs, extra_args=extra,
             case_name=case_name or test, parent_run=parent_run)
    write(directory / "manifest.json", m)
    write(directory / "command.json", dict(argv=argv, cwd=cwd, shell=False))
    if on_planned is not None:
        on_planned(directory)
    if dry_run:
        result = dict(schema_version=1, run_id=directory.name, run_dir=str(directory),
                      profile=name, test=test, seed=seed, validation_level=p["validation_level"],
                      status="PLANNED", acceptance="PLANNED", reasons=[],
                      process={"state": "NOT_STARTED", "elapsed_s": 0})
        write(directory / "result.json", result)
        return result
    return worker(directory / "manifest.json")


def reproduce(directory, output, dry_run=False):
    m = read(Path(directory) / "manifest.json")
    if Path(m["source_root"]) != ROOT:
        raise FlowError("Source tree moved; rebase site paths explicitly and rebuild", "BLOCKED")
    check_build(m["build"], m["profile_name"])
    return run(m["profile_name"], m["simulator"], output, m["test"], m["seed"],
               m["timeout_s"], m["scenario"], previous_build=m["build"], dry_run=dry_run,
               expected=m.get("expected_failures"), suite_kind=m.get("suite_kind", "normal"),
               parent_run=m["run_id"], extra=m.get("extra_args"),
               expected_counts=m.get("expected_counts"), expected_log_counts=m.get("expected_log_counts"))
