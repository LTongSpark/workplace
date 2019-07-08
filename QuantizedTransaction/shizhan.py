# -*- coding:utf-8 -*-
import requests
import re

content1 = requests.get('https://book.douban.com/').text

#print(content1)

content = """
 
"""
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?</li>', re.S)
# pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?author"(.*?).*?</li>' ,re.S)
# pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?</li>', re.S)
result = re.findall(pattern,content)

for href ,title ,author in result:
    print(href+ "\t\t\t"+title +"\t\t\t" +author.strip())

print("jieshu")

# print(result)