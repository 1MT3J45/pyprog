import MySQLdb

db = MySQLdb.connect("localhost","root","epsilon","college")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS becomp")

sql = """CREATE TABLE becomp (
FIRST_NAME CHAR(20) NOT NULL,
AGE INT NOT NULL,
MARKS FLOAT )"""

cursor.execute(sql)


db.close()

