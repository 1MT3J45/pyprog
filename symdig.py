num = input("Enter the number: ")
add = 0
while num > 0:
	add = add + (num%10)
	num = num / 10
else:
	print "Addition is : ", add
