#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from crawl_img_final.cral_img02 import crawl_img_tools02
from lxml import etree

url = 'http://www.girlsky.cn/mntp/xgmn/'

# 获取网页源码
html = crawl_img_tools02.get_html(url)

# 数据清洗
content = etree.ElementTree(etree.HTML(html))

# 获取子页链接
sub_page_urls = content.xpath(r'//*[@class="TypeList"]/ul/li/a/@href')

# 传入子页链接进行循环下载
for sub_page_url in sub_page_urls:
    crawl_img_tools02.download_subpage(url, sub_page_url, 'H://test/')






