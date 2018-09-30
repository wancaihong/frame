# -*- coding:utf-8 -*-
# !/usr/bin/python
__author__ = 'wancaihong'
__date__ = '2018/9/26 22:51'
"""
case:主要是查看搜索结果框显示是否正确
"""

import unittest
import time
import sys
sys.path.append("..")
from framework.PublicMethod import PublicMethod
from framework.configfile import env_info
from common.baidu import BaiduPage

class baidutest(unittest.TestCase):

    def setUp(self):
        # 实例化utils下PublicMethod类
        self.driver = PublicMethod(env_info['browser'])
        self.driver.wd.implicitly_wait(30)
        self.driver.max_window()

    def test_01_search_selenium(self):
        self._search_content(u'百度搜索Selenium', 'Selenium', u'Selenium_百度搜索')

    def test_02_search_python(self):
        self._search_content(u'百度搜索Python', 'Pyhon', u'python_百度搜索')

    def tearDown(self):
        self.driver.quit()

    def _search_content(self, description, text, expected):
        driver = self.driver
        driver.open_link(env_info['url'])
        print('case description: ', description)
        baidupage = BaiduPage.Baidu_Page(driver)
        baidupage.input_search_text(text)
        baidupage.click_search_button()
        time.sleep(3)
        self._verify_text(expected)

    # 验证搜索结果的页面title
    def _verify_text(self, expacted):
        actual_text = self.driver.get_title()
        expact_text = expacted
        self.assertEqual(actual_text, expact_text)
        # if actual_text == expact_text:
        #     pass#print 'PASS-----', 'Actual Result:', actual_text
        # else:
        #     pass#print 'FAIL-----', 'Expect Result:', expact_text, '***Actual Result:', actual_text

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(baidutest('test_01_search_selenium'))
    suite.addTest(baidutest('test_02_search_python'))
    unittest.TextTestRunner().run(suite)