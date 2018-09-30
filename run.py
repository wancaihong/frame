# -*- coding:utf-8 -*-
# !/usr/bin/python
__author__ = 'wancaihong'
__date__ = '2018/9/27 20:57'

import unittest
import time
import HTMLTestRunner

def get_test_cases(dirpath):
    test_cases = unittest.TestSuite()
    suites = unittest.defaultTestLoader.discover(dirpath, 'test*.py', top_level_dir=dirpath)
    for suite in suites:
        test_cases.addTests(suite)
    return test_cases

if __name__ == '__main__':
    cases = get_test_cases('case/baidu')
    now = time.strftime("%Y-%m-%d_%H_%M_%S_")
    # 设置报告位置与文件名
    filename = '.\\report\\'+now+'report.html'
    f = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=u'Page Object Demo Test', description=u'详细测试结果如下:')
    runner.run(cases)
    f.close()