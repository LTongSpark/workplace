#-*-encoding:utf-8-*-

import time

def timmer():
    time.sleep(3)
    print("in the test")

timmer()

import sys
import re

p = re.compile("\\w+")
for line in sys.stdin:
    ss = line.strip().split(" ")
    for s in ss:
        if len(p.findall(s)[0]) <1:
            continue
        ss_low = p.findall(s)[0].lower()
        print (ss_low +"\t"+1)

cur_word = None
sum = 0
for line in sys.stdin:
    word,val = line.strip().split(" ")


    if cur_word == word:
        cur_word = word
    if cur_word != word:
        cur_word = None
        sum = 0
        print ("%s\t%s"%(cur_word ,sum))
    sum +=int(val)