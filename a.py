num = int (raw_input("Enter number"))
def fact(a):
	if a ==1 :
		return 1
	else:
		return a * fact (a-1)

print "Factorial is ", fact (num)
