#-*-encoding:utf-8-*-
import random


def bubble_sort(li):
    for i in range(len(li) -1):
        exchange = False
        for j in range(len(li) - i -1):
            if li[j] > li[j +1]:
                li[j],li[j + 1] = li[j +1] ,li[i]
                exchange = True
        if not exchange:
            break

def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i +1 ,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i],li[min_loc] = li[min_loc] ,li[i]



data = list(range(1000000))
random.shuffle(data)
bubble_sort(data)
print(data)
