#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from crawl_img_final.cral_img01 import crawl_img_tools02
from lxml import etree
from urllib import request, error

url = 'http://www.girlsky.cn/mntp/xgmn/'

# 获取网页源码
html = crawl_img_tools02.get_html(url)

# 数据清洗
content = etree.ElementTree(etree.HTML(html))

# 获取子页链接
sub_page_urls = content.xpath(r'//*[@class="TypeList"]/ul/li/a/@href')

for sub_page_url in sub_page_urls:
    # print(sub_page_url)
    # 获取html
    sub_page_html = crawl_img_tools02.get_html(sub_page_url)
    # 数据清洗
    sub_page_content = etree.ElementTree(etree.HTML(sub_page_html))
    # 获取子页图片链接
    sub_page_img_urls = sub_page_content.xpath(r'//*[@class="ImageBody"]/p/a/img/@src')
    print(sub_page_img_urls)

    if not len(sub_page_img_urls) == 0:
        crawl_img_tools02.download(sub_page_img_urls[0], 'H://test/')




