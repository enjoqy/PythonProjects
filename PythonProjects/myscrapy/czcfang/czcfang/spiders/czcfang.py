#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
这个一个基本的scrapy的spider的model，首先我们要导入Scrapy.spiders中的Spider类，
以及scrapyspider.items中我们刚刚定义好的DoubanMovieItem。

Spider
 Spider是最简单的spider。每个其他的spider必须继承自该类(包括Scrapy自带的其他spider以及您自己编写的spider)。
 Spider并没有提供什么特殊的功能。 其仅仅请求给定的 start_urls/start_requests ，
 并根据返回的结果(resulting responses)调用spider的 parse 方法。

name
 定义spider名字的字符串(string)。spider的名字定义了Scrapy如何定位(并初始化)spider，所以其必须是唯一的。
 不过您可以生成多个相同的spider实例(instance)，这没有任何限制。 name是spider最重要的属性，而且是必须的。
 如果该spider爬取单个网站(single domain)，一个常见的做法是以该网站(domain)(加或不加 后缀 )来命名spider。
 例如，如果spider爬取 mywebsite.com ，该spider通常会被命名为 mywebsite 。

allowed_domains
 可选。包含了spider允许爬取的域名(domain)列表(list)。 当 OffsiteMiddleware 启用时， 域名不在列表中的URL不会被跟进。

start_urls
 URL列表。当没有制定特定的URL时，spider将从该列表中开始进行爬取。 因此，第一个被获取到的页面的URL将是该列表之一。
 后续的URL将会从获取到的数据中提取。

start_requests()
 该方法必须返回一个可迭代对象(iterable)。该对象包含了spider用于爬取的第一个Request。
 当spider启动爬取并且未制定URL时，该方法被调用。 当指定了URL时，make_requests_from_url() 将被调用来创建Request对象。
 该方法仅仅会被Scrapy调用一次，因此您可以将其实现为生成器。
 该方法的默认实现是使用 start_urls 的url生成Request。

make_requests_from_url(url)
 该方法接受一个URL并返回用于爬取的 Request 对象。 该方法在初始化request时被 start_requests() 调用，
 也被用于转化url为request。
 默认未被复写(overridden)的情况下，该方法返回的Request对象中， parse() 作为回调函数，dont_filter参数也被设置为开启。
 (详情参见 Request).

parse(response)
 当response没有指定回调函数时，该方法是Scrapy处理下载的response的默认方法。
 parse 负责处理response并返回处理的数据以及(/或)跟进的URL。 Spider 对其他的Request的回调函数也有相同的要求。
 该方法及其他的Request回调函数必须返回一个包含 Request 及(或) Item 的可迭代的对象。

log(message[, level, component])
 使用 myscrapy.log.msg() 方法记录(log)message。 log中自动带上该spider的 name 属性。 更多数据请参见 Logging 。

closed(reason)
 当spider关闭时，该函数被调用。 该方法提供了一个替代调用signals.connect()来监听 spider_closed 信号的快捷方式。
'''

from scrapy.spiders import Spider
from czcfang.items import CzcfangItem
from scrapy import Request


class CFang(Spider):
    name = 'czcfang'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36'
    }

    # 该方法必须返回一个可迭代对象(iterable)。该对象包含了spider用于爬取的第一个Request。
    def start_requests(self):
        url = 'http://www.czcfang.com/agent/index/?agent/index/=&page=1'
        yield Request(url, headers=self.headers)

    # 当response没有指定回调函数时，该方法是Scrapy处理下载的response的默认方法。
    def parse(self, response):
        item = CzcfangItem()
        '''
        //div[@class="dw_table"]/div[@class="el"]
        '''
        houseLists = response.xpath(r'//li[@class="houseList"]')
        for houseList in houseLists:
            item['s_name'] = houseList.xpath(r'div/div/div/span[@class="topic"]/text()').extract()
            if item['s_name']:
                item['s_name'] = item['s_name'][0].strip().lstrip().rstrip(',')
            else:
                item['s_name'] = ''
            print(item['s_name'])

            item['s_phone'] = houseList.xpath(r'div/div/p[@class="saler-phone"]/text()').extract()
            if item['s_phone']:
                item['s_phone'] = item['s_phone'][0].strip().lstrip().rstrip(',')
            else:
                item['s_phone'] = ''
            print(item['s_phone'])

            item['s_department'] = houseList.xpath(r'div/div/p[@class="saler-door"]/text()').extract()
            if item['s_department']:
                item['s_department'] = item['s_department'][0].strip().lstrip().rstrip(',')
            else:
                item['s_department'] = ''
            print(item['s_department'])

            item['s_images'] =houseList.xpath(r'img/@src').extract()
            if item['s_images']:
                item['s_images'] = item['s_images'][0].strip().lstrip().rstrip(',')
            else:
                item['s_images'] = ''
            print(item['s_images'])

            yield item

        # 获取下一页的链接
        next_url = response.xpath(r'//ul[@class="paging-ul"]/a/@href').extract()
        if next_url:
            if next_url[-1]:
                next_url = 'http://www.czcfang.com/agent/index/' + next_url[-1]
                yield Request(next_url, headers=self.headers)
        else:
            return None





