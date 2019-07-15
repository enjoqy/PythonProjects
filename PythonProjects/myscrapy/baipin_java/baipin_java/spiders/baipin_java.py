#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time: 2019/5/17 001716:42
# @Author: junhi
from scrapy import Spider


class baipin_java(Spider):
    name = 'company_51job'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    # 该方法必须返回一个可迭代对象(iterable)。该对象包含了spider用于爬取的第一个Request。
    def start_requests(self):
        url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%25B9%25B3%25E9%259D%25A2,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        yield Request(url, headers=self.headers)

    # 当response没有指定回调函数时，该方法是Scrapy处理下载的response的默认方法。
    def parse(self, response):
        item = Company51JobItem()
        jobLists = response.xpath(r'//div[@class="dw_table"]/div[@class="el"]')
        for jobList in jobLists:
            item['job_title'] = jobList.xpath(r'p/span/a/@title').extract()
            if item['job_title']:
                item['job_title'] = item['job_title'][0]
            else:
                item['job_title'] = ''
            print(item['job_title'])

            item['company_name'] = jobList.xpath(r'span[@class="t2"]/a/text()').extract()
            if item['company_name']:
                item['company_name'] = item['company_name'][0]
            else:
                item['company_name'] = ''
            print(item['company_name'])

            item['working_place'] = jobList.xpath(r'span[@class="t3"]/text()').extract()
            if item['working_place']:
                item['working_place'] = item['working_place'][0]
            else:
                item['working_place'] = ''
            print(item['working_place'])

            item['salary'] = jobList.xpath(r'span[@class="t4"]/text()').extract()
            if item['salary']:
                item['salary'] = item['salary'][0]
            else:
                item['salary'] = ''
            print(item['salary'])

            item['release_time'] = jobList.xpath(r'span[@class="t5"]/text()').extract()
            if item['release_time']:
                item['release_time'] = item['release_time'][0]
            else:
                item['release_time'] = ''
            print(item['release_time'])

            # 获取详情页页的数据
            spage_url = jobList.xpath(r'p/span/a/@href').extract()[0]
            print(spage_url)
            yield Request(spage_url, meta={'item': item}, callback=self.detail_parse, headers=self.headers)

        next_url = response.xpath(r'//div[@class="p_in"]/ul/li[@class="bk"]/a/@href').extract()
        if next_url:
            next_url = next_url[-1]
            yield Request(next_url, headers=self.headers)
        else:
            return None

    # 获取详情页的数据
    def detail_parse(self, response):
        # 接收上级已爬取的数据
        item = response.meta['item']
        job_mess = response.xpath(r'//*[contains(@class,"tHeader")]/div/div/p[contains(@class,"msg")]/@title').extract()
        if not len(job_mess) == 0:
            # 这种方法可以去除网页中的&nbsp
            job_mes = "".join(job_mess[0].split())
            # 分割字符串中的‘|’
            job_mess = job_mes.split('|')
            # print(jop_reqs)

            # 调用处理字符串的方法
            job_mess = self.process_char(job_mess)
            item['district'] = job_mess[0]
            item['work_exp'] = job_mess[1]
            item['degree'] = job_mess[2]
            item['hiring_number'] = job_mess[3]
        else:
            job_mess = ''

        print(item)
        yield item

    # 对传进来的字符进行处理，返回:'工作地区', '工作经验要求','学历要求','招多少人'
    def process_char(self, strs):
        degree_tmp = ['初中及以下', '高中', '中技', '中专', '大专', '本科', '硕士', '博士']
        work_exp = degree = hiring_number = ''
        for str1 in strs:
            # 工作经验要求
            if '验' in str1:
                work_exp = str1
            # 学历要求
            elif ''.join(degree_tmp).find(str1) >= 0:
                degree = str1
            # 招多少人
            elif '人' in str1:
                hiring_number = str1
        rows = [strs[0], work_exp, degree, hiring_number]

        return rows
