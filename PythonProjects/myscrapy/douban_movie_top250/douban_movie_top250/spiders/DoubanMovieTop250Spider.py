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
from douban_movie_top250.items import DoubanMovieTop250Item
from scrapy import Request


class DoubanMovieTop250Spider(Spider):
    name = 'douban_movie_top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    # 该方法必须返回一个可迭代对象(iterable)。该对象包含了spider用于爬取的第一个Request。
    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    # 当response没有指定回调函数时，该方法是Scrapy处理下载的response的默认方法。
    def parse(self, response):
        item = DoubanMovieTop250Item()
        movies = response.xpath(r'//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath(r'.//div[@class="pic"]/em/text()').extract()[0]
            # TODO span[1]
            item['movie_name'] = movie.xpath(r'.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath(r'.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            # re()是正则表达式，python3.6不支持
            # item['score_num'] = movie.xpath(r'.//div[@class="star"]/span/text()').re(ur'(\d+)人评价')[0]
            item['score_num'] = movie.xpath(r'.//div[@class="star"]/span/text()').extract()[-1]
            yield item

        next_url = response.xpath(r'//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)


