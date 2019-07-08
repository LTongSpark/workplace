#-*-encoding:utf-8-*-
import time

def timmer(func):
    def doec(*args ,**kwargs):
        start_time = time.time()
        func(*args ,**kwargs)
        end_time = time.time()
        print("this is 耗时 %s" %(end_time-start_time))
    return doec

@timmer
def test1():
    time.sleep(3)
    print("this is test1")
@timmer
def test2(name ,age):
    print("this is test2",name ,age)

test1()
test2("liutong" ,26)
