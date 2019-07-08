#-*-encoding:utf-8-*-

def fun1():
    print("test1")
    return 0

def fun2():
    print("tes2")

a = fun1()
b = fun2()

print("the fun1 id return %s" %a)
print("the fun2 id return %s" %b)