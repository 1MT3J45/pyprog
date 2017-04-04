class Ball:
	count = 0
	def __init__ (self,x,y):
		self.x = x
		self.y = y
	def show(self):
		print "Object %d created" %Ball.count
class Game(Ball):
	def __init__(self,a,b):
		super(Game,self).__init__()
		Ball.count = Ball.count + 1
	def display(self):
		z = self.x * self.y
		print "Multiplication : ", z
	def __del__(self):
		class_name = self.__class__.__name__
		print class_name, "destroyed"

	
b = Game(34,88)
b.show()
b.display()

del b
c = Game(23,11)
c.show()
c.display()
