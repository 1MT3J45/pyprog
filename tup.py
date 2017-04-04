stud = []
stud.append((1,"ajay",58.90))
stud.append((2,"vijay",48.12))
stud.append((3,"amar",78.34))
stud.append((4,"asha",65.22))
marks = 0
for x in stud:
	marks = marks + x[2]
else:
	print "Average: ", float(marks)/4
