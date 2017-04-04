t = []
for x in range(0,3):
	roll = input("Enter roll number: ")
	name = raw_input("Enter name: ")
	marks = input("Enter marks: ")
	t.append((roll, name, marks))
t1 = []
for x in t:
	t1.append((x[0], x[1], x[2]+0.26))

t = t1
