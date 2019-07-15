# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


# scrapy的pipeline是一个非常重要的模块，主要作用是将return的items写入到数据库、文件等持久化模块
class Company51JobPipeline(object):

    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host='localhost', user='root', password="1234", db='mypython', port=3306)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 往数据库里面写入数据
        # sql = "INSERT INTO company_51job (job_title, company_name, working_place, salary, release_time, district, work_exp, degree, hiring_number) " \
        #       " VALUES " \
        #       "(\"" + {} + "\",\"" + {} + "\",\"" + {} + "\",\"" + {} + "\",\"" + {} + "\",\"" + \
        #       {} + "\",\"" + {} + "\",\"" + {} + "\",\"" + {} + "\");"
        sql = "INSERT INTO company_51job (job_title, company_name, working_place, salary, release_time, district, work_exp, degree, hiring_number) " \
              " VALUES " \
              "(\"" + item['job_title'] + "\",\"" + item['company_name'] + "\",\"" + item['working_place'] + "\",\"" + item['salary'] + "\",\"" + item['release_time'] + "\",\"" + \
              item['district'] + "\",\"" + item['work_exp'] + "\",\"" + item['degree'] + "\",\"" + item['hiring_number'] + "\");"
        #
        # self.cursor.execute(sql.format(item['job_title'], item['company_name'], item['working_place'], item['salary'],
        #                                item['release_time'], item['district'], item['work_exp'], item['degree'], item['hiring_number']))
        self.cursor.execute(sql)
        self.connect.commit()
        return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
