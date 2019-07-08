#-*-encoding:utf-8-*-
sum = lambda a ,b :a + b
print (sum(1,2))

# str = raw_input("please enter :")
# print "nishuru" ,str

try:
    fh = open("testfile" ,"w")
    fh.write("the is")
finally:
    print( "go in")