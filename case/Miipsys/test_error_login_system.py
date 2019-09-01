# -*- coding:utf-8 -*-
# !/usr/bin/python
#__author__='wancaihong'
#__date__='2018/12/2 19:48'

# -*- coding:utf-8 -*-
# !/usr/bin/python
#__author__='wancaihong'
#__date__='2018/10/16 22:38'

"""
case:测试登录system系统
"""

import unittest
import sys
sys.path.append("..")
from framework.PublicMethod import PublicMethod
from framework.configfile import miip_system_info
from common.Miipsys import LoginPage
from selenium.webdriver.remote import switch_to

class logintest(unittest.TestCase):

	def setUp(self):
		# 实例化utils下PublicMethod类
		self.driver = PublicMethod(miip_system_info['browser'])
		self.driver.wd.implicitly_wait(30)
		self.driver.max_window()

	def tearDown(self):
		self.driver.quit()

	def test_login_system(self):
		driver = self.driver
		loginpage = LoginPage.Login_Page(driver)
		self.driver.open_link(miip_system_info['url'])
		error_name = 'test'
		error_password = 'test'
		error_code = '1234'
		loginpage.add_loginname(miip_system_info[error_name])
		loginpage.add_password(miip_system_info[error_password])
		loginpage.add_check_code(miip_system_info[error_code])
		loginpage.click_login()
		self.driver.wait(3)
		# 验证是否进入主页
		# 从html页面切换到alert弹框
		alert = self.driver.switch_to.alert
		alert.accept()
		title_system = self.driver.get_title()
		title_name = '手机一卡通卡务平台'
		self.assertEqual(title_name, title_system)