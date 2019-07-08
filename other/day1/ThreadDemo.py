#-*-encoding:utf-8-*-
import threading
def add(a,b):
    print(a +b)

try:
    t = threading.Thread(target=add ,args=(1,2))
    print(threading.current_thread().name)
    t.start()
except Exception:
    print(1)
