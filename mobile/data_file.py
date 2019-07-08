#-*-encoding:utf-8-*-
import pandas as pd

work_book = pd.read_excel("D:/google/19年研判处置关停号码库0216.xlsx", sheetname=0)
word = work_book["号码"]
lines_seen = []
data = pd.read_csv("C:/Users/Administrator/Desktop/1.txt",header=None)
# print(data)

for i in word:
    for j in data[1]:
        if(i== j):
            print(i)
