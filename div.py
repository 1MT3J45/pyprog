a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")
try:
	c = a / b
	print "Division is : ",c
except:
	print "Denominator must not be Zero"
finally:
	print "Good Bye"

