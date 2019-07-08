# # -*- coding: utf-8 -*-
killed = 100
if killed <= 100:
    print ("杀人犯")
elif killed > 100 and killed < 10000:
    print ("英雄")
else:
    print ("开国上将")

# for
list = [1, 2, 3, 4, 5]
for x in list:
    print (x)

t = (5, 6, 7, 8)
for tt in t:
    print (tt)

dict = {"key1": "tom", "key2": "tom2"}
for d in dict.keys():
    print (d)

# 99乘法表
rows = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cols = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for r in rows:
    for c in cols:
        if c == r:
            print (str(c) + "x" + str(r) + "=" + str(c * r))
        elif c < r:
            print (str(c) + "x" + str(r) + "=" + str(c * r))

# while99表
rows = 1

while (rows < 10):
    cols = 1
    while cols <= rows:
        if cols == rows:
            print (str(cols) + "x" + str(rows) + "=" + str(cols * rows))
        else:
            print (str(cols) + "x" + str(rows) + "=" + str(cols * rows) + "\t")
        cols += 1
    rows += 1