# 寻找url地址栏规律拼接地址栏的页码
# 注意事项：地址栏中出现的中文关键字都是url编码，需要手动转码处理的
import crawl_tool as tool
from urllib import parse  # url的解析库(编码,解码)
import csv

kw = input("请输入关键字:")
start = int(input("请输入起始网页:"))
end = int(input("请输入结束网页:"))

#  """Encode a dict or sequence of two-element tuples into a URL query string.
# 传递参数的类型 必须是字典 或者 二元组
s = parse.urlencode({"kw": kw})
print(s)
# kw=%E5%A4%A7%E6%95%B0%E6%8D%AE
keyword = s[len("kw") + 1:]
print(keyword)

# 将多页抓取的数据 一次写入到文本中
rows = []
for page in range(start, end + 1):
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    url.format(keyword, page)
    context = tool.get_html(url, encoding='gbk')
    row = tool.crawl_one_page(context)
    rows.extend(row)

with open("51job.csv", mode='w+', encoding='utf-8') as job:
    f = csv.writer(job)
    f.writerows(rows)
