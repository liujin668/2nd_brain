#!/usr/bin/env python3
"""Run local, license-free delivery checks. Does not compile SystemVerilog."""
import datetime
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "template"
EVIDENCE = ROOT / "validation" / "evidence"


def main():
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    (EVIDENCE / "validation_summary.json").write_text(json.dumps({"status": "RUNNING"}), encoding="utf-8")
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    records = []
    with tempfile.TemporaryDirectory(prefix="soc_verify_") as scratch:
        checks = [
            ("image_unittest", ["-m", "unittest", "discover", "-s", "native/sw_lib", "-p", "test_*.py", "-v"]),
            ("flow_unittest", ["-m", "unittest", "discover", "-s", "tests_flow", "-v"]),
            ("mock_smoke_cli", ["script/socflow.py", "regress", "--suite", "regress/mock_smoke.json", "--jobs", "2", "--out", str(Path(scratch) / "smoke")]),
            ("mock_negative_cli", ["script/socflow.py", "regress", "--suite", "regress/mock_negative.json", "--out", str(Path(scratch) / "negative")]),
            ("bundle_integrity", [str(ROOT / "validation" / "check_bundle.py")]),
        ]
        for name, arguments in checks:
            start = time.monotonic()
            process = subprocess.run([sys.executable] + arguments, cwd=str(TEMPLATE),
                                     env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     encoding="utf-8", errors="replace", timeout=180)
            record = dict(name=name, argv=["python3"] + arguments, exit_code=process.returncode,
                          elapsed_s=round(time.monotonic() - start, 3),
                          status="PASS" if process.returncode == 0 else "FAIL")
            (EVIDENCE / (name + ".log")).write_text(
                "STDOUT\n" + process.stdout + "\nSTDERR\n" + process.stderr, encoding="utf-8")
            if name.endswith("_cli"):
                try:
                    summary = json.loads(process.stdout)
                    (EVIDENCE / (name + ".json")).write_text(
                        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                except ValueError:
                    record["status"] = "FAIL"
                    record["reason"] = "CLI did not return a JSON report"
            records.append(record)
            print(json.dumps(record, ensure_ascii=True), flush=True)
    result = dict(
        timestamp_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        host_platform=platform.platform(), python=sys.version,
        status="PASS" if all(r["status"] == "PASS" for r in records) else "FAIL",
        scope="Python unit tests, mock runner CLI, static bundle integrity",
        tools_on_path={name: bool(shutil.which(name)) for name in ("vcs", "xrun", "bsub", "csh", "gcc")},
        checks=records,
        limitations=["No SystemVerilog compilation or simulation was performed",
                     "No real N2, CMN, commercial VIP, LSF or coverage merge was exercised",
                     "Mock run directories are temporary; retained reports are validation evidence only",
                     "Python 3.8 compatibility is a source target, not a tested runtime version"])
    (EVIDENCE / "validation_summary.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
