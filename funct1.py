# Function definition is here
def printinfo( arg, *vartuple ):
	print "Output is: "
	print arg
	for var in vartuple:
		print var
	return;

# Now you can call printinfo function
printinfo( 10 );
printinfo( 70, 60, 50 );
