# -*- coding:utf-8 -*-  
# !/usr/bin/python
#__author__='wancaihong'
#__date__='2019/4/7 12:36'

"""
case:获取100以内的合数
"""

import unittest

class logintest(unittest.TestCase):

	def test_get_composite_number(self):
		list = []
		for i in range(2, 100):
			for j in range(2, i):
				if i%j == 0:
					break
			else:
				list.append(i)
		print(list)
		com_list = []
		for k in range(100):
			if k not in list:
				com_list.append(k)
		print(com_list)