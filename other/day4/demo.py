#-*-encoding:utf-8-*-

def get_name(name):
    flag = False
    if name == "tong":
        flag = True
        print("welcome boss")
    else:
        print(name)

def if_between(num):
    if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
        print("hello")
    else:
        print(num)

def lette():
    for ltter in "python":
        print("当前字母为",ltter)

def length():
    list = ["ting" ,"tong",'asd']
    for key in range(len(list)):
        print(list[key])

def timmer():
    import  time
    localtime = time.localtime(time.time())
    print("lacaltime :",localtime)

def time1():
    import calendar
    cal = calendar.month(2018,9)
    print(cal)



if __name__ == '__main__':
    #get_name("tong")
    #if_between(6)
    #lette()
    #length()
    #timmer()
    time1()