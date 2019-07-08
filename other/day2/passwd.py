#-*-encoding:utf-8-*-

import getpass

_name = "tong"
_passwd = "tong"
user_name = input("username:")
# pass_word = getpass.getpass("passwd :")
pass_word = input("passwd :")
if user_name == _name and pass_word == _passwd:
    print("welcome {name}".format(name = user_name))
else:
    print("invalid username and passwd")

print(user_name ,pass_word)

