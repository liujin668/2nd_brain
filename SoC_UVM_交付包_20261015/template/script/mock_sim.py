#!/usr/bin/env python3
"""Flow-only fixture: never a substitute for SV, VIP or DUT simulation."""
import argparse
import json
import sys
import time
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", default="pass")
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--result-file", required=True)
    parser.add_argument("--profile", default="mock")
    parser.add_argument("--test", default="soc_mock_test")
    parser.add_argument("--seed", type=int, required=True)
    args = parser.parse_args()
    result = dict(schema_version=1, run_id=args.run_id, profile=args.profile,
                  test=args.test, seed=args.seed, status="PASS", completed=True,
                  stimulus_count=4, checks_count=4, pending_count=0, uvm_errors=0,
                  uvm_fatals=0, assertion_errors=0, software_required=False,
                  software_status="NOT_REQUIRED", failures=[])
    scenario = args.scenario
    if scenario == "timeout":
        time.sleep(60)
    if scenario == "missing_result":
        return 0
    if scenario == "truncated_result":
        Path(args.result_file).write_text('{"status":', encoding="utf-8")
        return 0
    if scenario == "fail":
        result.update(status="FAIL", uvm_errors=1, failures=["MOCK_MISMATCH"])
        print("UVM_ERROR @ 10: mock [MOCK_MISMATCH] injected mismatch", flush=True)
    elif scenario == "no_completion":
        result["completed"] = False
    elif scenario == "wrong_run_id":
        result["run_id"] = "stale-run"
    elif scenario == "empty_checks":
        result["checks_count"] = 0
    elif scenario == "empty_stimulus":
        result["stimulus_count"] = 0
    elif scenario == "pending":
        result["pending_count"] = 1
    elif scenario == "software_fail":
        result.update(software_required=True, software_status="FAIL")
    elif scenario not in ("pass", "crash", "late_error", "timeout"):
        print("SOC_FLOW_ERROR [UNKNOWN_SCENARIO] " + scenario)
        return 2
    Path(args.result_file).write_text(json.dumps(result), encoding="utf-8")
    print("FLOW_MOCK fixture wrote result; this is not HDL simulation.", flush=True)
    if scenario == "late_error":
        print("SOC_FLOW_ERROR [MOCK_LATE_ERROR] after result was written", flush=True)
    if scenario == "crash":
        return 7
    return 0


if __name__ == "__main__":
    sys.exit(main())
