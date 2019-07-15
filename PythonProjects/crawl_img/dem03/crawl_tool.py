import random
from urllib import request, error
from lxml import etree
import csv


def get_html(url, encoding='utf-8'):
    '''
    获取网页数据
    :param url:
    :param encoding: 编码格式
    :return:
    '''
    # 1.构建一个User-agent列表 随机从列表中选择一个User-agent来模拟浏览器
    user_agents = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
                   "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
                   "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"]

    try:
        # 生成请求对象
        req = request.Request(url)
        req.add_header("User-Agent", random.choice(user_agents))

        # 发送请求 并接受响应对象
        response = request.urlopen(req)
        # 读取数据
        context = response.read().decode(encoding)
        return context
    except error.URLError as e:
        # URLError
        # 产生的原因主要有：
        # 1.没有网络连接
        # 2.服务器连接失败
        # 3.找不到指定的服务
        print("URL 异常 {}".format(e.reason))
    except error.HTTPError as e:
        # HTTPError 获取响应状态码来判断响应失败的原因
        print("HTTP 异常".format(e.reason))
    return None


def crawl_one_page(context):
    """
    获取一个网页中以及子网页数据
    :param text:
    :return:
    """
    # 2 数据清洗  转换成元素树
    html = etree.ElementTree(etree.HTML(context))

    # 3.使用xpath语法对数据进行清洗
    els = html.xpath(r'//div[@id="resultList"]/div[@class="el"]')
    print(els)

    # 4.遍历每一行的数据
    rows = []  # 用于保存每一行抓取到数据
    g_i = 0
    for el in els:
        g_i += 1
        print("正在获取第{}条数据.".format(g_i))
        el = etree.ElementTree(el)
        position = el.xpath(r'p/span/a/@title')  # 获取职位信息
        # if position:
        #     position = position[0]
        # else:
        #     None
        position = position[0] if position else None
        company = el.xpath(r'span[@class="t2"]/a/text()')
        company = company[0] if company else None
        area = el.xpath(r'span[@class="t3"]/text()')
        area = area[0] if area else None
        money = el.xpath(r'span[@class="t4"]/text()')
        money = money[0] if money else None
        time = el.xpath(r'span[@class="t5"]/text()')
        time = time[0] if time else None
        # row = (position, company, area, money, time)
        # rows.append(row)
        # 5.获取子网页 抓取 福利待遇,招聘简单要求
        # 5.1 获取子网页的url
        child_url = el.xpath('/div/p/span/a/@href')
        child_url = child_url[0] if child_url else  None
        # 5.2进入到子网页  抓取子网页数据
        child_context = get_html(child_url,encoding='gbk')
        child_html = etree.ElementTree(etree.HTML(child_context))
        others = child_html.xpath('//div[@class="tHeader tHjob"]/div/div[@class="cn"]/p[@class="msg ltype"]/@title')
        others = others[0].replace("  |  ", ",") if others else None
        fuli = child_html.xpath('//div[@class="tHeader tHjob"]/div/div[@class="cn"]/div/div/span/text()')
        fuli = ",".join(fuli) if fuli else None
        # print("other:{}, fuli:{}".format(others, fuli))
        row = (position, company, area, money, time, others, fuli)
        rows.append(row)
    # 在重复执行处添加随机时间延迟

    return rows


# 抓取一页数据,以追加形式写入到51job.csv
def write_on_page(url):
    context = get_html(url, encoding="gbk")
    rows = crawl_one_page(context)
    with open("51job.csv", mode="a", encoding="utf-8", newline="") as job:
        f = csv.writer(job)
        f.writerows(rows)
