import MySQLdb

# create database college;
# use college;
# create table becomp (roll int, name char(20), surname char(20), gender char(1), marks float);

def view_all():
	db = MySQLdb.connect("localhost","root","epsilon","college" )
	cursor = db.cursor()

	sql = "select * from becomp"

	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		print "ROLL FIRT_NAME LAST_NAME GENDER MARKS"
		for row in results:
			roll = row[0]
			name = row[1]
			last = row[2]
			gender = row[3]
			marks = row[4]
			print "%3d %8s %8s %6s %8.2f" %(roll, name, last, gender, marks)

	except:
		print "Error: unable to fetch data"

	db.close()
	view()
	return

def view_gender():

	db = MySQLdb.connect("localhost","root","epsilon","college" )
	cursor = db.cursor()

	sql = "select * from becomp WHERE gender = 'F'"
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		print "\t**** FEMALE NAMES ****"
		print "ROLL FIRT_NAME LAST_NAME GENDER MARKS"
		for row in results:
			roll = row[0]
			name = row[1]
			last = row[2]
			gender = row[3]
			marks = row[4]
			print "%3d %8s %8s %6s %8.2f" %(roll, name, last, gender, marks)
	except:
		print "Error: unable to fetch data"

	print "\n---------------------------------------\n"

	sql = "select * from becomp WHERE gender = 'M'"
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		print "\t**** MALE NAMES ****"
		print "ROLL FIRT_NAME LAST_NAME GENDER MARKS"
		for row in results:
			roll = row[0]
			name = row[1]
			last = row[2]
			gender = row[3]
			marks = row[4]
			print "%3d %8s %8s %6s %8.2f" %(roll, name, last, gender, marks)
	except:
		print "Error: unable to fetch data"

	db.close()
	view()
	return

def view_marks_lt():
	db = MySQLdb.connect("localhost","root","epsilon","college" )
	cursor = db.cursor()

	m = float(raw_input("Enter marks: "))
	sql = "select * from becomp where marks < %f" %m

	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		print "\nROLL FIRT_NAME LAST_NAME GENDER MARKS"
		for row in results:
			roll = row[0]
			name = row[1]
			last = row[2]
			gender = row[3]
			marks = row[4]
			print "%3d %8s %8s %6s %8.2f" %(roll, name, last, gender, marks)

	except:
		print "Error: unable to fetch data"

	db.close()
	view()
	return

def view_marks_gt():
	db = MySQLdb.connect("localhost","root","epsilon","college" )
	cursor = db.cursor()

	m = float(raw_input("Enter marks: "))
	sql = "select * from becomp where marks > %f" %m

	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		print "\nROLL FIRT_NAME LAST_NAME GENDER MARKS"
		for row in results:
			roll = row[0]
			name = row[1]
			last = row[2]
			gender = row[3]
			marks = row[4]
			print "%3d %8s %8s %6s %8.2f" %(roll, name, last, gender, marks)

	except:
		print "Error: unable to fetch data"

	db.close()
	view()
	return

def view_marks():
	print "\n**** View by Marks ****"
	print "1. Less than"
	print "2. Greater than"
	print "3. MAIN MENU"
	ch = int(raw_input("Enter your choice: "))
	if ch==1:
		view_marks_lt()
	elif(ch==2):
		view_marks_gt()
	elif(ch==3):
		menu()
	else:
		print "_____PLEASE ENTER CORRECT CHOICE_____\n"
		view_marks()
	view()
	return 

def view():
	print "\n**** View Menu ****"
	print "1. View all"
	print "2. View by gender"
	print "3. View by marks"
	print "4. MAIN MENU"
	ch = int(raw_input("Enter your choice: "))
	if ch==1:
		view_all()
	elif(ch==2):
		view_gender()
	elif(ch==3):
		view_marks()
	elif(ch==4):
		menu()
	else:
		print "_____PLEASE ENTER CORRECT CHOICE_____\n"
		view()
	view()
	return 

def insert():
	db = MySQLdb.connect("localhost","root","epsilon","college" )
	cursor = db.cursor()
	roll = int(raw_input("Enter roll no: "))
	name = raw_input("Enter first name: ")
	last = raw_input("Enter last name: ")
	gender = raw_input("Enter gender: ")
	marks = float(raw_input("Enter marks: "))

	sql = "INSERT INTO becomp VALUES (%d, '%s', '%s', '%s', %f)" %(roll, name.upper(), last.upper(), gender.upper(), marks)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		print "Error"
		db.rollback()

	print "ROW INSERTED SUCCESSFULLY..."
	db.close()
	menu()
	return

def update():
	db = MySQLdb.connect("localhost","root","epsilon","college" )
	cursor = db.cursor()

	r = int(raw_input("Enter roll number to update: "))

	roll = int(raw_input("Enter NEW roll no: "))
	name = raw_input("Enter NEW first name: ")
	last = raw_input("Enter NEW last name: ")
	gender = raw_input("Enter NEW gender: ")
	marks = float(raw_input("Enter NEW marks: "))

	sql = "update becomp set roll=%d, name='%s', surname='%s', gender='%s', marks=%f where roll=%d" %(roll, name.upper(), last.upper(), gender.upper(), marks, r)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		print "Error"
		db.rollback()

	print "*** ROW UPDATED SUCCESSFULLY... ***\n"
	menu()
	return


def delete():
	db = MySQLdb.connect("localhost","root","epsilon","college" )
	cursor = db.cursor()
	r = int(raw_input("Enter roll number to delete: "))
	sql = "delete from becomp where roll=%d" %r

	try:
		cursor.execute(sql)
		db.commit()
	except:
		print "Error: unable to delete data"
		db.rollback()

	print "*** RECORD DELETED SUCCESSFULLY... ***\n"
	db.close()
	menu()
	return

def menu():
	print "\n**** Menu ****"
	print "1. View Database"
	print "2. Add new entry"
	print "3. Update record"
	print "4. Delete record"
	print "5. Exit"
	ch = int(raw_input("Enter your choice: "))
	if ch==1:
		view()
	elif(ch==2):
		insert()
	elif(ch==3):
		update()
	elif(ch==4):
		delete()
	elif(ch==5):
		print "\n **** GOOD BYE ****\n"
		exit(0)
	else:
		print "_____PLEASE ENTER CORRECT CHOICE_____\n"
		menu()
	return

menu()
