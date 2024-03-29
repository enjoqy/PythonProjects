# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


'''
Item 对象是种简单的容器，保存了爬取到得数据
'''


class DoubanMovieTop250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 排名
    ranking = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评论人数
    score_num = scrapy.Field()
    pass
