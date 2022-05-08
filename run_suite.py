# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/6 15:18
@Auth ： 李江
@Company ：李江
@Function ：请输入模块功能描述
"""
import unittest
import app,time
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from script.login import login

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(login))
report_file = app.BASE_DIR + '/report/report{}.html'.format(time.strftime("%Y%m%d %H%M%S"))

with open(report_file,'wb') as f:
    runner = HTMLTestRunner(f,title="P2P测试报告",description="test")
    runner.run(suite)
