# -*- coding:utf-8 -*-  
__author__ = 'wancaihong'
__date__ = '2018/9/26 22:29'

class BasePage(object):
    """
    This is a base page class for Page Object.
    """
    def __init__(self, driver):
        self.driver = driver
