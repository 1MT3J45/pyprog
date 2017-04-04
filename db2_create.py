import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","epsilon","secomp" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS COLLEGE")

# Create table as per requirement
sql = """CREATE TABLE COLLEGE (
FIRST_NAME CHAR(20) NOT NULL PRIMARY KEY,
LAST_NAME CHAR(20),
AGE INT,
GENDER CHAR(1),
INCOME FLOAT )"""
cursor.execute(sql)

# disconnect from server
db.close()
