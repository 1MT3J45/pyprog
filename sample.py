def Worker():
	i = 0
	while i < 10:
		print "This is worker"
		i = i + 1

def Builder():
	i = 0
	while i < 10:
		print "This is builder"
		i = i + 1 

Worker()
Builder()
while True:
	pass
	
