#!/usr/bin/env python
# -*- coding:utf-8 -*-
from crawl_img.dem03 import crawl_tool_copy as tool
from lxml import etree
import urllib
from concurrent.futures import ThreadPoolExecutor

# 数据抓取
# url = 'http://www.baidu.com'
url = 'http://www.girlsky.cn/mntp/xgmn/'
context = tool.get_html(url, 'utf-8')
# print(context)

# 2 数据清洗  转换成元素树
html = etree.ElementTree(etree.HTML(context))
# print(html)

# 3.使用xpath语法对数据进行清洗
# els = html.xpath(r'//div[@id="resultList"]/div[@class="el"]')  # /html/body/div[2]/div[7]
els = html.xpath(r'//div[@class="TypeList"]')  # /html/body/div[2]/div[7]

# 4.遍历每一行的数据  /html/body/div[2]/div[7]

def download(el):
    el = etree.ElementTree(el)
    print(el)
    position = el.xpath(r'p/span/a/@title')
    img = el.xpath(r'ul/li/a/img/@src')
    for url in img:
        print(url)
        if (url.find('.') != -1):
            name = url[-8:]
            f = open("H://pythonimg/" + name, 'wb')
            bytes = urllib.request.urlopen(url)
            f.write(bytes.read())
            f.flush()
            f.close()

# 开启多线程
def main():
    with ThreadPoolExecutor(8) as executor:
        executor.map(download, els)

if __name__ == '__main__':
    main()
