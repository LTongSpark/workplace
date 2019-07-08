# -*- coding: utf-8 -*-

import threading
def add(a,b):
    print (a + b)

try:
    threading.start_new_thread(add ,(1,2))
except Exception:
    print (1)