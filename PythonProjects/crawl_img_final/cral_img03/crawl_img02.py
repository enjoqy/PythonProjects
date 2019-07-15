#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from crawl_img_final.cral_img03 import crawl_img_tools02
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

url = 'http://www.girlsky.cn/mntp/xgmn/'
filepath = 'H://test/'

# 获取网页源码
html = crawl_img_tools02.get_html(url)
# 数据清洗
content = etree.ElementTree(etree.HTML(html))
# 获取子页链接
sub_page_urls = content.xpath(r'//*[@class="TypeList"]/ul/li/a/@href')

# 获取文件夹名字
spage_name = content.xpath(r'//*[@class="TypeList"]/ul/li/a/span/text()')
# print(spage_name)

# i = 0
# 传入子页链接进行循环下载
# for sub_page_url in sub_page_urls:
#     crawl_img_tools02.download_subpage(url, sub_page_url, spage_name[i], filepath)
#     i += 1

# 开启线程池
def main():
    with ThreadPoolExecutor(10) as executor:
        i = 0
        # 传入子页链接进行循环下载
        for sub_page_url in sub_page_urls:
            executor.submit(crawl_img_tools02.download_subpage, url, sub_page_url, spage_name[i], filepath)
            i += 1

if __name__ == '__main__':
    main()
