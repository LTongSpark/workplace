#-*-encoding:utf-8-*-

import sys

print(sys.path)

import os

os_read = os.popen("dir").read()
print(os_read)