#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author : LTong
# Created on 2019-04-21 : 上午 10:10
# Project: demo

class ShowList(object):
    def __init__(self):
        self.L1 = []
        self.l2 = []
        self.l3 =()
        self.hello = "tong"
        self.createTuple()
        #self.createList()
        self.sub_list(self.l3)




    # def createList(self):
    #     print("创建列表：")
    #     self.L1 = list('asdddfff')
    #     print(self.L1)
    #     print(self.hello)
    def createTuple(self):
        self.l3 =(1,2,3,4,5,6)
        list = map(str, range(3, 51))


        li = filter(lambda x:x%2==0 , [x for x in range(1, 11)])
        for i in li:
            print(i)

    def sub_list(self,Tuple):
        print("1234567890")
        print(self.l3[3])

if __name__ == '__main__':
    ShowList()