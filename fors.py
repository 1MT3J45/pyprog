n = input("Enter a number: ")
flag = 0
for i in range(2,n/2):
	if n%i == 0:
		print "NOT PRIME.. divided by",i
		break	
else:
	print "PRIME"
	
