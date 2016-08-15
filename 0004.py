#!/usr/bin/python
# -*- coding: UTF-8 -*- 

with open ('0004.txt', 'r') as f:
	for line in f:
		line = line.replace(',', '').replace('.', '').replace('?', '').replace(';', '').replace('\t', '').replace('\n', '').strip().split(' ')
	print len(line)
