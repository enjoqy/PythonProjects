#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time: 2019/5/15 001517:24
# @Author: junhi

from scrapy.cmdline import execute

# 其中name参数为spider的name。
name = 'douban_ajax'
cmd = 'scrapy crawl {0} -o douban_movie.csv'.format(name)
execute(cmd.split())
