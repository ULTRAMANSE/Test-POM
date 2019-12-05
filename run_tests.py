import os
import time
import unittest
from config import CaseDir, ReportDir
from HTMLTestRunner import HTMLTestRunner

suit = unittest.defaultTestLoader.discover(CaseDir, pattern="*test.py")


def report_build():
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_file_name = os.path.join(ReportDir, "report" + now_time)
    report = open(report_file_name, "wb")
    runner = HTMLTestRunner(
        stream=report,
        title="哔哩哔哩首页测试报告",
        verbosity=2,
    )
    runner.run(suit)
    report.close()


if __name__ == '__main__':
    report_build()
