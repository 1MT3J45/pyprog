data = open("nested.py")
c = 0
for line in data:
	c = c + line.split().count("print")
else:
	print "Count:",c

