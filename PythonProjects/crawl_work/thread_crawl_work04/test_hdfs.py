#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from pyhdfs import HdfsClient

'''
python链接hadoop的hdfs文件系统，进行文件的上传和下载
'''

# 从hdfs文件系统读取文件

# hdfs地址
# client = HdfsClient(hosts='192.168.1.163:50070')
client = HdfsClient(hosts='192.168.1.156:50070')

print(client.listdir("/repo/"))

res = client.open('/repo/README.txt')
for r in res:
    line = str(r, encoding='utf-8')  # open后是二进制,str()转换为字符串并转码
    print(line)

client = HdfsClient(hosts='192.168.1.156:50070', user_name='hadoop')  # 只有hadoop用户拥有写权限
str1 = 'hello world'
client.create('/py.txt', str1)  # 创建新文件并写入字符串





# 上传本地文件到HDFS

# client = HdfsClient(hosts='hacker:50070', user_name='root')
# 本地文件绝对路径,HDFS目录必须不存在
# client.copy_from_local('D:/PythonProjects/crawl_work/thread_crawl_work02', '/usr/hadoop/')