#-*-encoding:utf-8-*-

file_old = open("hello" ,"r" )
file_new = open("hello.bak" ,"w" )

for line in file_old:
    if "spark" in line:
       line =  line.replace("spark" ,"sqoop")
    file_new.write(line)
file_old.close()
file_new.close()