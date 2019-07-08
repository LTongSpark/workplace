import requests
from selenium import webdriver
import urllib.request
import requests
import re

from bs4 import BeautifulSoup


#reponse = requests.get("www.baidu.com")

# response = requests.get("http://d.hiphotos.baidu.com/image/h%3D300/sign=3aca62b68c8ba61ec0eece2f713597cc/0e2442a7d933c8955abcfc07df1373f08302008f.jpg")
# print(response.content)
# print(response.status_code)
#
# with open("D:\\tong.gif" ,"wb") as fs:
#     fs.write(response.content)
#     fs.close()


driver = webdriver.Chrome()
driver.get("https://www.taobao.com")

reponse = urllib.request.urlopen("")


# re = requests.get("http://www.baidu.com")
# for key,values in re.cookies.items():
#     print(key + "," + values)

# s = requests.session()
# s.get("http://httpbin.org/cookies/set/number/123456789")
# re1 = s.get("http://httpbin.org/cookies")
# print(re1.text)

# response = requests.get("https://www.12306.cn")
# print(response.status_code)
#
# content = requests.get("https://book.douban.com").text
# print(content)

