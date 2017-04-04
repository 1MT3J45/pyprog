def worker():
	x = 10
	while True:
		print "This is worker"
		x = x - 1

def builder():
	x = 10
	while x > 0:
		print "This is builder"
		x = x - 1

worker()
builder()
		
