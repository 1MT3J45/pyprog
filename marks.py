a = input("Enter first subject: ")
b = input("Enter second subject: ")
c = input("Enter third subject: ")
d = input("Enter fourth subject: ")
e = input("Enter fifth subject: ")
m = 0
if a < 40:
	m = m + 1
if b < 40:
	m = m + 1
if c < 40:
	m = m + 1
if d < 40:
	m = m + 1
if e < 40:
	m = m + 1
if m == 5 or m == 4:
	print "FAILED"
elif m == 1 or m == 2 or m == 3:
	print "ATKT"
else:
	print "PASS"
