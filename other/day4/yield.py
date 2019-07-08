#-*-encoding:utf-8-*-

import time

def consumer(name):
    print("%s，准备吃包子啦" % name)
    while True:
        baozi = yield

        print("%s，包子来了，被%s吃了" % (baozi,name) )

def producer(name):
    c = consumer("a")
    c1 = consumer("b")
    c.__next__()
    c1.__next__()
    print("开始吃包子啦")
    for i in range(10):
        time.sleep(1)
        print("制作了两个包子")
        c.send(i)
        c1.send(i)

producer("name")