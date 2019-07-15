#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from urllib import request, error
from lxml import etree
import random
import os
import csv


'''
爬取招聘网站的工具类
'''

# 根据传入的网址进行获取网页源码，默认编码是utf-8，
def get_html(url, encoding='utf-8'):
    # 模拟请求头，防止反爬封ip
    user_agents = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
                   "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
                   "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"]
    try:
        req = request.Request(url)
        req.add_header("User-Agent", random.choice(user_agents))
        response = request.urlopen(req)
        content = response.read().decode(encoding)
        return content
    except error.URLError as e:
        # URLError
        # 产生的原因主要有：
        # 1.没有网络连接
        # 2.服务器连接失败
        # 3.找不到指定的服务
        print("URL 异常 {}".format(e.reason))
    except error.HTTPError as e:
        # HTTPError 获取响应状态码来判断响应失败的原因
        print("HTTP 异常".format(e.reason))
        return None

# 根据传入的url进行数据获取
def get_one_page(url):
    print('开启一个线程')

    # 获取招聘网站的网页源码
    content = get_html(url, 'GBK')
    # 数据清洗
    html = etree.ElementTree(etree.HTML(content))

    # 获取含有信息的数组
    els = html.xpath(r'//div[@id="resultList"]/div[@class="el"]')

    rows = []  # 用于保存每一行抓取到数据
    for el in els:
        el = etree.ElementTree(el)
        job_title = el.xpath(r'p/span/a/text()')
        # 去除尾空格
        job_title = job_title[0].strip()
        # print(job_title)
        company_name = el.xpath(r'span[@class="t2"]/a/text()')  # //*[@id="resultList"]/div[4]/span[1]/a
        # print(company_name[0])
        working_place = el.xpath(r'span[@class="t3"]/text()')
        # print(working_place[0])
        salary = el.xpath(r'span[@class="t4"]/text()')
        # print(salary[])
        release_time = el.xpath(r'span[@class="t5"]/text()')
        # print(release_time[0])
        row = [job_title, company_name[0], working_place[0], salary[0], release_time[0]]
        rows.append(row)
    # print(rows)

    #  将爬虫的数据写入到csv格式文件中
    with open('thread_51jop02.txt', mode="a+", encoding="utf-8", newline = "") as f:
        # "51job.csv", mode = "a", encoding = "utf-8", newline = ""
        # 将文件的读写和csv文件进行关联
        file = csv.writer(f)
        file.writerows(rows)  # 将爬到数据一次性写入到csv格式中

    for row in rows:
        print(row)
    return rows
