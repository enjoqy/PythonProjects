#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from scrapy.cmdline import execute


# 其中name参数为spider的name。
name = 'company_51job'
cmd = 'scrapy crawl {0} -o company_51job.csv'.format(name)
execute(cmd.split())

