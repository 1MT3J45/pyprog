num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

if num1 > num2:
	if num1 > num3:
 		print "%d %d is greater" %(num1, num2)
		print "{} and {}".format(num1,num2)
	else:
		print "%d is greater" %num3
else :
	if num2 > num3:
		print "%d is greater" %num2
	else:
		print "%d is greater" %num3

