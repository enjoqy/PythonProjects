#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from urllib import request, error
from lxml import etree
import urllib
import random
import os

def get_html(url, encoding='utf-8'):
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


def download_img(urls, file_path, img_names):
    print('开始下载: ')
    i = 0
    for url in urls:
        img_name = img_names[i]
        f = open(file_path + img_name + '.jpg', 'wb')
        print(file_path + img_name + '.jpg')
        i += 1
        f.write(request.urlopen(url).read())
        f.flush()
        f.close()

def download_img_subpage(urls, file_path, img_names):
    i = 0
    # print('爬取第: ' + i + ' 个子页')
    for img_name in img_names:
        if not os.path.exists(file_path + img_name):
            os.makedirs(file_path + img_name)
    for url_subpage in urls:
        content = get_html(url_subpage)
        html = etree.ElementTree(etree.HTML(content))
        els = html.xpath(r'//*[@class="ImageBody"]')

        # 需要重构
        # next_pages = html.xpth(r'//*[@class="pages"]')

        for el in els:
            el = etree.ElementTree(el)
            urls_subpages = el.xpath(r'p/a/img/@src')
            for urls_subpage in urls_subpages:
                img_name_page = urls_subpage.split('/')[-1]
                print(img_name_page)
                f = open(file_path + img_names[i] + '/' + img_name_page, 'wb')
                i += 1
                print(file_path + img_names[i] + '/'  + img_name_page)
                f.write(request.urlopen(urls_subpage).read())
                f.flush()
                f.close()
