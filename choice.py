print "1.Add"
print "2.Sub"
print "3.Mul"
print "4.Div"

choice=int(raw_input("Enter a choice"))

def add(x,y):
	#x=int(raw_input("Enter the first number"))
 	#y=int(raw_input("Enter the first number"))
	z = x + y
	print "The addition of ", x, "and ", y, " is ", z

def sub(x,y):
	#x=int(raw_input("Enter the first number"))
 	#y=int(raw_input("Enter the first number"))
	z = x - y
	print "The substraction of ", x, "and ", y, " is ", z

def mul(x,y):
	#x=int(raw_input("Enter the first number"))
 	#y=int(raw_input("Enter the first number"))
	z = x * y
	print "The multiplication of ", x, "and ", y, " is ", z

def div(x,y):
	#x=int(raw_input("Enter the first number"))
 	#y=int(raw_input("Enter the first number"))
	z = x / y
	print "The division of ", x, "and ", y, " is ", z	

if choice == 1:
	add(4,5)
elif choice == 2:
	sub(4,5)
elif choice == 3:
	mul(4,5)
elif choice == 4:
	div(4,5)
else:
	print "Enter a proper choice"

	
	
	

