#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from urllib import request, error
from lxml import etree
import random
import csv
import pymysql

'''
爬取招聘网站的工具类
'''


# 根据传入的网址进行获取网页源码，默认编码是utf-8，
def get_html(url, encoding='gbk'):
    print(url)
    # 模拟请求头，防止反爬封ip
    user_agents = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"
    ]
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
        print("HTTP 异常{}".format(e.reason))
        return None
    except BaseException as e:
        print('有异常{}'.format(e.reason))


# 根据传入的url进行数据获取
def get_one_page(url, province_name):
    # print(url)
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
        # 职位
        job_title = el.xpath(r'p/span/a/@title')
        if not len(job_title) == 0 and not job_title[0] == '':
            job_title = job_title[0]
        else:
            job_title = ''
        # 公司名称
        company_name = el.xpath(r'span[@class="t2"]/a/text()')  # //*[@id="resultList"]/div[4]/span[1]/a
        if not len(company_name) == 0 and not company_name[0] == '':
            company_name = company_name[0]
        else:
            company_name = ''
        # 工作地点
        working_place = el.xpath(r'span[@class="t3"]/text()')
        if not len(working_place) == 0 and not working_place[0] == '':
            working_place = working_place[0]
        else:
            working_place = ''
        # 薪资
        salary = el.xpath(r'span[@class="t4"]/text()')
        if not len(salary) == 0 and not salary[0] == '':
            salary = salary[0]
        else:
            salary = ''
        # 发布时间
        release_time = el.xpath(r'span[@class="t5"]/text()')
        if not len(release_time) == 0 and not release_time[0] == '':
            release_time = release_time[0]
        else:
            release_time = ''
        # 获取子页的数据
        spage_urls = el.xpath(r'p/span/a/@href')
        # 获取招聘网站的网页源码,清洗，获取指定数据
        spage_html = get_html(spage_urls[0], 'gbk')
        spage_content = etree.ElementTree(etree.HTML(spage_html))
        jop_req = spage_content.xpath(r'//*[contains(@class,"tHeader")]/div/div/p[contains(@class,"msg")]/@title')
        if not len(jop_req) == 0:
            # 这种方法可以去除网页中的&nbsp
            jop_req = "".join(jop_req[0].split())
            # 分割字符串中的‘|’
            jop_reqs = jop_req.split('|')
            # print(jop_reqs)

            # 调用处理字符串的方法
            jop_reqs = process_char(jop_reqs)
        else:
            jop_reqs = ''
        row = [job_title, company_name, province_name, salary, release_time]
        row = row + jop_reqs
        print(row)

        # 将数据插入数据库
        # connect_DB(row, province_name)

        rows.append(row)

    # 将爬虫的数据追加写入到csv格式文件中
    write(rows)

    return rows


# 对传进来的字符进行处理，返回:'工作地区', '工作经验要求','学历要求','招多少人'
def process_char(strs):
    degree_tmp = ['初中及以下', '高中', '中技', '中专', '大专', '本科', '硕士', '博士']
    work_exp = degree = hiring_number = ''
    for str1 in strs:
        # 工作经验要求
        if '验' in str1:
            work_exp = str1
        # 学历要求
        elif ''.join(degree_tmp).find(str1) >= 0:
            degree = str1
        # 招多少人
        elif '人' in str1:
            hiring_number = str1
    rows = [strs[0], work_exp, degree, hiring_number]
    return rows


#  将爬虫的数据写入到csv格式文件中
def write(rows):
    with open('H://province_jobs/' + '全国.txt', mode="a+", encoding="utf-8", newline="") as f:
        # "51job.csv", mode = "a", encoding = "utf-8", newline = ""
        # 将文件的读写和csv文件进行关联
        file = csv.writer(f)
        file.writerows(rows)  # 将爬到数据一次性写入到csv格式中
        # f.flush()
        # f.close()


def connect_DB(row, province_name):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "1234", "mypython")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    # cursor.execute("select * from info")
    # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()
    # fetchall = cursor.fetchall()
    # sql1 = "insert into 51job_java (" \
    #        "job_title, company_name, working_place, salary, release_time)" \
    #        "values " \
    #        "(" + row[0] + "," + row[1] + "." + row[2] + "," + row[3] + "," + row[4] + ")"
    # 执行插入操作
    sql = "INSERT INTO china_job (province, job_title, company_name, working_place, salary, release_time, district, work_exp, degree, hiring_number) " \
          " VALUES " \
          "(\"" + province_name + "\",\"" + row[0] + "\",\"" + row[1] + "\",\"" + row[2] + "\",\"" + row[3] + "\",\"" + \
          row[4] + "\",\"" + row[5] + "\",\"" + row[6] + "\",\"" + row[7] + "\",\"" + row[8] + "\");"
    print('数据库执行： ', sql)
    cursor.execute(sql)
    db.commit()
    db.close()
