import sqlite3

def createTables():
	connection = sqlite3.connection("lecture.db")

	cursor = connection.cursor()

	cursor.execute(""" CREATE TABLE student(
		id INTEGER PRIMARY KEY,
		name VARCHAR(256),
		average REAL) """)

	connection.commit()

	connection.close()

# createTables()

connection = sqlite3.connect("lecture.db")

cursor = connection.cursor()

name = "Matthew"

cursor.execute(""" INSERT INTO student(name,average) VALUES (?,?) """, (name, 91.3) )

connection.commit()

cursor.execute(""" SELECT * FROM student """)

student_info = cursor.fetchall()

print(student_info)

connection.close()