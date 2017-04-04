import time
def countdown(n):
	if n == 0:
		print "Blast Off"
	else:
		print n
		time.sleep(2)
		countdown(n-1)

countdown(5)

