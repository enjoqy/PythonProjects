#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from urllib import request, error
import random
from lxml import etree
import os
from crawl_img_final.cral_img03 import crawl_heade

def get_html(url, encoding='utf-8'):
    # 模拟请求头，防止反爬封ip
    # user_agents = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    #                "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    #                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    #                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    #                "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"]
    user_agents = crawl_heade.get_heade()

    try:
        # 增加随机请求头
        req = request.Request(url)
        req.add_header("User-Agent", user_agents)
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
        # 写入到本地文件
        f = open(filepath + img_name, 'wb')
        f.write(request.urlopen(img_url).read())
        print('下载图片：', filepath + img_url)
        f.flush()
        f.close()


def download_subpage(url, spage_url, spage_name, filepath='H://test/'):
    print('获取一个子页链接: ' + spage_url)

    # 判断是否存在，创建文件夹
    if not spage_name == '' or not os.path.exists(filepath + spage_name):
        os.mkdir(filepath + spage_name)
        filepath_last = filepath + spage_name + '/'
        print('创建文件夹： ' + filepath_last)
    else:
        filepath_last = filepath
    # 获取子页html内容
    sub_page_html = get_html(spage_url)
    # 数据清洗
    sub_page_content = etree.ElementTree(etree.HTML(sub_page_html))
    # 获取子页图片链接
    sub_page_img_urls = sub_page_content.xpath(r'//*[@class="ImageBody"]/p/a/img/@src')

    # 下载子页图片
    if not len(sub_page_img_urls) == 0:
        download(sub_page_img_urls[0], filepath_last)

    # 获取子页的下一页链接
    spage_apge_url = sub_page_content.xpath(r'//*[@class="pages"]/ul/li/a/@href')
    # print(spage_apge_url[-1])

    if len(spage_apge_url) != 0 or spage_apge_url[-1] != '#':
        spage_spage_url_last = url + spage_apge_url[-1]
        # print(spage_spage_url_last)
        download_subpage(url, spage_spage_url_last, '', filepath_last)
        # print('递归循环')
    else:
        print('子页已无链接')
        return None


