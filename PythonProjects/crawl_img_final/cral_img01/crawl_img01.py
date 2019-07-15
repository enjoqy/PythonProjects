#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from urllib import request
from lxml import etree

url = 'http://www.girlsky.cn/mntp/xgmn/'

# 打开链接
response = request.urlopen(url)
# 输出了响应的状态码
# print(response.status)
# 响应的头信息
# print(response.getheaders())
# 获取网页源码
html = response.read().decode('utf-8')
# print(html)

# 数据清洗
content = etree.ElementTree(etree.HTML(html))

# 拿到img的url数组
img_urls = content.xpath(r'//*[@class="TypeList"]/ul/li/a/img/@src')

for img_url in img_urls:
    # download(img_url)
    # print(img_url)
    # img_name = img_url.split('/')
    # print(img_name)

    # 截取img_url的名字
    img_name = img_url.split('/')[-1]
    # print(img_name)

    # 写入到本地文件
    f = open('H://test/' + img_name, 'wb')
    f.write(request.urlopen(img_url).read())
    print('下载图片：', img_url)
    f.flush()
    f.close()
