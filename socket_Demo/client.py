#-*-encoding:utf-8-*-

import socket

s = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)

host = socket.gethostname()
port = 8888

s.connect((host ,port))
msg = s.recv(1024)
while True:
    import time
    time.sleep(2)
    print(msg.decode("unicode-escape"))