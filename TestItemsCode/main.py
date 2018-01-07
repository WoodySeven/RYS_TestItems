#!/usr/bin/env python
#author:RYS

import time
import unittest
import HTMLTestRunner

from RYS_Test_Code.Bugfree_Login_testcodes.BugfreeLoginOut import BugfreeLogin

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(BugfreeLogin))
    fp = open('RYS_Report/RYS_report_bugfree_{0}.html'.format(time.strftime("%Y-%m-%d %H-%M-%S")),'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = 'Bugfree的测试报告',
        description = 'Bugfree的所有测试用例执行细节'
    )
    runner.run(suite)
    fp.close()


