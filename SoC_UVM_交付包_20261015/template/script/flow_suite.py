"""Frozen regression plans, bounded local concurrency and reports."""
import concurrent.futures
from pathlib import Path
import threading
from flow_common import CANCEL, FlowError, read, write, unique, integer, timeout, profile, ready, negative_contract
from flow_engine import build, run
from flow_result import report


def validate(spec):
    if spec.get("schema_version") != 1 or spec.get("kind") not in ("normal", "negative_selftest"):
        raise FlowError("Unsupported suite schema or kind")
    if not isinstance(spec.get("profile"), str) or not isinstance(spec.get("cases"), list) or not spec["cases"]:
        raise FlowError("Suite needs a profile and nonempty cases")
    expanded, names = [], set()
    for case in spec["cases"]:
        name = case.get("name")
        if not isinstance(name, str) or not name or name in names:
            raise FlowError("Case names must be nonempty and unique")
        names.add(name)
        seeds = case.get("seeds", [666])
        if not isinstance(seeds, list) or not seeds:
            raise FlowError("seeds must be a nonempty array")
        for seed in seeds:
            integer(seed, "seed", 1, 2147483647)
        if len(seeds) != len(set(seeds)):
            raise FlowError("Duplicate seed within a case")
        expected = case.get("expected_failures", [])
        if not isinstance(expected, list) or any(not isinstance(x, str) or not x for x in expected):
            raise FlowError("expected_failures must be an array of IDs")
        if spec["kind"] == "normal" and expected:
            raise FlowError("Business test failure cannot be converted to PASS")
        if spec["kind"] == "negative_selftest" and not expected:
            raise FlowError("Negative selftests require exact expected IDs")
        negative_contract(spec["kind"], expected, case.get("expected_counts", {}),
                          case.get("expected_log_counts", {}))
        timeout(case.get("timeout_s", 60))
        for seed in seeds:
            item = dict(case, seed=seed)
            item.pop("seeds", None)
            expanded.append(item)
    return expanded


def regress(suite_path, simulator, output, jobs=1, site=None, dry_run=False, scheduler="local"):
    integer(jobs, "jobs", 1)
    spec = read(suite_path)
    cases = validate(spec)
    ready(profile(spec["profile"]), scheduler)
    directory = unique(Path(output) / "regressions", "reg")
    plan = dict(schema_version=1, suite=spec, cases=cases, run_dirs=[], controller_errors=[])
    write(directory / "plan.json", plan)
    b = build(spec["profile"], simulator, output, site, dry_run)
    plan["build"] = b
    write(directory / "plan.json", plan)
    if b["status"] not in ("READY", "PLANNED"):
        return report(directory)
    lock = threading.Lock()
    def register(run_dir):
        with lock:
            plan["run_dirs"].append(str(run_dir))
            write(directory / "plan.json", plan)
    def one(case):
        return run(spec["profile"], simulator, directory, test=case.get("test"),
                   seed=case["seed"], seconds=case.get("timeout_s", 60),
                   scenario=case.get("scenario", "pass"), previous_build=b, dry_run=dry_run,
                   scheduler=scheduler, expected=case.get("expected_failures"),
                   suite_kind=spec["kind"], case_name=case["name"],
                   extra=case.get("extra_args"), on_planned=register,
                   expected_counts=case.get("expected_counts"),
                   expected_log_counts=case.get("expected_log_counts"))
    with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as pool:
        futures = [pool.submit(one, case) for case in cases]
        try:
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as exc:
                    with lock:
                        plan["controller_errors"].append(str(exc))
                        write(directory / "plan.json", plan)
        except KeyboardInterrupt:
            CANCEL.set()
            for future in futures:
                try:
                    future.result()
                except Exception as exc:
                    plan["controller_errors"].append(str(exc))
            write(directory / "plan.json", plan)
    return report(directory)
