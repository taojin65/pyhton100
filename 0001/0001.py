#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import random

def rand():
	code_list = []
	for i in range (10):
		code_list.append(str(i))
	for i in range (65, 91): # A-Z
		code_list.append(chr(i)) # 把acsii编码的字母转化成string
	for i in range (97, 123): # a-z
		code_list.append(chr(i))
	# print code_list
	code_rand = "".join(random.sample(code_list, 10))
	return code_rand

n = 200
while n > 0:
	print rand()
	n = n - 1
	n = n - 1

