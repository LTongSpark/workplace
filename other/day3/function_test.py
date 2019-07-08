#-*-encoding:utf-8-*-


def a():
    print("the test1")


def b():
    print("the test2")
    return 0

def c():
    print("the test3")
    return 1, 'name', [1, 2, 3], {"name": "tong"}


a = a()
b = b()
c = c()
print(a)
print(b)
print(c)