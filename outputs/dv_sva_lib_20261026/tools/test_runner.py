#!/usr/bin/env python3
"""Test regression-result classification, not SystemVerilog assertion behavior."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('dv_sva_runner', ROOT/'scripts/run_tests.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class RunnerClassification(unittest.TestCase):
    positive = {'name': 'positive', 'expect': 'pass', 'expected_ids': []}
    negative = {'name': 'negative', 'expect': 'fail', 'expected_ids': ['a_expected']}
    complete = 'DV_SVA_CASE_DONE: negative\n'
    failure = 'DV_SVA_FAIL a_expected | test.scope | deliberately violated\n'

    def test_positive(self):
        self.assertTrue(runner.evaluate(self.positive, 0, 'DV_SVA_CASE_DONE: positive\n')['passed'])

    def test_expected_failure(self):
        for status in (0, 1):
            self.assertTrue(runner.evaluate(self.negative, status, self.failure+self.complete)['passed'])

    def test_exit_code_is_not_proof(self):
        self.assertFalse(runner.evaluate(self.negative, 1, self.complete)['passed'])

    def test_extra_assertion(self):
        self.assertFalse(runner.evaluate(self.negative, 1, self.failure+'DV_SVA_FAIL a_unexpected\n'+self.complete)['passed'])

    def test_no_completion(self):
        self.assertFalse(runner.evaluate(self.negative, 1, self.failure)['passed'])

    def test_fatal_is_not_expected_failure(self):
        for text in ('** Fatal: crash', 'Fatal: vcs crash', 'xmsim: *F,CRASH', 'UVM_FATAL crash'):
            self.assertFalse(runner.evaluate(self.negative, 1, self.failure+self.complete+text)['passed'], text)

    def test_license_error(self):
        self.assertFalse(runner.evaluate(self.negative, 1, self.failure+self.complete+'license checkout failed')['passed'])

    def test_timeout_and_crash(self):
        for status in (-11, 124, 127, 2):
            self.assertFalse(runner.evaluate(self.negative, status, self.failure+self.complete)['passed'])

    def test_positive_nonzero_fails(self):
        self.assertFalse(runner.evaluate(self.positive, 1, 'DV_SVA_CASE_DONE: positive\n')['passed'])

    def test_manifest_and_simulator_commands(self):
        top, cases = runner.load_manifest()
        self.assertEqual(len(cases), 24)
        self.assertEqual(len({case['name'] for case in cases}), len(cases))
        for simulator in ('questa', 'vcs', 'xrun'):
            compile_commands, run = runner.simulator_commands(simulator, top, ROOT/'build/command tests', None)
            self.assertTrue(compile_commands)
            self.assertTrue(run)
            self.assertTrue(any(str(ROOT/'tests/dv_sva_tb.sv') in command for command in compile_commands))


if __name__ == '__main__':
    unittest.main(verbosity=2)