def add(x,y):
	c = x + y
	return c
def sub(x,y):
	c = x - y
	return c
def mul(x,y):
	c = x * y
	return c
def div(x,y):
	c = float(x) / y
	return c
while True:
	print "1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit"
	ch = input("Enter choice: ")
	a = input("Enter first number: ")
	b = input("Enter second number: ")
	
	if ch==1:
		c = add(a,b)
		print "Addition is: ", c
	elif ch==2:
		c = sub(a,b)
		print "Subtraction is: ", c
	elif ch==3:
		c = mul(a,b)
		print "Multiplication is: ", c
	elif ch==4:
		c = div(a,b)
		print "Division is: ", c
	elif ch==5:
		break
	else:
		print "Wrong choice"
