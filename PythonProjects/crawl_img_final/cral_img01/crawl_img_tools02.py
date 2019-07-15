#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from urllib import request, error
import random


def get_html(url, encoding='utf-8'):
    # 模拟请求头，防止反爬封ip
    user_agents = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
                   "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
                   "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"]
    try:
        # 增加随机请求头
        req = request.Request(url)
        req.add_header("User-Agent", random.choice(user_agents))
        response = request.urlopen(req)
        # 获取网页源码
        html = response.read().decode('utf-8')
        return html
    except error.URLError as e:
        # URLError
        # 产生的原因主要有：
        # 1.没有网络连接
        # 2.服务器连接失败
        # 3.找不到指定的服务
        print("URL异常{}".format(e.reason))
    except error.HTTPError as e:
        # HTTPError 获取响应状态码来判断响应失败的原因
        print("HTTP异常{}".format(e.reason))
        return None


# 下载图片
def download(img_url, filepath='H://test/'):
    if not img_url == '':
        # 截取img_url的名字
        img_name = img_url.split('/')[-1]
        print(img_name)
        # 写入到本地文件
        f = open(filepath + img_name, 'wb')
        f.write(request.urlopen(img_url).read())
        print('下载图片：', img_url)
        f.flush()
        f.close()

