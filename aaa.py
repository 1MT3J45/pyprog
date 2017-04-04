for n in range(101,999):
	a=n%10
	b=n/10
	c=b%10
	b=b/10

	if(a*a*a)+(b*b*b)+(c*c*c)==n:
		print n
	
