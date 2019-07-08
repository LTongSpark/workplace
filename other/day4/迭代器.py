#-*-encoding:utf-8-*-

def fib(max):
    n,b,c = 0,1,1
    while(n < max):
        print(b)
        b,c = c ,b + c
        n += 1

fib(10)
print()