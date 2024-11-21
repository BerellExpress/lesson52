import unittest
from RunnerTest import RunnerTest
import logging
import code_for_log

test_suite = unittest.TestSuite()

runner_tests = unittest.TestLoader().loadTestsFromTestCase(RunnerTest)
test_suite.addTests(runner_tests)

runner = unittest.TextTestRunner(verbosity=2)
results = runner.run(test_suite)

