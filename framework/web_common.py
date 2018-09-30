# -*- coding:utf-8 -*-
# !/usr/bin/python
__author__ = 'wancaihong'
__date__ = '2018/9/25 22:54'

import time
import os
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class WebCommon(object):

	def delay(self, sec=1):
		'''
		:param sec:
		:return:
		'''
		time.sleep(sec)

	def wait_element_by_xpath(self, xpath, timeout=5):
		'''
		:param xpath:
		:param timeout:
		:return:
		'''
		try:
			elemennt = WebDriverWait(self, timeout).until(
				lambda x: x.find_element_by_xpath(xpath))
		except NoSuchElementException:
			elemennt = None
		return elemennt

	def wait_element_by_id(self, id, timeout=5):
		'''
		:param xpath:
		:param timeout:
		:return:
		'''
		try:
			elemennt = WebDriverWait(self, timeout,ignored_exceptions=NoSuchElementException).until(
				lambda e: e.find_element_by_xpath(id)
				if e.find_find_element_by_xpath(id).is_displayed() else False)
		except NoSuchElementException:
			elemennt = None
		return elemennt