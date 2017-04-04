import threading
import time
class myThread (threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
	def run(self):
		print "Starting " + self.name
		time.sleep(1)
		print "Exiting " + self.name

threadLock = threading.Lock()
threads = []
	
# Create new threads
thread1 = myThread(1, "Thread-1")
thread2 = myThread(2, "Thread-2")
# Start new Threads
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
	t.join()
print "Exiting Main Thread"
