import HtmlTestRunner
import unittest

from HtmlTestRunner.runner import HTMLTestRunner


from tests.test_login import TestLogin


class TestSuite(unittest.TestCase):

    def test_suite(self):
        test_runs = unittest.TestSuite()

        test_runs.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin))


        runner = HTMLTestRunner(
            report_name="Report name",
            combine_reports=True,
            report_title="Title raport"
        )
        runner.run(test_runs)