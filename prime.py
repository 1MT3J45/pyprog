def isPrime(n):
	for i in range(2,n/2):
		if n%i==0:
			return False
	else:
		return True

def max1(a,b):
	if a > b:
		return a
	else:
		return b

def min1(a,b):
	if a < b:
		return a
	else:
		return b
