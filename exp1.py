a = input("Enter the number: ")
b = input("Enter the number: ")
try:
	c = a / b
	print	"Division: ", c
except:
	print "EXCEPTION OCCURED..."
else:
	print "Else executed"
finally:
	print "Good bye\nProgram terminated"
