n = input("Enter the number: ")
fact = 1
while n > 1:	#condition
	fact = fact * n
	n -= 1		#increment
else:
	print "Factorial is:",fact
