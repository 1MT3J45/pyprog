data = open("num.txt")
lines = data.readlines()
max1 = 0
for line in lines:
	s = line.split()
	max2 = 0
	for num in s:	
		if int(num) > max2: 
			max2 = int(num)
	if max2 > max1:
		max1 = max2

print "Maximum: ", max1
