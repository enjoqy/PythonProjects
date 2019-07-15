#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import impala as ipdb
conn = ipdb.connect(host="localhost",port=3306,user="root",password="1234",database="mypython",auth_mechanism='PLAIN')
cursor = conn.cursor()
cursor.execute('select * From 51job_java')
print(cursor.description)
for rowData in cursor.fetchall():
    print(rowData)
conn.close()
# ipdb.connet()



