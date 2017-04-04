def fact(num):
	if num == 1:
		return 1
	else:	
		return (num * fact(num-1))

a = input("Enter the number: ")
print fact(a)
