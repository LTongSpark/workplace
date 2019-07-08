#-*-encoding:utf-8-*-
import time
import random

def cal_time(func):
    def wrapper(*args ,**kwargs):
        t1 = time.time()
        x = func(*args ,**kwargs)
        t2 = time.time()
        print("time is" ,t1 - t2)
        return x
    return wrapper

@cal_time
def bin_search(data_set ,val ):
    low = 0
    high = len(data_set) - 1
    while low <= high :
        mid = (low + high) //2
        if data_set[mid] == val:
            return mid
        elif data_set[mid] > val:
            high = mid -1
        else:
            low = mid + 1
    return

data = list(range(100000000))

bin_search(data ,152)