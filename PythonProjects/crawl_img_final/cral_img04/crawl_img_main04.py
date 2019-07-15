#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from urllib import request
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
from crawl_img_final.cral_img04 import crawl_img_tools04

"""

1,获取网页源码

2，解析网页源码获取指定数据

3，存储获得的数据

"""
# url = 'http://www.girlsky.cn/mntp/xgmn/'
# url = 'http://www.girlsky.cn/mntp/gzmn/'
# url = 'http://www.girlsky.cn/mntp/swmn/'
url = 'http://www.girlsky.cn/mntp/swmn/'
filepath = 'H://test/'

# 获取第二页的链接
s_url = crawl_img_tools04.get_spage_urls(url)
print(s_url)

while True:
    # 1,获取网页源码
    html = crawl_img_tools04.get_html(url)
    # 数据清洗
    content = etree.ElementTree(etree.HTML(html))
    # 解析源码获取子链接的地址
    spage_urls = content.xpath(r'//*[@class="TypeList"]/ul/li/a/@href')

    # 解析源码中的写真名字，进行创建文件夹
    spage_names = content.xpath(r'//*[@class="TypeList"]/ul/li/a/span/text()')


    def main():
        with ThreadPoolExecutor(10) as executor:
            i = 0
            for spage_url in spage_urls:
                print('开启一个线程')
                executor.submit(crawl_img_tools04.download_spage, url, spage_url, spage_names[i], filepath)
                i += 1

    if __name__ == '__main__':
        main()

    # 获取第二页的链接
    url = crawl_img_tools04.get_spage_urls(url)

    print(url)