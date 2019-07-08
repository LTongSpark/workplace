#-*-encoding:utf-8-*-
from matplotlib import pyplot  as plt
import matplotlib
import random

#
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}
#
# matplotlib.rc("font" , **font)

my_font = matplotlib.font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")

x = range(1,120)
y = [random.randint(20,35) for i in range(1,120)]
plt.figure(figsize=(20,8) ,dpi=80)
plt.plot(x,y)
plt.xlabel("时间" ,fontproperties = my_font)
plt.ylabel("温度", fontproperties=my_font)
_xlick =["10点{}分".format(i) for i in range(60)]
_xlick +=["11点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::3] ,_xlick[::3],rotation = 90 ,fontproperties = my_font)#旋转90度
plt.show()