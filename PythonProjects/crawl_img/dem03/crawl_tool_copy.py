#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from urllib import request, error
from lxml import etree
import random

# 获取网页的源码
def get_html(url, encoding='utf-8'):
    # 1.构建一个User-agent列表 随机从列表中选择一个User-agent来模拟浏览器
    user_agents = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
                   "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
                   "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"]

    # url = "http://www.xiaohuar.com/mm/"

    try:
        # 生成请求对象
        req = request.Request(url)
        req.add_header("User-Agent", random.choice(user_agents))

        # 发送请求 并接受响应对象
        response = request.urlopen(req)
        # 读取数据
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
