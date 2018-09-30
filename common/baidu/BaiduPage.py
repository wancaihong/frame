# -*- coding:utf-8 -*-
# !/usr/bin/python
__author__ = 'wancaihong'
__date__ = '2018/9/26 22:31'
"""
该页面主要保存公共API,方便case调用
"""

import common.BasePage
import common.baidu.baidu_widget

class Baidu_Page(common.BasePage.BasePage):
    # 调用widget页面
    baidu_widget = common.baidu.baidu_widget.Widget

    # 输入搜索内容到搜索框
    def input_search_text(self, text):
        input_box = self.driver.get_element(self.baidu_widget.search_box)
        input_box.send_keys(text)

    # 点击搜索按钮
    def click_search_button(self):
        self.driver.get_element(self.baidu_widget.search_button).click()