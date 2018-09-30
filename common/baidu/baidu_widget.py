# -*- coding:utf-8 -*-
# !/usr/bin/python
__author__='wancaihong'
__date__='2018/9/30 21:59'
"""
该页面主要保存需要用到的页面控件信息等,以便API调用
"""

import common.BasePage

class Widget(common.BasePage.BasePage):
	# 通过id定位搜索框
	search_box = "id>>>kw"

	# 通过id定位"百度一下"button"
	search_button = "id>>>su"