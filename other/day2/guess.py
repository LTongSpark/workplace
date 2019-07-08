#-*-encoding:utf-8-*-
from builtins import range, int, input

_age = 20
count = 0
while count < 3:
    age = int(input("please age :"))
    count += 1
    if age == _age :
        print("age is same")
        break
    elif age > _age :
        print("age is bigger")
    else:
        print("age is small")
    if count == 3:
        couninue_config = input("do you want to guessing...")
        if couninue_config != 'n':
            count =0
else:
    print("your have tried times ,fuck off")

for i in range(0,10 ,2):
    print(i)