Exercise 1:

Using the SQL Schema Designer (http://ondras.zarovi.cz/sql/demo/) design the following 3 tables.

	1. A Table that models movies. The rows should include; the title, director, lead actor, length, and year that it was released

	2. Create a database that models employees, departments that an employee can work in, and their relation to each other.

	3. Create a database that models a school. This should include; students, teachers, classes, and a schedule


Exercise 2:

In this challenge, you will be asked to import CSV data into a sqlite database.

In the CSV file, you will find a person with a name, email, country of residence, and three phone numbers.

Create a users table and a phone numbers table. The relation is that a user has many phone numbers. Create the schema in SQL designer and push it to this folder on Github.

When you have done that, use Python's sqlite3 library to create the tables.

Hints:
Take a look here at Python's sqlite driver documentation
```
https://docs.python.org/3.4/library/sqlite3.html
```

You need to establish a database and a cursor object.
```py
import sqlite3
conn = sqlite3.connect('mydb.db')
c = conn.cursor()
```
To create a table:
```py
c.execute("CREATE TABLE 'users' (
'id' INTEGER,
'name' VARCHAR,
'account' VARCHAR,
'balance' REAL,
PRIMARY KEY ('id')
)")
```
To insert a row of data:
```py
c.execute("INSERT INTO users(name, account, balance) VALUES(?,?,?)", (name, account, balance))
```
**Note: ** You must specify the columns names otherwise sqlite3 will default to all columns. 

dir() and help() the cursor for all the methods possible.

What does executemany do?

What are your options for fetch?


Take a look at the CSV library for Python's documentation
```
https://docs.python.org/3.4/library/csv.html
```

Import the file using Python's csv library and figure out how to write this data into the appropriate table and column in the db.
