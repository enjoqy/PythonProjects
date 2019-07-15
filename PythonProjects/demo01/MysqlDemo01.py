#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "1234", "mydb")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("select * from info")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
fetchall = cursor.fetchall()

print(data)
print(fetchall)

# 执行插入操作
sql = "insert into info (" \
      "name, age, sex, phone, address)" \
      "values " \
      "(\"python\", 1.0, \"未知\", 111, \"哈哈\")"
cursor.execute(sql)
db.commit()

cursor.execute("select * from info")
fetchall = cursor.fetchall()
print(fetchall)

db.close()
