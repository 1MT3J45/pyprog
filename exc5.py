class NegOutputException(Exception):
	def __init__(self, data):
		self.data = data
	def __str__(self):
		return repr(self.data)

try:
	x = input("Enter first Number: ")
	y = input("Enter first Number: ")
	z = x - y
	if z < 0:
		raise NegOutputException(z)
except NegOutputException as ae:
	print "Exception:Negative-output", ae.data
else:
	print "Result: ", z
