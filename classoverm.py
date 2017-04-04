
class Vector:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def __str__(self):
		return 'Vector (%d, %d)' % (self.a, self.b)
	def __cmp__(self,other):
		if(self.a==other.a and self.b == other.b):
			return 0
		else:
			return 1

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1
x = v1 == v2
print x

