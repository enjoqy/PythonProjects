#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from lxml import html
import os
from concurrent.futures import ThreadPoolExecutor
import time

# 反爬虫
def header(referer):
    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers




# 获取主页列表
def getPage(baseUrl):
    print('打开链接： \t' + baseUrl)
    # baseUrl = 'https://www.mzitu.com/'
    selector = html.fromstring(requests.get(baseUrl).content)

    urls = []
    for i in selector.xpath(r'//ul[@id="pins"]/li/a/@href'):
        urls.append(i)
    # print(urls)
    return urls


# 返回标题和图片地址的列表
def getPiclink(url):
    sel = html.fromstring(requests.get(url).content)
    # 获取子页的总数
    total = sel.xpath(r'//div[@class="pagenavi"]/a/span/text()')[-2]
    # 获取标题
    title = sel.xpath(r'//h2[@class="main-title"]/text()')

    # 子页链接放到这个列表中
    jpgList = []

    for i in range(int(total)):
        # 每一页
        link = '{}/{}'.format(url, i+1)
        s = html.fromstring(requests.get(link).content)
        # 获取图片地址
        jpg = s.xpath(r'//div[@class="main-image"]/p/a/img/@src')[0]
        jpgList.append(jpg)
    return title, jpgList


# 图片下载
def download(title, jpgList):
    k = 1
    dirName = 'H://test03/' + title[0]
    # 新建文件夹
    if not os.path.exists(dirName):
        os.mkdir(dirName)

    for i in jpgList:
        print(i)
        fileName = '%s/%s.jpg'%(dirName, k)
        print('开始下载： \t' + fileName)

        with open(fileName, 'wb') as jpg:
            jpg.write(requests.get(i, headers=header(i), timeout=1).content)
            time.sleep(0.5)
        k += 1



#
# for url in getPage():
#     # title, jpgList = getPiclink(url)
#     # download(title, jpgList)
#     getBasePage()