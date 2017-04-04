num = input("Enter the number: ")
flag = 0
for n in range(2,num/2+1):
	if num % n != 0:
		continue
	flag = 1
	break
if flag==1:
	print "NOT PRIME"
else:
	print "PRIME"

