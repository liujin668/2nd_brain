#!/usr/bin/env python3
"""Independent SoC runner: mock validates flow only; real tools require site adapters."""
import argparse
import json
from pathlib import Path
import re
import sys
from flow_common import ROOT, RESERVED, FlowError, profile, ready, adapter, read
from flow_engine import build, run, reproduce
from flow_result import FIELDS, report
from flow_suite import validate, regress
from flow_config import generate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="command", required=True)
    for name in ("doctor", "build", "run", "regress", "validate"):
        p = subs.add_parser(name)
        p.add_argument("--profile", default="mock")
        p.add_argument("--simulator", choices=("vcs", "xcelium"), default="vcs")
        p.add_argument("--site")
        p.add_argument("--out", default=str(ROOT / "regress" / "out"))
        p.add_argument("--dry-run", action="store_true")
        p.add_argument("--scheduler", choices=("local", "lsf"), default="local")
        if name in ("regress", "validate"):
            p.add_argument("--suite", default=str(ROOT / "regress" / "mock_smoke.json"))
        if name == "regress":
            p.add_argument("--jobs", type=int, default=1)
        if name == "run":
            p.add_argument("--test")
            p.add_argument("--seed", type=int, default=666)
            p.add_argument("--timeout", type=float, default=60)
            p.add_argument("--scenario", default="pass")
            p.add_argument("--build")
            p.add_argument("--extra-arg", action="append", default=[])
    p = subs.add_parser("report")
    p.add_argument("path")
    p = subs.add_parser("repro")
    p.add_argument("run_dir")
    p.add_argument("--out", default=str(ROOT / "regress" / "out"))
    p.add_argument("--dry-run", action="store_true")
    p = subs.add_parser("config")
    p.add_argument("--design", required=True)
    p.add_argument("--out", required=True)
    subs.add_parser("contracts")
    subs.add_parser("coverage")
    a = parser.parse_args()
    try:
        if a.command == "contracts":
            result = dict(schema_version=1, tb_result_required_fields=sorted(FIELDS),
                          reserved_plusargs=list(RESERVED), supported_schedulers=["local"],
                          lsf="TEMPLATE_ONLY_BLOCKED", coverage_merge="SITE_REQUIRED_BLOCKED",
                          cache="OFF", shell=False,
                          placeholders=["project_root", "build_dir", "run_dir", "result_file",
                                        "profile", "test", "seed", "run_id", "python"])
        elif a.command == "coverage":
            raise FlowError("Coverage merge not integrated; see docs_flow.md compatibility contract", "BLOCKED")
        elif a.command == "config":
            result = generate(a.design, a.out)
        elif a.command == "report":
            result = report(a.path)
        elif a.command == "repro":
            result = reproduce(a.run_dir, a.out, a.dry_run)
        elif a.command == "validate":
            spec = read(a.suite)
            cases = validate(spec)
            result = dict(status="VALID", cases=len(cases), profile=spec["profile"],
                          integration_status=profile(spec["profile"])["integration_status"])
        elif a.command == "doctor":
            p = profile(a.profile)
            ready(p, a.scheduler)
            adapter(p, a.simulator, a.site)
            result = dict(status="READY_FOR_MOCK" if p["kind"] == "mock" else "CONFIGURED_NOT_RUN",
                          python=sys.version, profile=a.profile, validation_level=p["validation_level"])
        elif a.command == "build":
            ready(profile(a.profile), a.scheduler)
            result = build(a.profile, a.simulator, a.out, a.site, a.dry_run)
        elif a.command == "run":
            b = read(Path(a.build) / "build.json") if a.build else None
            result = run(a.profile, a.simulator, a.out, a.test, a.seed, a.timeout, a.scenario,
                         a.site, b, a.dry_run, a.scheduler, extra=a.extra_arg)
            report(result["run_dir"])
        else:
            result = regress(a.suite, a.simulator, a.out, a.jobs, a.site, a.dry_run, a.scheduler)
        print(json.dumps(result, indent=2, ensure_ascii=True))
        return 1 if result.get("status") in (
            "FAIL", "BUILD_ERROR", "WALL_TIMEOUT", "CANCELLED", "INFRA_ERROR", "INCOMPLETE") else 0
    except (FlowError, OSError, ValueError, KeyError, TypeError, re.error) as exc:
        status = getattr(exc, "status", "CONFIG_ERROR")
        print(json.dumps(dict(status=status, error=str(exc)), ensure_ascii=True), file=sys.stderr)
        return 2 if status == "BLOCKED" else 1


if __name__ == "__main__":
    sys.exit(main())
