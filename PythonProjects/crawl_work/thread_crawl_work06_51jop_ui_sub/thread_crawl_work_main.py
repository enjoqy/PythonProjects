#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
from crawl_work.thread_crawl_work06_51jop_ui_sub import thread_crawl_work_tools
from crawl_work.thread_crawl_work06_51jop_ui_sub import nationwide_make_urls
from lxml import etree

'''
爬取招聘网站的主方法
'''

# 获取全国的java岗位链接
nationwide_java_urls = nationwide_make_urls.get_nationwide_urls()

for province_name in nationwide_java_urls:
    # 每个省的url
    province_url = nationwide_java_urls[province_name]

    # 获取每个省共有多少页
    html = thread_crawl_work_tools.get_html(province_url)
    content = etree.ElementTree(etree.HTML(html))
    page_numbers = content.xpath(r'//*[@class="p_in"]/span[@class="td"]/text()')
    if not len(page_numbers) == 0:
        # 对获取的页码数字符串进行处理
        page_number = page_numbers[0].split('页')[0][1:]
    else:
        page_number = 1

    # 获取每个省有多少子页链接
    i = 1
    urls = []
    while i <= int(page_number):
        print(page_number)
        province_url_final = province_url[0: 90] + str(i) + province_url[91:]
        print(province_url_final)
        urls.append(province_url_final)
        i = int(i)
        i += 1

    # 开启线程
    # 池
    def main():
        with ThreadPoolExecutor(10) as executor:
            for url in urls:
                executor.submit(thread_crawl_work_tools.get_one_page, url, province_name)


    # 开启线程池进行下载
    if __name__ == '__main__':
        main()
