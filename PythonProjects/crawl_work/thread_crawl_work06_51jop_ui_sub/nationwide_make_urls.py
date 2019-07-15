#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time: 2019/5/16 001612:11
# @Author: junhi

# 平面设计
url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,%25E5%25B9%25B3%25E9%259D%25A2,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

# 大数据
# url = 'https://search.51job.com/list/050000,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

# 云计算
# url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,%25E4%25BA%2591%25E8%25AE%25A1%25E7%25AE%2597,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
provinces = [
    '北京', '上海', '广东省', '深圳', '天津', '重庆', '江苏省', '浙江省',
    '四川省', '海南省', '福建省', '山东省', '江西省', '广西', '安徽省', '河北',
    '河南省', '湖北省', '湖南省', '陕西省', '山西省', '黑龙江省', '辽宁省', '吉林省',
    '云南省', '贵州省', '甘肃省', '内蒙古', '宁夏', '西藏', '新疆', '青海省',
    ]

def get_nationwide_urls():
    i = 1
    nationwide_java_urls = {}
    for province in provinces:
        if i <= 9:
            province_url = url[0:31] + str(i) + url[32:]
        else:
            province_url = url[0:30] + str(i) + url[32:]
        nationwide_java_urls[province] = province_url
        i = int(i)
        if i == 32:
            break
        i += 1
    return nationwide_java_urls
