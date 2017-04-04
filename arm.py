for n in range(100,1000):
	num = n
	r1 = n %10
	n = n / 10
	r2 = n % 10
	r3 = n / 10
	if r1**3 + r2**3 + r3**3 == num:
		print num,
