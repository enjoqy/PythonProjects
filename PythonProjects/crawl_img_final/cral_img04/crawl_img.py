#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from urllib import request
from lxml import etree
"""

1,获取网页源码

2，解析网页源码获取指定数据

3，存储获得的数据

"""

url = 'http://www.girlsky.cn/mntp/xgmn/'

# 1,获取网页源码
html = request.urlopen(url).read().decode('utf-8')

# 2，解析网页源码获取指定数据
# 数据清洗
content = etree.ElementTree(etree.HTML(html))
# 解析源码获取img的地址
img_urls = content.xpath(r'//*[@class="TypeList"]/ul/li/a/img/@src')

# 3，存储获得的数据
for img_url in img_urls:
    # 获取图片名字
    img_url_name = img_url.split('/')[-1]
    # 下载的图片的路径 H://test/
    f = open("H://test/" + img_url_name, "wb")
    f.write(request.urlopen(img_url).read())

    print('下载图片： ' + "H://test/" + img_url_name)

    f.flush()
    f.close()
