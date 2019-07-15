#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
import time

# 开启线程池
# map可以保证输出的顺序, submit输出的顺序是乱的
# 如果你要提交的任务的函数是一样的，就可以简化成map。
# submit和map的参数是不同的，submit每次都需要提交一个目标函数和对应的参数，map只需要提交一次目标函数，
#   目标函数的参数放在一个迭代器（列表，字典）里就可以。

def sayhello(a):
    print("hello: " + a)
    time.sleep(0.2)

def main():
    seeds = ['a', 'b', 'c']

    # 没有用多线程的打印时间
    starttime1 = time.time()
    for seed in seeds:
        sayhello(seed)
    endtime1 = time.time()
    print("time1: " + str(endtime1 - starttime1))

    # 使用线程池的打印（调用sayhello方法会休眠2秒，线程池会在很短时间打印完成）
    # 使用线程池的第一种方法
    starttime2 = time.time()
    with ThreadPoolExecutor(3) as executor:
        for seed in seeds:
            executor.submit(sayhello, seed)
    endtime2 = time.time()
    print("time2: " + str(endtime2 - starttime2))

    # 使用线程池的第二种方法
    starttime3 = time.time()
    with ThreadPoolExecutor(3) as executor1:
        executor1.map(sayhello, seeds)
    endtime3 = time.time()
    print("time3: " + str(endtime3 - starttime3))

if __name__ == '__main__':
    main()


