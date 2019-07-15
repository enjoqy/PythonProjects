#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
from crawl_img.thread_crawl02 import thread_crawl_tools

'''
爬虫的主方法，在这里写逻辑
'''

url = 'http://www.girlsky.cn/mntp/xgmn/'
file_path = 'H://pythonimg/'

content = thread_crawl_tools.get_html(url)
# 数据清洗
html = etree.ElementTree(etree.HTML(content))

# 获取子链接数组
els = html.xpath(r'//*[@class="TypeList"]')
for el in els:
    el = etree.ElementTree(el)
    sub_page_urls = el.xpath(r'ul/li/a/@href')

# 获取子链接数组的名字，用来创建文件夹
el_names = html.xpath(r'//*[@class="TypeList"]/ul/li/a/span/text()')

# 开启线程池
def main():
    with ThreadPoolExecutor(8) as executor:
        i = 0
        for sub_page_url in sub_page_urls:
            executor.submit(thread_crawl_tools.img_sub_page_download, sub_page_url, el_names[i])
            i += 1

# 开启线程池进行下载
if __name__ == '__main__':
    main()
