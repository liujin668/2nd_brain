"""Strict verdicts and reporting. A successful process is not a successful test."""
import csv
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from flow_common import FlowError, read, write, negative_contract

FIELDS = {"schema_version", "run_id", "profile", "test", "seed", "status", "completed",
          "stimulus_count", "checks_count", "pending_count", "uvm_errors", "uvm_fatals",
          "assertion_errors", "software_required", "software_status", "failures"}
PATTERNS = [r"^\s*UVM_(?:ERROR|FATAL)\b(?!\s*:\s*\d+\s*$)",
            r"^\s*SOC_(?:FLOW|ASSERT(?:ION)?)_ERROR\b"]


def log_errors(path, extra, expected):
    patterns = [re.compile(x) for x in PATTERNS + extra]
    hits, seen = [], {}
    with Path(path).open(encoding="utf-8", errors="replace") as stream:
        for line in stream:
            if any(x.search(line) for x in patterns):
                match = re.search(r"\[([A-Za-z0-9_.:-]+)\]", line)
                allowed = line.lstrip().startswith("UVM_ERROR") and match and match.group(1) in expected
                if allowed:
                    key = match.group(1)
                    seen[key] = seen.get(key, 0) + 1
                    allowed = seen[key] <= expected[key]
                if not allowed and len(hits) < 100:
                    hits.append(line.rstrip()[:2000])
    for key, count in expected.items():
        if seen.get(key, 0) != count:
            hits.append("EXPECTED_LOG_COUNT_MISMATCH:" + key)
    return hits


def evaluate(manifest, process, tb_path, log_path):
    invalid, functional = [], []
    if process.get("state") != "EXITED":
        invalid.append(process.get("state", "INCOMPLETE"))
    elif process.get("returncode") != 0:
        invalid.append("PROCESS_EXIT_NONZERO")
    try:
        tb = read(tb_path)
    except (OSError, ValueError):
        tb = {}
        invalid.append("RESULT_MISSING_OR_INVALID")
    if not isinstance(tb, dict):
        tb = {}
        invalid.append("RESULT_NOT_OBJECT")
    missing = FIELDS - set(tb)
    if missing:
        invalid.append("MISSING_FIELDS:" + ",".join(sorted(missing)))
    else:
        p = manifest["profile"]
        for field in ("schema_version", "seed", "stimulus_count", "checks_count", "pending_count",
                      "uvm_errors", "uvm_fatals", "assertion_errors"):
            if type(tb[field]) is not int or tb[field] < 0:
                invalid.append("INVALID_TYPE:" + field)
        for field in ("completed", "software_required"):
            if type(tb[field]) is not bool:
                invalid.append("INVALID_TYPE:" + field)
        if tb["schema_version"] != 1:
            invalid.append("SCHEMA_MISMATCH")
        for field in ("run_id", "test", "seed", "profile"):
            wanted = manifest["profile_name"] if field == "profile" else manifest[field]
            if tb[field] != wanted:
                invalid.append("IDENTITY_MISMATCH:" + field)
        if tb["status"] not in ("PASS", "FAIL"):
            invalid.append("INVALID_STATUS")
        if tb["completed"] is not True:
            invalid.append("NOT_COMPLETED")
        if not isinstance(tb["failures"], list) or any(not isinstance(x, str) or not x for x in tb["failures"]):
            invalid.append("INVALID_FAILURE_IDS")
        for field, minimum in (("stimulus_count", p["min_stimulus_count"]),
                               ("checks_count", p["min_checks_count"])):
            if type(tb[field]) is int and tb[field] < minimum:
                invalid.append("INSUFFICIENT_" + field.upper())
        if tb["pending_count"] != 0:
            invalid.append("PENDING_TRANSACTIONS")
        if tb["uvm_fatals"] != 0:
            invalid.append("UVM_FATAL")
        if tb["software_required"] != p["software_required"]:
            invalid.append("SOFTWARE_REQUIREMENT_MISMATCH")
        wanted = "PASS" if p["software_required"] else "NOT_REQUIRED"
        if tb["software_status"] != wanted:
            invalid.append("SOFTWARE_NOT_SUCCESSFUL")
        for condition, reason in ((tb["status"] != "PASS", "TB_FAIL"),
                                  (tb["uvm_errors"] != 0, "UVM_ERRORS"),
                                  (tb["assertion_errors"] != 0, "ASSERTION_ERRORS"),
                                  (bool(tb["failures"]), "FAILURE_IDS")):
            if condition:
                functional.append(reason)
        if tb["status"] == "PASS" and functional:
            invalid.append("INCONSISTENT_PASS_RESULT")
    expected = manifest.get("expected_failures", [])
    try:
        negative_contract(manifest.get("suite_kind", "normal"), expected,
                          manifest.get("expected_counts", {}), manifest.get("expected_log_counts", {}))
    except FlowError as exc:
        invalid.append("INVALID_EXPECTATION_CONTRACT:" + str(exc))
    if manifest.get("suite_kind") == "negative_selftest":
        for field, value in manifest.get("expected_counts", {}).items():
            if tb.get(field) != value:
                invalid.append("EXPECTED_COUNT_MISMATCH:" + field)
    try:
        hits = log_errors(log_path, manifest["adapter"].get("native_error_patterns", []), manifest.get("expected_log_counts", {}))
    except OSError:
        hits = ["LOG_MISSING"]
    if hits:
        invalid.append("LOG_ERROR")
    status = "PASS" if not invalid and not functional else "FAIL"
    if process.get("state") in ("WALL_TIMEOUT", "CANCELLED", "INFRA_ERROR"):
        status = process["state"]
    match = (manifest.get("suite_kind") == "negative_selftest" and bool(expected)
             and not invalid and tb.get("status") == "FAIL"
             and sorted(tb.get("failures", [])) == sorted(expected) and bool(functional))
    acceptance = "EXPECTED_FAILURE" if match else ("PASS" if status == "PASS" and not expected else "FAIL")
    if expected and not match:
        invalid.append("EXPECTED_FAILURE_CONTRACT_NOT_MET")
    return dict(schema_version=1, run_id=manifest["run_id"], run_dir=manifest["run_dir"],
                test=manifest["test"], seed=manifest["seed"], profile=manifest["profile_name"],
                validation_level=manifest["profile"]["validation_level"], status=status,
                acceptance=acceptance, reasons=invalid + functional, process=process,
                tb_result=tb, log_errors=hits)


def report(directory):
    directory = Path(directory)
    if (directory / "plan.json").is_file():
        plan = read(directory / "plan.json")
        runs, total = plan.get("run_dirs", []), len(plan["cases"])
    elif (directory / "manifest.json").is_file():
        runs, total = [str(directory)], 1
    else:
        raise FlowError("Report requires a run or regression directory")
    rows = []
    for run in runs:
        path = Path(run) / "result.json"
        try:
            rows.append(read(path))
        except (OSError, ValueError):
            rows.append(dict(status="INCOMPLETE", acceptance="FAIL", run_dir=run, reasons=["RESULT_MISSING"]))
    while len(rows) < total:
        rows.append(dict(status="INCOMPLETE", acceptance="FAIL", reasons=["PLANNED_CASE_NOT_STARTED"]))
    accepted = sum(row.get("acceptance") in ("PASS", "EXPECTED_FAILURE") for row in rows)
    status = "PASS" if rows and accepted == total == len(rows) else "FAIL"
    if rows and len(rows) == total and all(row["status"] == "PLANNED" for row in rows):
        status = "PLANNED"
    result = dict(schema_version=1, status=status, planned_count=total, result_count=len(rows),
                  accepted_count=accepted, validation_levels=sorted({
                      row.get("validation_level", "UNKNOWN") for row in rows}), runs=rows,
                  report_dir=str(directory))
    write(directory / "summary.json", result)
    fields = ["run_id", "profile", "test", "seed", "validation_level", "status", "acceptance", "run_dir"]
    with (directory / "summary.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    suite = ET.Element("testsuite", name=directory.name, tests=str(len(rows)))
    counts = dict(failures=0, errors=0, skipped=0)
    for row in rows:
        case = ET.SubElement(suite, "testcase", name=str(row.get("test", "incomplete")) +
                             "[seed=" + str(row.get("seed", "?")) + "]",
                             classname=str(row.get("profile", "unknown")),
                             time=str(row.get("process", {}).get("elapsed_s", 0)))
        props = ET.SubElement(case, "properties")
        for key in ("validation_level", "status", "acceptance", "run_id", "run_dir"):
            ET.SubElement(props, "property", name=key, value=str(row.get(key, "")))
        if row.get("acceptance") == "EXPECTED_FAILURE":
            ET.SubElement(case, "system-out").text = "Expected negative selftest; raw test verdict remains FAIL."
        elif row.get("status") == "PLANNED":
            counts["skipped"] += 1
            ET.SubElement(case, "skipped", message="Dry run, not executed")
        elif row.get("acceptance") != "PASS":
            infra = row.get("status") not in ("FAIL", "PASS")
            counts["errors" if infra else "failures"] += 1
            ET.SubElement(case, "error" if infra else "failure",
                          message=row.get("status", "UNKNOWN")).text = str(row.get("reasons", []))
    for key, count in counts.items():
        suite.set(key, str(count))
    ET.ElementTree(suite).write(str(directory / "junit.xml"), encoding="utf-8", xml_declaration=True)
    return result
