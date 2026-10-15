"""Shared helpers. Python 3.8+, no third-party dependencies."""
import datetime
import hashlib
import json
import math
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import threading
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
CANCEL = threading.Event()
RESERVED = ("+SOC_RUN_ID", "+SOC_RESULT_FILE", "+SOC_SEED", "+UVM_TESTNAME", "+SOC_PROFILE")


class FlowError(Exception):
    def __init__(self, message, status="CONFIG_ERROR"):
        super().__init__(message)
        self.status = status


def read(path):
    with Path(path).open(encoding="utf-8-sig") as stream:
        return json.load(stream)


def write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(".tmp-" + uuid.uuid4().hex[:16])
    temp.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(str(temp), str(path))


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def unique(parent, prefix):
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S")
    path = Path(parent) / (prefix + "-" + stamp + "-" + uuid.uuid4().hex[:12])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.mkdir(exist_ok=False)
    return path.resolve()


def integer(x, name, low=0, high=None):
    if type(x) is not int or x < low or (high is not None and x > high):
        raise FlowError("Invalid integer " + name)
    return x


def timeout(x):
    if type(x) not in (int, float) or not math.isfinite(x) or x <= 0:
        raise FlowError("timeout must be a positive finite number")
    return float(x)


def profile(name):
    data = read(ROOT / "config" / "profiles.json")
    if data.get("schema_version") != 1 or name not in data.get("profiles", {}):
        raise FlowError("Unknown profile " + name)
    p = data["profiles"][name]
    for field in ("min_checks_count", "min_stimulus_count"):
        integer(p[field], field, 1)
    if type(p.get("software_required")) is not bool:
        raise FlowError("Invalid software_required profile field")
    return p


def ready(p, scheduler="local"):
    if scheduler != "local":
        raise FlowError("LSF is TEMPLATE_ONLY; see lsf_adapter_template.py", "BLOCKED")
    if p["integration_status"] == "BLOCKED":
        raise FlowError(p.get("blocked_reason", "Profile not integrated"), "BLOCKED")


def argv_check(argv):
    if not isinstance(argv, list) or not argv or any(not isinstance(x, str) or not x or "\0" in x for x in argv):
        raise FlowError("Command must be a nonempty argv array")


def adapter(p, simulator, site=None):
    if p["kind"] == "mock":
        return {"kind": "mock"}
    path = Path(site or ROOT / "config" / "site.json")
    if not path.is_file():
        raise FlowError("site.json missing; configure actual wrappers first", "BLOCKED")
    data = read(path)
    a = data.get("adapters", {}).get(simulator, {})
    if data.get("schema_version") != 1 or a.get("enabled") is not True:
        raise FlowError("Simulator adapter disabled", "BLOCKED")
    for field in ("build_argv", "run_argv"):
        argv_check(a.get(field))
    if a.get("elaborate_argv"):
        argv_check(a["elaborate_argv"])
    if any(any(item.startswith(k) for k in RESERVED) for item in a["run_argv"]):
        raise FlowError("Adapter must not override reserved SoC plusargs")
    if not a.get("tool_identity") or not a.get("build_inputs") or not a.get("build_artifacts"):
        raise FlowError("Set tool_identity, build_inputs and build_artifacts")
    if a.get("log_contract_acknowledged") is not True or not a.get("native_error_patterns"):
        raise FlowError("Validate native/late error detection before enabling adapter", "BLOCKED")
    for expression in a["native_error_patterns"]:
        re.compile(expression)
    env = a.get("environment", {})
    if not isinstance(env, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in env.items()):
        raise FlowError("environment must be a string-to-string object")
    return a


def expand(items, values):
    try:
        return [item.format_map(values) for item in items]
    except (KeyError, ValueError) as exc:
        raise FlowError("Unknown/malformed placeholder: " + str(exc))


def values(build_dir="", run_dir="", run_id="", name="", test="", seed=0):
    return dict(project_root=str(ROOT), build_dir=str(build_dir), run_dir=str(run_dir),
                result_file=str(Path(run_dir) / "tb_result.json"), run_id=run_id,
                profile=name, test=test, seed=str(seed), python=sys.executable)


def snapshot(paths, vals):
    found = {}
    for item in paths:
        path = Path(expand([item], vals)[0])
        path = (ROOT / path).resolve() if not path.is_absolute() else path.resolve()
        if not path.is_file():
            raise FlowError("Input is not a file: " + str(path))
        found[str(path)] = sha(path)
    return found


def verify(snapshot_data):
    for path, expected in snapshot_data.items():
        if not Path(path).is_file() or sha(path) != expected:
            raise FlowError("Changed/missing input or artifact: " + path, "BLOCKED")


def stop(proc):
    if os.name == "posix":
        for sig in (signal.SIGTERM, signal.SIGKILL):
            try:
                os.killpg(proc.pid, sig)
            except ProcessLookupError:
                pass
            try:
                proc.wait(timeout=0.5)
            except subprocess.TimeoutExpired:
                pass
    else:
        subprocess.run(["taskkill", "/PID", str(proc.pid), "/T", "/F"], check=False,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                       creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        if proc.poll() is None:
            proc.kill()
    proc.wait()


def execute(argv, cwd, log, seconds, environment=None):
    argv_check(argv)
    seconds = timeout(seconds)
    start = time.monotonic()
    result = dict(argv=argv, cwd=str(cwd), state="STARTING", returncode=None, elapsed_s=0)
    env = dict(os.environ)
    env.update(environment or {})
    flags = (getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0) |
             getattr(subprocess, "CREATE_NO_WINDOW", 0)) if os.name == "nt" else 0
    with Path(log).open("w", encoding="utf-8") as stream:
        try:
            proc = subprocess.Popen(argv, cwd=str(cwd), stdout=stream, stderr=subprocess.STDOUT,
                                    env=env, shell=False, start_new_session=os.name == "posix",
                                    creationflags=flags)
        except OSError as exc:
            result.update(state="INFRA_ERROR", error=str(exc))
            return result
        result.update(state="RUNNING", pid=proc.pid)
        try:
            while proc.poll() is None:
                if CANCEL.is_set() or time.monotonic() - start >= seconds:
                    result["state"] = "CANCELLED" if CANCEL.is_set() else "WALL_TIMEOUT"
                    stop(proc)
                    break
                time.sleep(0.02)
            if result["state"] == "RUNNING":
                result["state"] = "EXITED"
        except KeyboardInterrupt:
            CANCEL.set()
            result["state"] = "CANCELLED"
            stop(proc)
        result["returncode"] = proc.returncode
    result["elapsed_s"] = round(time.monotonic() - start, 6)
    return result


def negative_contract(kind, failures, counts, logs):
    if kind not in ("normal", "negative_selftest"):
        raise FlowError("Unknown suite kind")
    if not isinstance(failures, list) or any(not isinstance(x, str) or not x for x in failures):
        raise FlowError("Expected failures must be an array of IDs")
    if not isinstance(counts, dict) or not isinstance(logs, dict):
        raise FlowError("Expected counts must be objects")
    if kind == "normal":
        if failures or counts or logs:
            raise FlowError("Normal tests cannot allow expected failures")
        return
    if not failures or set(counts) != {"uvm_errors", "uvm_fatals", "assertion_errors"}:
        raise FlowError("Negative suite requires exact IDs and all three expected error counts")
    for value in counts.values():
        integer(value, "expected_counts", 0)
    if counts["uvm_fatals"] != 0:
        raise FlowError("Fatal negative tests are outside this completed-test contract")
    for key, value in logs.items():
        if key not in failures:
            raise FlowError("Expected log ID must be included in expected_failures")
        integer(value, "expected_log_counts", 1)
    if sum(logs.values()) != counts["uvm_errors"]:
        raise FlowError("Expected UVM error log counts must equal expected uvm_errors")
