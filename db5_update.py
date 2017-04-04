import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","root","epsilon","secomp")
# prepare a cursor object using cursor() method

cursor = db.cursor()

# Prepare SQL query to UPDATE required records
sql = "UPDATE student SET age = 20 WHERE roll = 2"
try:
	# Execute the SQL command
	cursor.execute(sql)
	# Commit your changes in the database
	db.commit()
except:
	# Rollback in case there is any error
	db.rollback()

# disconnect from server
db.close()
