#-*-encoding:utf-8-*-
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
a = ["战狼2" ,"速度与激情","平凡的世界","阿童木"]

b_14 = [123,23,456,678]
b_15 = [13,22,567,1222]
b_16 = [53,53,789,1456]

x_14 = range(len(a))
x_15 = [i+ 0.2 for i in x_14]
x_16 = [i+ 0.2*2 for i in x_14]

#设置图形的大小
plt.figure(figsize=(20 ,8) ,dpi=80)

plt.bar(x_14 ,b_14 ,width = 0.2 ,label = "9月14日")
plt.bar(x_15 ,b_15 ,width = 0.2, label="9月15日")
plt.bar(x_16 ,b_16 ,width = 0.2, label="9月16日")


plt.xticks(x_15 ,a ,fontproperties = my_font)

plt.legend(loc = "best" ,prop = my_font)
plt.show()