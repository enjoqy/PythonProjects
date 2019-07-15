#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from urllib import request, error
from lxml import etree
import random
import os

'''
爬虫的工具类
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

# 根据传入的url路径，下载文件到传入的下载路径中
def download(img_url, file_path='H://pythonimg/'):
    img_name = img_url.split('/')[-1]
    f = open(file_path + img_name, 'wb')
    print('开始下载: ', file_path + img_name)
    f.write(request.urlopen(img_url).read())
    f.flush()
    f.close()

# 根据传入的子链接找到img_url进行下载，并且模拟点击下一页按钮
def img_sub_page_download(sub_page_url, img_name, file_path='H://pythonimg/'):

    print('找到子链接: ', sub_page_url),

    # 根据原网页的名称进行创建文件夹
    if img_name != '':
        if not os.path.exists(file_path + img_name):
            os.makedirs(file_path + img_name)
            file_path_last = file_path + img_name + '/'
            print('创建文件夹: ', file_path_last)
    else:
        file_path_last = file_path + img_name

    # 数据清洗,子链接的网页源码
    sub_page_content = get_html(sub_page_url)
    sub_page_html = etree.ElementTree(etree.HTML(sub_page_content))

    # 找到图片路径进行下载
    subpage_img_urls = sub_page_html.xpath(r'//*[@class="ImageBody"]/p/a/img/@src')
    subpage_img_url = subpage_img_urls[0]
    download(subpage_img_url, file_path_last)

    # 找到下一页按钮进行模拟点击
    sub_page_button_urls = sub_page_html.xpath(r'//*[@class="pages"]/ul/li/a/@href')
    sub_page_button_url_tmp = sub_page_button_urls[-1]

    # 或得到的网页url是相对地址，需要拼接
    # 判断是不是最后一页（最后一页是#），如果是最后一页，结束循环
    if sub_page_button_url_tmp != '#':
        sub_page_button_url = 'http://www.girlsky.cn/mntp/xgmn/' + sub_page_button_url_tmp
        # 递归调用
        img_sub_page_download(sub_page_button_url, '', file_path_last)
    else:
        print('子页链接已经全部获取完毕')
        return