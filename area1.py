class Over:
	def area(self,a):
		return a*a
class Calculate(Over):
	def area(self,a):
		return 3.14*a*a

c = Calculate()
o = Over()
print "Square: ",o.area(21)
print "Circle: ",c.area(12)
