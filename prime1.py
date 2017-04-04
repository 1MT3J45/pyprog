for num in range(3,51):
	for n in range(2,num/2+1):
		if num % n == 0:
			break
	else:
		print num

