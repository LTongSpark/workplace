#-*-encoding:utf-8-*-
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
x = range(11,31)
y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3 ,3,1,1,1]
y_2 = [1,0,2,1,4,4,3,2,3,4,4,4,8,5,1,3 ,3,1,1,1]

#设置图形的大小
plt.figure(figsize=(20,8) ,dpi=80)

plt.xlabel("年龄" ,fontproperties = my_font)
plt.ylabel("交了多少女朋友" ,fontproperties = my_font)

plt.grid(alpha = 0.4)
_xticks = ["{}岁".format(i) for i in x]
plt.xticks(x, _xticks ,fontproperties = my_font)
#绘制图形
plt.plot(x,y_1,label = "自己")
plt.plot(x,y_2 ,label= "别人")
plt.legend(prop = my_font,loc = 5)

plt.show()