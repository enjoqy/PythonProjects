#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from lxml import etree
from crawl_img.thread_crawl import thread_crawl_tool

url = 'http://www.girlsky.cn/mntp/xgmn/'
# url = 'http://www.girlsky.cn/mntp/jpmn/'
file_path = 'H://pythonimg/'


content = thread_crawl_tool.get_html(url)

html = etree.ElementTree(etree.HTML(content))
els = html.xpath(r'//*[@class="TypeList"]')

# for el in els:
#     el = etree.ElementTree(el)
#     urls = el.xpath(r'ul/li/a/img/@src')
#     img_names = el.xpath(r'ul/li/a/span/text()')
#     thread_crawl_tool.download_img(urls, file_path, img_names)

for el in els:
    el = etree.ElementTree(el)
    urls = el.xpath(r'ul/li/a/@href')
    img_names = el.xpath(r'ul/li/a/span/text()')


    thread_crawl_tool.download_img_subpage(urls, file_path, img_names)






