class Employee:
	count=0
	def __init__(self,salary):
		self.salary=salary
		Employee.count=+1
	def display(self):
		print "salary is : ",self.salary

e=Employee(20000)
e.display()
f=Employee(45000)
f.display()
