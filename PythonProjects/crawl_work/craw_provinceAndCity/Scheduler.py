#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time: 2019/5/18 001812:52
# @Author: junhi

import Spiders
import downloading
from multiprocessing import Pool


# 目标列表
aimurl = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/"
aimurllist = ["11", "12", "13", "14", "15", "21", "22", "23", "31", "32", "33", "34", "35", "36", "37",
              "41", "42", "43", "44", "45", "46", "50", "51", "52", "53", "54", "61", "62", "63", "64", "65"]


def run_proc(url, num):
    print(num + ' is running')
    (city, county, town, village) = Spiders.spider(url, num)
    downloading.download(city, county, town, village, num)
    print(num + ' ended')


if __name__ == "__main__":
    p = Pool(8)
    for i in aimurllist:
        p.apply_async(run_proc, args=(aimurl, i))
    print('Waiting for all subprocesses done ...')
    p.close()  # 关闭进程池
    p.join()  # 等待开辟的所有进程执行完后，主进程才继续往下执行
    print('All subprocesses done')
