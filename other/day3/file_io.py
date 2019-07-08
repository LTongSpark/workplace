#-*-encoding:utf-8-*-

file = open("hello","a",encoding="utf-8")
#打印当前的位置
print(file.tell())
print(file.readline())
print(file.tell())

#回到起点
file.seek(0)
# data  = file.read()
# print(data)

file.write("\nhello hbase")
file.close()

for i in range(5):
    print(file.readline())
count = 0
for line in file:
    if count ==9:
        print("================")
        continue
        count += 1
    print(line)
    count += 1



for index ,line in enumerate(file.readline()):
    if index == 9:
        print("----------------------")
        continue
    print(line.strip())
