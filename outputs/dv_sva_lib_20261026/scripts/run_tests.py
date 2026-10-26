#!/usr/bin/env python3
"""Run real SVA simulations; a negative case must fire its expected assertion ID.

Python 3 standard library only. No Python emulation of assertion semantics is used.
Simulator binaries must be installed, licensed, and on PATH (or under --tool-dir).
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
FAILURE_RE = re.compile(r"DV_SVA_FAIL\s+([A-Za-z_][A-Za-z_0-9$]*)\b")
HARD_ERROR_RE = re.compile(
    r"(?:\*\*\s*Fatal:|UVM_FATAL|segmentation fault|internal (?:error|fatal)|"
    r"license (?:checkout|check.?out).*fail|no valid license|Self-test timeout|Unknown CASE:)",
    re.IGNORECASE,
)


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sim", choices=("questa", "vcs", "xrun"))
    parser.add_argument("--case", action="append", default=[], help="Repeat to select cases; default: all")
    parser.add_argument("--list", action="store_true", help="List manifest cases without invoking a simulator")
    parser.add_argument("--dry-run", action="store_true", help="Print commands; do not claim tests were run")
    parser.add_argument("--tool-dir", type=Path, help="Optional directory containing simulator executables")
    parser.add_argument("--build-dir", type=Path, help="Default: build/<sim> under the library root")
    parser.add_argument("--timeout", type=int, default=120, help="Timeout in seconds per compile/run command")
    return parser.parse_args()


def load_manifest() -> tuple[str, list[dict]]:
    data = json.loads((ROOT / "tests" / "cases.json").read_text(encoding="utf-8"))
    cases = data["cases"]
    names = [case["name"] for case in cases]
    if len(names) != len(set(names)):
        raise ValueError("Duplicate case name in manifest")
    for case in cases:
        if case["expect"] not in ("pass", "fail"):
            raise ValueError("Invalid expectation for " + case["name"])
        if (case["expect"] == "fail") != bool(case["expected_ids"]):
            raise ValueError("Negative cases must declare expected assertion IDs")
    return data["top"], cases


def run_command(command: list[str], work: Path, log: Path, timeout: int) -> tuple[int, str]:
    try:
        process = subprocess.run(
            command, cwd=work, text=True, encoding="utf-8", errors="replace",
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout, check=False,
        )
        text = process.stdout
        status = process.returncode
    except subprocess.TimeoutExpired as error:
        captured = error.stdout or b""
        text = captured.decode("utf-8", errors="replace") if isinstance(captured, bytes) else captured
        text += "\nRUNNER_TIMEOUT\n"
        status = 124
    except OSError as error:
        text = "RUNNER_TOOL_ERROR: " + str(error) + "\n"
        status = 127
    log.write_text(text, encoding="utf-8")
    return status, text


def simulator_commands(sim: str, top: str, build: Path, tool_dir: Path | None) -> tuple[list[list[str]], list[str]]:
    def tool(name: str) -> str:
        if tool_dir:
            candidate = tool_dir / (name + (".exe" if os.name == "nt" else ""))
            if candidate.is_file():
                return str(candidate.resolve())
            candidate = tool_dir / name
            if candidate.is_file():
                return str(candidate.resolve())
        return shutil.which(name) or name

    include = str(ROOT / "include")
    sources = [str(ROOT / "checkers" / name) for name in (
        "dv_sva_ready_valid.sv", "dv_sva_response_window.sv", "dv_sva_fifo.sv",
    )] + [str(ROOT / "tests" / "dv_sva_tb.sv")]
    if sim == "questa":
        compile_commands = []
        if not (build / "work").is_dir():
            compile_commands.append([tool("vlib"), "work"])
        compile_commands.append([tool("vlog"), "-sv", "-work", "work", "+incdir+" + include] + sources)
        run = [tool("vsim"), "-c", "-assertdebug", "-onfinish", "stop", "work." + top]
        run += ["-do", "set BreakOnAssertion 4; run -all; quit -code 0"]
        return compile_commands, run
    if sim == "vcs":
        executable = build / ("simv.exe" if os.name == "nt" else "simv")
        compile_commands = [[tool("vcs"), "-full64", "-sverilog", "+incdir+" + include,
                             "-top", top, "-o", str(executable)] + sources]
        return compile_commands, [str(executable)]
    compile_commands = [[tool("xrun"), "-64bit", "-sv", "-elaborate", "-top", top,
                         "-xmlibdirname", str(build / "xcelium.d"), "-incdir", include] + sources]
    return compile_commands, [tool("xrun"), "-64bit", "-R", "-xmlibdirname", str(build / "xcelium.d")]


def evaluate(case: dict, status: int, text: str) -> dict:
    seen = sorted(set(FAILURE_RE.findall(text)))
    expected = sorted(case["expected_ids"])
    completed = ("DV_SVA_CASE_DONE: " + case["name"]) in text
    reasons = []
    if not completed:
        reasons.append("missing completion marker (early stop/crash is not a successful negative test)")
    if HARD_ERROR_RE.search(text) or status in (124, 127) or status < 0 or status > 1:
        reasons.append("simulator/tool failure")
    if seen != expected:
        reasons.append("assertion IDs differ: expected " + repr(expected) + ", saw " + repr(seen))
    if case["expect"] == "pass" and status != 0:
        reasons.append("positive case returned a nonzero exit status")
    # Simulators may return 1 for intentional $error. An exit code alone never proves success.
    return {"case": case["name"], "passed": not reasons, "expected": case["expect"],
            "expected_ids": expected, "seen_ids": seen, "returncode": status,
            "completed": completed, "reasons": reasons}


def main() -> int:
    args = arguments()
    try:
        top, all_cases = load_manifest()
    except (OSError, ValueError, KeyError) as error:
        print("Manifest error:", error, file=sys.stderr)
        return 2
    if args.list:
        for case in all_cases:
            requirements = ",".join(case.get("requires", [])) or "standard SVA"
            print(f"{case['name']:<28} expect={case['expect']:<4} IDs={','.join(case['expected_ids']) or '-'} [{requirements}]")
        return 0
    if not args.sim:
        print("Choose --sim questa|vcs|xrun, or use --list.", file=sys.stderr)
        return 2
    selected = set(args.case)
    unknown = selected - {case["name"] for case in all_cases}
    if unknown:
        print("Unknown cases:", ", ".join(sorted(unknown)), file=sys.stderr)
        return 2
    cases = [case for case in all_cases if not selected or case["name"] in selected]
    build = (args.build_dir or ROOT / "build" / args.sim).resolve()
    compile_commands, base_run = simulator_commands(args.sim, top, build, args.tool_dir)
    if args.dry_run:
        print("DRY RUN: no simulator was invoked; this is not a test result.")
        print("Working directory:", build)
        for command in compile_commands:
            print("COMPILE:", subprocess.list2cmdline(command))
        for case in cases:
            print("RUN:", subprocess.list2cmdline(base_run + ["+CASE=" + case["name"]]))
        return 0
    build.mkdir(parents=True, exist_ok=True)
    for index, command in enumerate(compile_commands):
        log = build / f"compile_{index}.log"
        status, text = run_command(command, build, log, args.timeout)
        if status != 0:
            print(f"Compile/tool setup failed ({status}); no negative tests are credited. Log: {log}", file=sys.stderr)
            print(text[-4000:], file=sys.stderr)
            return 2
    results = []
    for case in cases:
        log = build / (case["name"] + ".log")
        status, text = run_command(base_run + ["+CASE=" + case["name"]], build, log, args.timeout)
        result = evaluate(case, status, text)
        result["log"] = str(log)
        results.append(result)
        print(("PASS " if result["passed"] else "FAIL ") + case["name"])
        for reason in result["reasons"]:
            print("  " + reason)
    summary = {"simulator": args.sim, "actual_simulations": True, "results": results,
               "passed": sum(result["passed"] for result in results), "total": len(results)}
    (build / "results.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{summary['passed']}/{summary['total']} cases matched expectations. Results: {build / 'results.json'}")
    return 0 if summary["passed"] == summary["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
