#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy.cmdline import execute


# 其中name参数为spider的name。 牛逼
name = 'czcfang'
cmd = 'scrapy crawl {0} -o czcfang.csv'.format(name)
execute(cmd.split())


