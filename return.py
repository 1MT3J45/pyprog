import math
def log(x):
	if x <= 0 :
		print "Enter a positive number"
		return

	result = math.log(x)
	print "The log of ", x, "is ", result
log(0)
	
