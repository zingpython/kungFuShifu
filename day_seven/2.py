import sqlite3
import csv

#Create a function to create all tables and their relations to each other 
def createTables():
	#Connect to database
	connection = sqlite3.connect("employee.db")

	#Start cursor to modifiy database
	cursor = connection.cursor()

	#Create the user table
	cursor.execute(""" CREATE TABLE user(
		id INTEGER PRIMARY KEY,
		name VARCHAR(256),
		email VARCHAR(256),
		country VARCHAR(256)
		) """)

	#Create the phone_number table and its relation to user
	cursor.execute(""" CREATE TABLE phone_number(
		id INTEGER PRIMARY KEY,
		phone VARCHAR(256),
		user_id INTEGER,
		FOREIGN KEY(user_id) REFERENCES user(id)
		) """)

	#Commit the changes to the database and close this connection to the database
	connection.commit()
	connection.close()

# createTables()

#Connect to databse
connection = sqlite3.connect("employee.db")

#Start cursor to modify database
cursor = connection.cursor()

#Open csv file employees.csv
with open("employees.csv") as csvfile:

	#Use the CSV module to read and interpret the CSV file as a list of lists
	csv_rows = csv.reader(csvfile)

	#FOr each row in our list of lists
	for row in csv_rows:
		#Insert a user into the user table
		cursor.execute(""" INSERT INTO user(name,email,country) VALUES (?,?,?) """, (row[0], row[4], row[5]) )

		#Save the changes to the database
		connection.commit()

		#Find the id of the last row inserted into the user table
		last_row = cursor.lastrowid
		print(last_row)

		#For each phone number in the row insert it into the phone number table
		#Using last_row as the id of the User in the foreign key 
		cursor.execute(""" INSERT INTO phone_number(phone,user_id) VALUES (?,?) """, (row[1],last_row ) )
		cursor.execute(""" INSERT INTO phone_number(phone,user_id) VALUES (?,?) """, (row[2],last_row ) )
		cursor.execute(""" INSERT INTO phone_number(phone,user_id) VALUES (?,?) """, (row[3],last_row ) )

		#Save the phone numbers
		connection.commit()	

#Close connecction to database
connection.close()