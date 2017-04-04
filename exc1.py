x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
try:
	a=x/y
	print a
except:	
	print "This statement is raising an exception"
else:
	print "Done successfully..."
