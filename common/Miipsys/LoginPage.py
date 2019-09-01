# -*- coding:utf-8 -*-  
# !/usr/bin/python
#__author__='wancaihong'
#__date__='2018/10/14 22:38'
"""
该页面主要保存登陆页面相关的API
"""

import common.BasePage
import common.Miipsys.Miip_Widget

class Login_Page(common.BasePage.BasePage):

	# 调用widget页面
	miip_widget = common.Miipsys.Miip_Widget.Widget

	def add_loginname(self, login_name):
		"""
		:introduction: 输入登录名
		:parameter: loginname:登录名
		:return: None
		"""
		login_name_but = self.driver.get_element(self.miip_widget.loginname_but)
		login_name_but.send_keys(login_name)

	def add_password(self, password):
		"""
		:introduction: 输入密码
		:parameter: password:密码
		:return: None
		"""
		password_but = self.driver.get_element(self.miip_widget.password_but)
		password_but.send_keys(password)

	def add_check_code(self, check_code):
		"""
		:introduction: 输入验证码
		:parameter: check_code:验证码
		:return: None
		"""
		check_code_but = self.driver.get_element(self.miip_widget.checkcode_but)
		# check_code_but = self.driver.wait_element_by_name('checkcode')
		check_code_but.send_keys(check_code)

	def click_login(self):
		"""
		:introduction: 点击登录
		:parameter:None
		:return: None
		"""
		self.driver.get_element(self.miip_widget.login_but).click()
