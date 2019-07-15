from demo01 import crawl_tool as tool
from lxml import etree
import csv

# 1 数据抓取
url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
context = tool.get_html(url, encoding='gbk')

# 2 数据清洗  转换成元素树
html = etree.ElementTree(etree.HTML(context))

# 3.使用xpath语法对数据进行清洗
els = html.xpath(r'//div[@id="resultList"]/div[@class="el"]')

# 4.遍历每一行的数据
# rows = []  # 用于保存每一行抓取到数据
# for el in els:
#     el = etree.ElementTree(el)
#     position = el.xpath(r'p/span/a/@title')  # 获取职位信息
#     # if position:
#     #     position = position[0]
#     # else:
#     #     None
#     position = position[0] if position else None
#     company = el.xpath(r'span[@class="t2"]/a/text()')
#     company = company[0] if company else None
#     area = el.xpath(r'span[@class="t3"]/text()')
#     area = area[0] if area else None
#     money = el.xpath(r'span[@class="t4"]/text()')
#     money = money[0] if money else None
#     time = el.xpath(r'span[@class="t5"]/text()')
#     time = time[0] if time else None
#     # row = (position, company, area, money, time)
#     # rows.append(row)
#     # 5.获取子网页 抓取 福利待遇,招聘简单要求
#     # 5.1 获取子网页的url
#     child_url = el.xpath('/div/p/span/a/@href')
#     child_url = child_url[0] if child_url else  None
#     # 5.2进入到子网页  抓取子网页数据
#     child_context = tool.get_html(child_url, encoding='gbk')
#     child_html = etree.ElementTree(etree.HTML(child_context))
#     others = child_html.xpath('//div[@class="tHeader tHjob"]/div/div[@class="cn"]/p[@class="msg ltype"]/@title')
#     others = others[0].replace("  |  ", ",") if others else None
#     fuli = child_html.xpath('//div[@class="tHeader tHjob"]/div/div[@class="cn"]/div/div/span/text()')
#     fuli = ",".join(fuli) if fuli else None
#     print("other:{}, fuli:{}".format(others, fuli) )


url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
context = tool.get_html(url, encoding='gbk')
rows = tool.crawl_one_page(context)

print(rows)

#  将爬虫的数据写入到csv格式文件中
# with open("51job.csv", mode="w+", encoding="utf-8") as f:
#     # 将文件的读写和csv文件进行关联
#     file = csv.writer(f)
#     file.writerows(rows)  # 将爬到数据一次性写入到csv格式中
