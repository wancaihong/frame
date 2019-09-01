# -*- coding:utf-8 -*-  
# !/usr/bin/python
#__author__='wancaihong'
#__date__='2018/10/16 22:38'

"""
case:测试错误密码登录system系统
"""

import unittest
import sys
sys.path.append("..")
from framework.PublicMethod import PublicMethod
from framework.configfile import miip_system_info
from common.Miipsys import LoginPage

class logintest(unittest.TestCase):

	def setUp(self):
		# 实例化utils下PublicMethod类
		self.driver = PublicMethod(miip_system_info['browser'])
		self.driver.wd.implicitly_wait(30)
		self.driver.max_window()

	def tearDown(self):
		self.driver.quit()

	def test_error_login_system(self):
		driver = self.driver
		loginpage = LoginPage.Login_Page(driver)
		self.driver.open_link(miip_system_info['url'])
		loginpage.add_loginname(miip_system_info['loginname'])
		loginpage.add_password(miip_system_info['password'])
		loginpage.add_check_code(miip_system_info['checkcode'])
		loginpage.click_login()
		self.driver.wait(3)
		# 验证是否进入主页
		title_system = self.driver.get_title()
		title_name = '手机一卡通卡务平台'
		self.assertEqual(title_name, title_system)