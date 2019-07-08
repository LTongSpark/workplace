#-*-encoding:utf-8-*-

import urllib.request

#创建url字符串
url = "https://www.baidu.com"
#打开链接  返回相应的对象

# def print_rv(rv):
#     for item in rv:
#         print(item)


resp = urllib.request.urlopen(url)
print(resp.read())
