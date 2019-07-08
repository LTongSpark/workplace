# -*- coding: utf-8 -*-
import os


#r = input("请输入计算表达式：")
#print r

#读取文件
r = open("d:/mr/stu.txt")
lines = r.readlines()
for line in lines:
    print(line),

f= open("d:/mr/stu.txt",mode="a+")
f.write("hello world")
f.close()



# os.renames("d:/mr/wc" ,"d:/mr/wc1")
# os.rename("d:/mr/stus.txt", "d:/mr/stu.txt")