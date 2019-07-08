# -*- coding: utf-8 -*-
#gui编程
import tkinter
from tkinter  import *

#创建窗口对象的背景色
root = Tk()

#列表
list2 = Listbox(root)

list2.insert(0,'sql')
list2.insert(1,"java")
list2.insert(2,"pyrhon")
list2.insert(3,"scala")

list3 = Listbox(root)

list3.insert(0,"big data")
list3.insert(1,"jee")
list3.insert(2,"vb")

list2.pack()
list3.pack()
root.mainloop() #进入消息循环