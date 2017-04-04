import threading
import time
def worker():
    """thread worker function"""
    print threading.currentThread().getName(), 'Starting'
    while True:
	time.sleep(1)
    	print 'This is first thread'
    print threading.currentThread().getName(), 'Ending'

def builder():
    """thread worker function"""
    print threading.currentThread().getName(), 'Starting'
    while True:
	time.sleep(1)
    	print 'This is second thread'
    print threading.currentThread().getName(), 'Ending'

t = threading.Thread(name="Worker",target=worker)
t.start()

u = threading.Thread(name="Builder",target=builder)
u.start()

