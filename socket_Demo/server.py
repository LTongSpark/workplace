#-*-encoding:utf-8-*-
import socket
import random
import json
json_datas = [
    {"base": {"client": "", "hostname": "", "ip": "106.38.97.146", "originalCMD": "", "originalLogId": "",
              "timestamp": 1528936995783, "userId": "李想(数据运营部)", "userType": "manual"}, "infotype": "LOADLOG",
     "interfaceNo": "BI_001",
     "operation": {"abnormal": "", "act": {"result": "success", "do": "login"}, "type": "LOADLOG_DOMAIN"},
     "optional": {"dataClass": "2", "databasename": "", "fieldname": "", "tablename": ""}},

    {"base": {"client": "", "hostname": "", "ip": "106.38.97.146", "originalCMD": "", "originalLogId": "",
              "timestamp": 1528945725653, "userId": "曾子玲", "userType": "manual"}, "infotype": "LOADLOG",
     "interfaceNo": "BI_001",
     "operation": {"abnormal": "", "act": {"result": "success", "do": "login"}, "type": "LOADLOG_DOMAIN"},
     "optional": {"dataClass": "2", "databasename": "", "fieldname": "", "tablename": ""}},

    {"base": {"client": "", "hostname": "", "ip": "106.38.97.146", "originalCMD": "", "originalLogId": "",
              "timestamp": 1528940182645, "userId": "谢洲勇", "userType": "manual"}, "infotype": "LOADLOG",
     "interfaceNo": "BI_001",
     "operation": {"abnormal": "", "act": {"result": "success", "do": "login"}, "type": "LOADLOG_DOMAIN"},
     "optional": {"dataClass": "2", "databasename": "", "fieldname": "", "tablename": ""}},

    {"base": {"client": "", "hostname": "", "ip": "118.26.16.188", "originalCMD": "", "originalLogId": "",
              "timestamp": 1528939676508, "userId": "孙丛丛", "userType": "manual"}, "infotype": "SENSITIVELOG",
     "interfaceNo": "BI_001",
     "operation": {"abnormal": "", "act": {"useTime": "42毫秒", "do": "select"}, "type": "SENSITIVELOG_DATA"},
     "optional": {"dataClass": "2", "databasename": "", "fieldname": "日期,DAU,有会话的用户量,浅连接,深连接,意向,普通线索",
                  "tablename": ""}},

    {"base": {"client": "", "hostname": "", "ip": "123.127.236.130", "originalCMD": "", "originalLogId": "",
              "timestamp": 1528940853700, "userId": "冯瑛", "userType": "manual"}, "infotype": "LOADLOG",
     "interfaceNo": "BI_001",
     "operation": {"abnormal": "", "act": {"result": "success", "do": "login"}, "type": "LOADLOG_DOMAIN"},
     "optional": {"dataClass": "2", "databasename": "", "fieldname": "", "tablename": ""}}
]
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostname = "192.168.1.221"
port = 8888
#绑定端口s
serverSocket.bind((hostname,port))
serverSocket.listen(5)
clientsocket,addr= serverSocket.accept()
while True:
    msg = random.sample(json_datas, 1)[0]
    clientsocket.send(json.dumps(msg).encode("utf-8"))
    import time
    time.sleep(2)
    print(msg)




