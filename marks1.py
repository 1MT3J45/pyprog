data = open("marks.txt")
rows = data.readlines()
top = 0
for row in rows:
	if float(row.split()[1]) > top:
		top = float(row.split()[1])
		name = row.split()[0]
else:
	print "Topper: ", name
