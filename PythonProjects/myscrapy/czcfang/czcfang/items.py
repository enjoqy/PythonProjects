# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CzcfangItem(scrapy.Item):
    # 姓名
    s_name = scrapy.Field()
    # 手机
    s_phone = scrapy.Field()
    # 所属部门
    s_department = scrapy.Field()
    # 头像
    s_images = scrapy.Field()
    pass
