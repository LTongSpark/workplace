#-*-encoding:utf-8-*-

import telnetlib
hostname= "192.168.1.221"
username = "root"
password = "123456"

tn = telnetlib.Telnet(hostname)
tn.read_until("login:")
tn.write(username + "\n")

tn.read_until("password:")
tn.write(password + "\n")

