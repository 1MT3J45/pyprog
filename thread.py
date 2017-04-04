import time
import threading
def worker():
	a=1
	while True:
		#time.sleep(1)
		print '\n Worker ',a
		a+=1
def builder():
	b=10
	while True:
		#time.sleep(1)
		print '\n Builder ',b
		b-=1
w=threading.Thread(target=worker)
w.start()
b=threading.Thread(target=builder)
b.start()
