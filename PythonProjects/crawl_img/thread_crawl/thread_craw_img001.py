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

for el in els:
    el = etree.ElementTree(el)
    urls = el.xpath(r'ul/li/a/@href')
    i = 1
    for url in urls:
        url = url[:-5]
        print(url)
        i = str(i)
        url = url + '_' + i + '.html'
        print(url)
        i = int(i)
        i += 1
        content = thread_crawl_tool.get_html(url)
        html = etree.ElementTree(etree.HTML(content))
        els = html.xpath(r'//*[@class="ImageBody"]/p/a/img/@src')[0]
        print(els)


