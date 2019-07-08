#-*-encoding:utf-8-*-

#读写   追加的模式
file = open("hello","r+",encoding="utf-8")
'''
a+ 
rb 二进制格式读
wb 二进制写
'''
print(file.readline())
print(file.readline())
print(file.readline())
file.write("-----------------------")#在文件的末尾追加  而程序中是在第三行
#写读 模式  先创建一个文件
file = open("hello","w+",encoding="utf-8")

file.write("=========================\n")
file.write("=========================\n")
file.write("=========================\n")
file.write("=========================\n")
file.write("=========================\n")

print(file.tell())
file.seek(10)
file.write("123256548736264262646")
print(file.tell())


