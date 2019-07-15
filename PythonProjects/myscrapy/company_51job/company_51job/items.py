# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Company51JobItem(scrapy.Item):
    # 职位
    job_title = scrapy.Field()
    # 公司名称
    company_name = scrapy.Field()
    # 工作地点
    working_place = scrapy.Field()
    # 薪资
    salary = scrapy.Field()
    # 发布时间
    release_time = scrapy.Field()
    # 行政区
    district = scrapy.Field()
    # 工作经验要求
    work_exp = scrapy.Field()
    # 学历要求
    degree = scrapy.Field()
    # 招聘人数
    hiring_number = scrapy.Field()
    pass
