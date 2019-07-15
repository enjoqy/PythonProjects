#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from urllib import request, error
from lxml import etree
import random
import os

# 1,获取网页源码
def get_html(url, encoding='utf-8'):
    # 模拟请求头，防止反爬封ip
    user_agents = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
                   "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
                   "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"]
    try:
        # 增加请求头
        req = request.Request(url)
        req.add_header("user_agents", random.choice(user_agents))
        # 获取网页源码
        html = request.urlopen(req).read().decode(encoding)
        return html
    except error.URLError as e:
        print("URL异常{}".format(e.reason))
    except error.HTTPError as e:
        print("HTTP异常{}".format(e.reason))
    return None


# 根据传入的img的url进行下载
def download(img_url, filepath="H://test/"):
    # 获取图片名字
    img_name = img_url.split('/')[-1]
    f = open(filepath + img_name, 'wb')
    f.write(request.urlopen(img_url).read())

    print('下载图片： ' + filepath + img_name)

    f.flush()
    f.close()


def download_spage(url, spage_url, spage_name, filepath="H://test/"):
    print('获取子页链接： ' + spage_url)

    # 判断文件夹是否存在，不存在就创建
    if not os.path.exists(filepath + spage_name) and not spage_name == '':
        os.mkdir(filepath + spage_name)
        filepath_final = filepath + spage_name + "/"
    else:
        filepath_final = filepath


    # 对子网页数据进行清洗
    spange_html = get_html(spage_url)
    spage_content = etree.ElementTree(etree.HTML(spange_html))
    # 获取子网页的img的url数组
    spage_imgs = spage_content.xpath(r'//*[@class="ImageBody"]/p/a/img/@src')

    if not len(spage_imgs) == 0:
        spage_img = spage_imgs[0]
        # 下载图片
        download(spage_img, filepath_final)
    else:
        return None

    # 模拟点击下一页按钮
    spage_spage_urls_tmp = spage_content.xpath(r'//*[@class="NewPages"]/ul/div/ul/li/a/@href')
    # print(spage_spage_urls_tmp)
    spage_spage_url_tmp = spage_spage_urls_tmp[-1]

    if spage_spage_url_tmp != '#':
        # 拼接子页链接
        spage_spage_url = url + spage_spage_url_tmp
        print(spage_spage_url)
        download_spage(url, spage_spage_url, '', filepath_final)
    else:
        print('子页已无链接')
        return None


def get_spage_urls(url):
    # 获取网页源码
    html = get_html(url)
    content = etree.ElementTree(etree.HTML(html))
    # 解析下一页链接
    spage_urls_tmp = content.xpath(r'//*[@class="NewPages"]/ul/li/a/@href')

    # 拼接链接
    spage_url_tmp = spage_urls_tmp[-2]
    if spage_url_tmp == '':
        return 'false'
    spage_url = url + spage_url_tmp
    return spage_url