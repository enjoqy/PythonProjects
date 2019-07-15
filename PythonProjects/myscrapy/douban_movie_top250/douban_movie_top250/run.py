#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from scrapy.cmdline import execute

# 其中name参数为spider的name。
name = 'douban_movie_top250'
cmd = 'scrapy crawl {0} -o douban01.csv'.format(name)
execute(cmd.split())
