#!/usr/bin/env python 
# -*- coding:utf-8 -*-

aa = '012345'
print(aa[0:4])
print(aa[2:])


str1 = '1,2,3'
arr = str1.split(',')
print(arr)


# str1 = ''.join(arr).find('2')
# print(str1)
#
# degree_tmp = ['初中及以下', '高中', '中技', '中专', '大专', '本科', '硕士', '博士']
# str2 = ''.join(degree_tmp).find('中专')
# print(str2 >= 0)

aa = ''
strs = ['广州-黄埔区', '无工作经验', '招10人', '05-08发布', '本科', '普通话良好', '计算机科学与技术']
for str3 in strs:
    print(str3)
    degree_tmp = ['初中及以下', '高中', '中技', '中专', '大专', '本科', '硕士', '博士']
    str2 = ''.join(degree_tmp).find(str3)
    if str2 >= 0 :
        aa = str3

print(aa)