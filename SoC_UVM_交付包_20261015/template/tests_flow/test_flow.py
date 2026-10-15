"""End-to-end flow checks using explicit mock processes; no HDL simulator needed."""
import copy
import json
import os
import subprocess
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "script"))
from flow_common import CANCEL, FlowError, read, write
from flow_engine import build, run, reproduce, worker, check_build
from flow_result import evaluate, report
from flow_suite import validate, regress
from flow_config import generate


class FlowTests(unittest.TestCase):
    def setUp(self):
        CANCEL.clear()
        self.base = ROOT / "tests_flow" / ".tmp"
        self.base.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=str(self.base), prefix="test-")
        self.out = Path(self.temp.name)
        self.b = build("mock", "vcs", self.out)

    def tearDown(self):
        CANCEL.clear()
        self.temp.cleanup()

    def launch(self, scenario="pass", **kwargs):
        if kwargs.get("suite_kind") == "negative_selftest":
            kwargs.setdefault("expected_counts", dict(uvm_errors=1, uvm_fatals=0, assertion_errors=0))
            ids = kwargs.get("expected", [])
            kwargs.setdefault("expected_log_counts", {ids[0]: 1} if ids else {})
        return run("mock", "vcs", self.out, scenario=scenario, previous_build=self.b, **kwargs)

    def test_pass_and_reports(self):
        r = self.launch(seed=123)
        self.assertEqual(r["status"], "PASS")
        self.assertEqual(r["validation_level"], "FLOW_MOCK")
        summary = report(r["run_dir"])
        self.assertEqual(summary["status"], "PASS")
        for name in ("manifest.json", "command.json", "process.json", "tb_result.json",
                     "result.json", "summary.json", "summary.csv", "junit.xml"):
            self.assertTrue((Path(r["run_dir"]) / name).is_file(), name)

    def test_fail_closed_cases(self):
        cases = {"fail": "FAIL", "no_completion": "FAIL", "crash": "FAIL",
                 "late_error": "FAIL", "wrong_run_id": "FAIL", "empty_checks": "FAIL",
                 "empty_stimulus": "FAIL", "pending": "FAIL", "software_fail": "FAIL",
                 "missing_result": "FAIL", "truncated_result": "FAIL"}
        for scenario, expected in cases.items():
            with self.subTest(scenario=scenario):
                r = self.launch(scenario)
                self.assertEqual(r["status"], expected)
                self.assertEqual(r["acceptance"], "FAIL")

    def test_timeout(self):
        r = self.launch("timeout", seconds=0.2)
        self.assertEqual(r["status"], "WALL_TIMEOUT")
        self.assertIsNotNone(r["process"]["returncode"])

    def test_exact_negative_contract(self):
        r = self.launch("fail", suite_kind="negative_selftest", expected=["MOCK_MISMATCH"])
        self.assertEqual(r["status"], "FAIL")
        self.assertEqual(r["acceptance"], "EXPECTED_FAILURE")
        wrong = self.launch("fail", suite_kind="negative_selftest", expected=["OTHER_ID"])
        self.assertEqual(wrong["acceptance"], "FAIL")
        no_failure = self.launch("pass", suite_kind="negative_selftest", expected=["MOCK_MISMATCH"])
        self.assertEqual(no_failure["acceptance"], "FAIL")
        with self.assertRaises(FlowError):
            self.launch("fail", expected=["MOCK_MISMATCH"])

    def test_negative_rejects_extra_same_id_and_late_duplicate(self):
        r = self.launch("fail", suite_kind="negative_selftest", expected=["MOCK_MISMATCH"])
        d = Path(r["run_dir"])
        m, proc, tb = read(d / "manifest.json"), read(d / "process.json"), read(d / "tb_result.json")
        tb["uvm_errors"] = 2
        write(d / "mutated.json", tb)
        judged = evaluate(m, proc, d / "mutated.json", d / "sim.log")
        self.assertEqual(judged["acceptance"], "FAIL")
        with (d / "sim.log").open("a", encoding="utf-8") as stream:
            stream.write("UVM_ERROR @ 20: mock [MOCK_MISMATCH] late duplicate\n")
        judged = evaluate(m, proc, d / "tb_result.json", d / "sim.log")
        self.assertEqual(judged["acceptance"], "FAIL")
        self.assertIn("LOG_ERROR", judged["reasons"])

    def test_result_type_identity_and_sw_contract(self):
        r = self.launch()
        directory = Path(r["run_dir"])
        m = read(directory / "manifest.json")
        original = read(directory / "tb_result.json")
        process = read(directory / "process.json")
        mutations = [("checks_count", True), ("seed", True), ("seed", 42),
                     ("profile", "n2_boot"), ("test", "different"),
                     ("schema_version", True), ("software_required", 0)]
        for field, value in mutations:
            with self.subTest(field=field, value=value):
                tb = copy.deepcopy(original)
                tb[field] = value
                write(directory / "mutated.json", tb)
                judged = evaluate(m, process, directory / "mutated.json", directory / "sim.log")
                self.assertEqual(judged["acceptance"], "FAIL")
        m["profile"]["software_required"] = True
        write(directory / "mutated.json", original)
        judged = evaluate(m, process, directory / "mutated.json", directory / "sim.log")
        self.assertIn("SOFTWARE_REQUIREMENT_MISMATCH", judged["reasons"])
        self.assertEqual(judged["status"], "FAIL")

    def test_cli_ascii_stdout_with_unicode_paths(self):
        env = dict(os.environ, PYTHONIOENCODING="ascii")
        command = [sys.executable, str(ROOT / "script" / "socflow.py"),
                   "run", "--profile", "mock", "--out", str(self.out), "--timeout", "10"]
        proc = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              env=env, encoding="ascii", timeout=30)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(json.loads(proc.stdout)["status"], "PASS")

    def test_late_assertion_log_is_failure(self):
        r = self.launch()
        d = Path(r["run_dir"])
        for prefix in ("SOC_ASSERT_ERROR", "SOC_ASSERTION_ERROR"):
            with self.subTest(prefix=prefix):
                log = d / "assertion_late.log"
                log.write_text(prefix + " [LATE_SVA] after result\\n", encoding="utf-8")
                judged = evaluate(read(d / "manifest.json"), read(d / "process.json"),
                                  d / "tb_result.json", log)
                self.assertEqual(judged["acceptance"], "FAIL")
                self.assertIn("LOG_ERROR", judged["reasons"])

    def test_info_containing_error_is_not_failure(self):
        r = self.launch()
        directory = Path(r["run_dir"])
        with (directory / "sim.log").open("a", encoding="utf-8") as stream:
            stream.write("UVM_INFO @ 10: tb [STATUS] error injection disabled\n")
            stream.write("UVM_ERROR : 0\nUVM_FATAL : 0\n")
        judged = evaluate(read(directory / "manifest.json"), read(directory / "process.json"),
                          directory / "tb_result.json", directory / "sim.log")
        self.assertEqual(judged["status"], "PASS")

    def test_unique_run_and_reproduce(self):
        first = self.launch(seed=777)
        second = reproduce(first["run_dir"], self.out)
        self.assertNotEqual(first["run_dir"], second["run_dir"])
        self.assertEqual(second["seed"], 777)
        self.assertEqual(second["status"], "PASS")
        m = read(Path(second["run_dir"]) / "manifest.json")
        self.assertEqual(m["parent_run"], first["run_id"])
        with self.assertRaises(FileExistsError):
            worker(Path(first["run_dir"]) / "manifest.json")

    def test_build_tamper_rejected(self):
        artifact = next(iter(self.b["artifacts"]))
        Path(artifact).write_text("changed", encoding="utf-8")
        with self.assertRaises(FlowError):
            check_build(self.b, "mock")

    def test_profile_and_lsf_blocked(self):
        for name in ("vip_selftest", "cmn_bfm", "n2_boot"):
            with self.subTest(profile=name), self.assertRaises(FlowError) as caught:
                run(name, "vcs", self.out, dry_run=True)
            self.assertEqual(caught.exception.status, "BLOCKED")
        with self.assertRaises(FlowError) as caught:
            self.launch(scheduler="lsf")
        self.assertEqual(caught.exception.status, "BLOCKED")
        with self.assertRaises(FlowError):
            build("uvm_selftest", "vcs", self.out, site=self.out / "missing.json")

    def test_dry_run_never_runs_mock(self):
        r = run("mock", "vcs", self.out, dry_run=True)
        self.assertEqual(r["status"], "PLANNED")
        self.assertFalse((Path(r["run_dir"]) / "worker.claim").exists())
        self.assertFalse((Path(r["run_dir"]) / "tb_result.json").exists())

    def test_parallel_regression_and_incomplete_report(self):
        spec = dict(schema_version=1, name="parallel", kind="normal", profile="mock",
                    cases=[dict(name="pass", seeds=[1, 2, 3], timeout_s=5)])
        path = self.out / "suite.json"
        write(path, spec)
        summary = regress(path, "vcs", self.out, jobs=3)
        self.assertEqual(summary["accepted_count"], 3, summary)
        self.assertEqual(summary["status"], "PASS")
        victim = Path(summary["runs"][0]["run_dir"]) / "result.json"
        victim.unlink()
        incomplete = report(summary["report_dir"])
        self.assertEqual(incomplete["status"], "FAIL")
        self.assertEqual(incomplete["planned_count"], 3)

    def test_suite_guards(self):
        with self.assertRaises(FlowError):
            validate(dict(schema_version=1, kind="normal", profile="mock", cases=[]))
        with self.assertRaises(FlowError):
            validate(dict(schema_version=1, kind="normal", profile="mock",
                          cases=[dict(name="bad", expected_failures=["ERROR"])]))
        with self.assertRaises(FlowError):
            validate(dict(schema_version=1, kind="negative_selftest", profile="mock",
                          cases=[dict(name="bad")]))

    def test_config_generation_and_overlap(self):
        out = self.out / "generated"
        generated = generate(ROOT / "config" / "design.example.json", out)
        self.assertEqual(generated["status"], "GENERATED")
        self.assertIn("DEMO_RAM_BASE", (out / "soc_generated_cfg_pkg.sv").read_text())
        with self.assertRaises(FlowError):
            generate(ROOT / "config" / "design.example.json", out)
        data = read(ROOT / "config" / "design.example.json")
        data["regions"][1]["base"] = data["regions"][0]["base"]
        path = self.out / "overlap.json"
        write(path, data)
        with self.assertRaises(FlowError):
            generate(path, self.out / "bad")


if __name__ == "__main__":
    unittest.main()
