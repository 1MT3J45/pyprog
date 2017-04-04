import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","epsilon","college" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

roll = input("enter roll: ")
name = raw_input("enter name: ")
marks = input("enter marks: ")
# Prepare SQL query to INSERT a record into the database.

sql = "INSERT INTO tecomp VALUES (%d, '%s', %f)" %(roll,name, marks)

try:
	# Execute the SQL command
	cursor.execute(sql)
	# Commit your changes in the database
	db.commit()
except:
	# Rollback in case there is any error
	print "Error"
	db.rollback()
	
# disconnect from server
db.close()
