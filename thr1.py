import threading
import time
def worker():
    """thread worker function"""
    while True:
	time.sleep(1)
    	print 'This is first thread'

def builder():
    """thread worker function"""
    while True:
	time.sleep(1)
    	print 'This is second thread'

t = threading.Thread(target=worker)
t.start()

u = threading.Thread(target=builder)
u.start()
