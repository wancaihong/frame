# -*- coding:utf-8 -*-  
# !/usr/bin/python
#__author__='wancaihong'
#__date__='2018/10/14 22:23'
"""
该页面主要保存需要用到的页面控件信息等,以便API调用
usage: widge_name = "ele>>>kw"
ele = 'id','name','xpath','css','tag','class','text','link_text'
"""

import common.BasePage

class Widget(common.BasePage.BasePage):

	# 登录名输入框
	loginname_but = "name>>>loginname"

	# 密码输入框
	password_but = "name>>>password"

	# 验证码输入框
	checkcode_but = "name>>>checkcode"

	# 登录按钮
	login_but = "xpath>>>/html/body/div[1]/form/div/div/a"

	# 验证码错误提示
	error_security_code_remind = "xpath>>>/html/body/div[1]/form/div/div/div/span"

	# 异常错误弹出框
	error_account_remind = "xpath>>>/html/head/script[5]"