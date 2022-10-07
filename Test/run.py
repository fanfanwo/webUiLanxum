import unittest

from execute.HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

testcase = unittest.TestLoader().discover(r"testcase/testcases","test*.py")

runner = HTMLTestRunner(open("testcase/reports/run_by_html_test_runner.html","w"),verbosity=2,title="自动化登录用例执行结果",description="运行者范聪瑶")

runner.run(testcase)