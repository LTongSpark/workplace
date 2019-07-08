# -*- coding: utf-8 -*-
import threading
import time

tickets = 100

#取票方法
#创建锁对象

lock = threading.Lock()

def getTicket():
    global lock
    lock.acquire()
    global tickets
    if tickets ==0 :
        return 0
    tmp = tickets
    tickets -= 1
    lock.release()
    return tmp


#定义售票员
class Saler(threading.Thread):
    def __init__(self ,name ,seconds):
        threading.Thread.__init__(self)
        self.name = name
        self.seconds = seconds

    def run(self):
        while True:
            tickNo = getTicket()
            if tickNo == 0 :
                return
            print(self.name + ":" + str(tickNo))

s1 = Saler("tom1" ,1)
s2 = Saler("tom2" ,1)

s1.start()
s2.start()


