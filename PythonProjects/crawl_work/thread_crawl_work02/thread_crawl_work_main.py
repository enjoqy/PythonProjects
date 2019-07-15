#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
from crawl_work.thread_crawl_work02 import thread_crawl_work_tools

'''
爬取招聘网站的主方法
'''

url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

i = 0
urls = []
while(i < 1706):
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,' + str(i) + '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    urls.append(url)
    i = int(i)
    i += 1

# rows = thread_crawl_work_tools.get_one_page(url)
# for row in rows:
#     print(row)

# 开启线程池
def main():
    with ThreadPoolExecutor(10) as executor:
        for url in urls:
            executor.submit(thread_crawl_work_tools.get_one_page, url)


# 开启线程池进行下载
if __name__ == '__main__':
    main()
