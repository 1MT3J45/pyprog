n = 2
num = input("Enter the number: ")
while n < num/2 and (num!=2 and num!=3 ):
	if num % n == 0:
		print "NOT Prime\n"
		break
	n = n + 1
else:
	print "Prime\n"
	
