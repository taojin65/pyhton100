#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import MySQLdb, random

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


sql_create = "create table appstorecode (code varchar(20))"
sql_drop = "drop table if exists appstorecode"

db = MySQLdb.connect('localhost', 'root', 'root', 'test') # 链接数据库
cursor = db.cursor() # 获取游标
cursor.execute(sql_drop) # 删除表
cursor.execute(sql_create) # 建立表

n = 200
while n > 0:
	code = rand() # 创建随机数变量
	sql_insert = "insert into appstorecode value('%s')" % code  # 插入数据sql
	try:
		cursor.execute(sql_insert) # 执行SQL语句
		db.commit() # 提交插入请求
	except:
		db.rollback()
	n = n - 1
cursor.close()
db.close()
print 'done'