import thread
import time
def worker(threadName, delay):
    i = 1
    while i < 5:
	time.sleep(1)
    	print 'This is first thread ',i
	i += 1

def builder():
    j = 1
    while j < 10:
	time.sleep(1)
    	print 'This is second thread ',j
	j += 1

thread.start_new_thread(worker,("Thread-1", 2, ))
while 1:
	pass
