import sys
import io
from urllib import request

class Data():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    def __init__(self):

        #浏览器登录后得到的cookie，也就是刚才复制的字符串
        # self.cookie_str = r'_ga=GA1.2.497555532.1608957411; _gid=GA1.2.648427415.1608957411; session=53616c7465645f5fec6238fdbf7a245cd4cc6ecfc3c8e7cbf293b6acc0ab9320cb23950d9c67b8346f3812daa8a7b417'

        self.cookie_str = r'_ga=GA1.2.1554389293.1608999262; _gid=GA1.2.1427853896.1608999262; session=53616c7465645f5f258916b5b441253429378a9e392e8c2f91aa62c78de95652bb020562275547bc9de234f111e56f0a'




    def getData(self, url = r'https://adventofcode.com/2020/day/2/input'):
        # 登录后才能访问的网站
        req = request.Request(url)
        # 设置cookie
        req.add_header('cookie', self.cookie_str)
        # 设置请求头
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
        resp = request.urlopen(req)
        return(resp.read().decode('utf-8'))