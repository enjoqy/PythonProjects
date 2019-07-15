#!/usr/bin/env python
# -*- coding:utf-8 -*-
from crawl_img_final.crawl_img_mzitu_01 import crwal_img_mzitu_tools
import requests
from lxml import html
from concurrent.futures import ThreadPoolExecutor

# 获取主页的分页
def getBasePage():
    baseUrl = 'https://www.mzitu.com/'
    selector = html.fromstring(requests.get(baseUrl).content)
    number = selector.xpath(r'//div[@class="nav-links"]/a[@class="page-numbers"]/text()')[-1]

    # 将主页的分页链接丢到集合中
    urls = []
    for i in range(int(number)):
        url = baseUrl + 'page/' + str(i) + '/'
        # print(url)
        urls.append(url)
    return urls


# 将工具类的方法串起来
def threadTmp(url):
    # 根据传入的url获取子页的链接
    urls = crwal_img_mzitu_tools.getPage(url)
    for spage_url in urls:
        # 返回标题，图片url集合
        title, jpgList = crwal_img_mzitu_tools.getPiclink(spage_url)
        # 下载图片
        crwal_img_mzitu_tools.download(title, jpgList)


def main():
    with ThreadPoolExecutor(10) as executor:
        for url in getBasePage():
            executor.submit(threadTmp, url)


if __name__ == '__main__':
    main()
