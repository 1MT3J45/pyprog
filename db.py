import MySQLdb

db = MySQLdb.connect("localhost","root","epsilon","college")

cursor = db.cursor()

cursor.execute("show tables")

data = cursor.fetchone()

print "Database version : %s " % data

db.close()

