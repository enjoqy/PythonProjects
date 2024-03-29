#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from concurrent.futures import ThreadPoolExecutor

from urllib import request, error
from lxml import etree
import random
import csv
import pymysql
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


'''
爬取招聘网站的工具类
'''

# 根据传入的网址进行获取网页源码，默认编码是utf-8，
def get_html(url, encoding='utf-8'):
    # 模拟请求头，防止反爬封ip
    user_agents = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
                   "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
                   "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"]
    try:
        req = request.Request(url)
        req.add_header("User-Agent", random.choice(user_agents))
        response = request.urlopen(req)
        content = response.read().decode(encoding)
        return content
    except error.URLError as e:
        # URLError
        # 产生的原因主要有：
        # 1.没有网络连接
        # 2.服务器连接失败
        # 3.找不到指定的服务
        print("URL 异常 {}".format(e.reason))
    except error.HTTPError as e:
        # HTTPError 获取响应状态码来判断响应失败的原因
        print("HTTP 异常".format(e.reason))
        return None

# 根据传入的url进行数据获取
def get_one_page(url):
    print('开启一个线程')

    # 获取招聘网站的网页源码
    content = get_html(url, 'GBK')
    # 数据清洗
    html = etree.ElementTree(etree.HTML(content))

    # 获取含有信息的数组
    els = html.xpath(r'//div[@id="resultList"]/div[@class="el"]')

    rows = []  # 用于保存每一行抓取到数据
    for el in els:
        el = etree.ElementTree(el)
        job_title = el.xpath(r'p/span/a/text()')
        # 去除尾空格
        job_title = job_title[0].strip()
        company_name = el.xpath(r'span[@class="t2"]/a/text()')  # //*[@id="resultList"]/div[4]/span[1]/a
        working_place = el.xpath(r'span[@class="t3"]/text()')
        salary = el.xpath(r'span[@class="t4"]/text()')
        release_time = el.xpath(r'span[@class="t5"]/text()')
        row = [job_title, company_name[0], working_place[0], salary[0], release_time[0]]

        # 将数据插入数据库
        # connect_DB(row)

        rows.append(row)
    #  将爬虫的数据写入到csv格式文件中
    with open('thread_51jop02.txt', mode="a+", encoding="utf-8", newline="") as f:
        # "51job.csv", mode = "a", encoding = "utf-8", newline = ""
        # 将文件的读写和csv文件进行关联
        file = csv.writer(f)
        file.writerows(rows)  # 将爬到数据一次性写入到csv格式中

    # for row in rows:
    #     print(row)
    return rows

# def connect_DB(row):
#     # 打开数据库连接
#     db = pymysql.connect("localhost", "root", "1234", "mypython")
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#     # 使用 execute()  方法执行 SQL 查询
#     # cursor.execute("select * from info")
#     # 使用 fetchone() 方法获取单条数据.
#     # data = cursor.fetchone()
#     # fetchall = cursor.fetchall()
#     sql1 = "insert into 51job_java ("\
#            "job_title, company_name, working_place, salary, release_time)"\
#            "values "\
#            "(" + row[0] + "," + row[1] + "." + row[2] + "," + row[3] + "," + row[4] + ")"
#     # 执行插入操作
#     sql = "insert into 51job_java (" \
#           "job_title, company_name, working_place, salary, release_time)" \
#           "values " \
#           "(\"" + row[0] + "\",\"" + row[1] + "\",\"" + row[2] + "\",\"" + row[3] + "\",\"" + row[4] + "\")"
#     print('数据库执行： ', sql)
#     cursor.execute(sql)
#     db.commit()
#     db.close()



# 开启线程池
def main():
    with ThreadPoolExecutor(10) as executor:
        for url in urls:
            executor.submit(get_one_page, url)


# 开启线程池进行下载
if __name__ == '__main__':
    main()
