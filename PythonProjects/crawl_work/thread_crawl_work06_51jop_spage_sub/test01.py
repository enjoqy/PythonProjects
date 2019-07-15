#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np

def process_char(strs):
    rows = []
    degree_tmp = ['初中及以下', '高中', '中技', '中专', '大专', '本科', '硕士', '博士']
    work_exp = ''
    degree = ''
    hiring_number = ''
    for str1 in strs:
        print(str1)
        # 工作经验要求
        if '验' in str1:
            work_exp = str1

        # 学历要求
        elif ''.join(degree_tmp).find(str1) >= 0:
            degree = str1
        # 招多少人
        elif '人' in str1:
            hiring_number = str1
        # else:
            # rows.append('')

    rows = [strs[0], work_exp, degree, hiring_number]
    # rows.append(strs[0])
    # rows.append(work_exp)
    # rows.append(degree)
    # rows.append(hiring_number)

    # print(rows)
    return rows


strs = ['广州-黄埔区', '无工作经验', '招10人', '05-08发布', '普通话良好', '计算机科学与技术',  '本科']

process_char(strs)