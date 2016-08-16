#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import re  

a = []

relink = re.compile(r'\w+')
with open('0004.txt', 'r') as f:
	for line in f:
		line = relink.findall(line)
		print line
		a.append(len(line))
	print sum(a)
		