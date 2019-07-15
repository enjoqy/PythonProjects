#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from urllib import request
from lxml import etree
from crawl_img_final.cral_img04 import crawl_img_tools03

"""

1,获取网页源码

2，解析网页源码获取指定数据

3，存储获得的数据

"""

url = 'http://www.girlsky.cn/mntp/xgmn/'
filepath = 'H://test/'

# 1,获取网页源码
html = crawl_img_tools03.get_html(url)

# 数据清洗
content = etree.ElementTree(etree.HTML(html))
# 解析源码获取子链接的地址
spage_urls = content.xpath(r'//*[@class="TypeList"]/ul/li/a/@href')

for spage_url in spage_urls:
    crawl_img_tools03.download_spage(url, spage_url, filepath)


    # # 对子网页数据进行清洗
    # spange_html = crawl_img_tools03.get_html(spage_url)
    # spage_content = etree.ElementTree(etree.HTML(spange_html))
    # spage_imgs = spage_content.xpath(r'//*[@class="ImageBody"]/p/a/img/@src')
    # if len(spage_imgs) > 0:
    #     spage_img = spage_imgs[0]
    #
    #     # 下载图片
    #     crawl_img_tools03.download(spage_img)
