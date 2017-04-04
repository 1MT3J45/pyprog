a=int(raw_input('Enter a number '))
b=int(raw_input('Enter a number '))
try: 
	x=a/b
	print x
	raise NameError('Hello')
except ArithmeticError as a:
	print 'Program terminated : ',a
except NameError as a:
	print 'Program terminated : ',a
finally:
	print 'Done successfully'
