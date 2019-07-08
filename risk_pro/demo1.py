#-*-encoding:utf-8-*-
import pandas as pd

f = open("D:/PyCharm/workplace/risk_pro/风险数据.txt")
a = pd.read_table(f)
print(a)