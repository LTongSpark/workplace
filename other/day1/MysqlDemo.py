# -*- coding: utf-8 -*-
import pymysql
# 得到数据库对象,不能用localhost,需要使用127.0.0.1
db = pymysql.connect("127.0.0.1", "root", "tong0614")

# 得到游标
cur = db.cursor()

# 测试
cur.execute("select version()")

# 提取一个结果
data = cur.fetchone()
print (data)

# 建库
cur.execute("drop database python")
cur.execute("create database python")
cur.execute("create table python.t1(id int primary key , name varchar(20) , age int)")
cur.execute("insert into python.t1 values(1,'tom1',12)")
cur.execute("insert into python.t1 values(2,'tom2',13)")
cur.execute("insert into python.t1 values(3,'tom3',14)")

cur.execute("select * from python.t1")
rows = cur.fetchall()
# row是tuple，使用t[0]访问组元。
for row in rows:
    print (str(row[0]) + " :" + row[1] + " : " + str(row[2]))

# 数据库提交
db.commit()
# 关闭数据库
db.close()
