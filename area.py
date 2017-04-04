class Area:
	def __init__(self):
		self.r = 0
		self.s = 0
	def display(self):
		a = 3.14 * self.r * self.r
		return a
class New(Area):
	def __init__(self,r,s):
		self.r = r
		self.s = s
	def show(self):
		s = self.display()
		print "Circle area: ",s
		a = self.s * self.s
		return a
n = New(12,15) 
print "Square area: ", n.show()
