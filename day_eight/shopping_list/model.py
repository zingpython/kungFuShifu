import sqlite3

class ShoppingList:


	def __init__(self):
		self.connection = sqlite3.connect("shopping.db")

		self.cursor = self.connection.cursor()

	def createTables(self):

		self.cursor.execute(""" CREATE TABLE shopping_list(
			id INTEGER PRIMARY KEY,
			item VARCHAR(256),
			checked VARCHAR(9)
			) """)

		self.connection.commit()

	def closeConnection(self):
		self.connection.close()

	def selectTable(self):

		self.cursor.execute("SELECT * FROM shopping_list")

		return self.cursor.fetchall()

	def insertRow(self, item):

		self.cursor.execute("INSERT INTO shopping_list(item,checked) VALUES (?,?)",(item,"UNCHECKED") )

		self.connection.commit()

	def updateChecked(self, checked, list_id):

		self.cursor.execute("UPDATE shopping_list SET checked=? WHERE id=?",(checked, list_id) )

		self.connection.commit()

	def checkID(self, list_id):
		self.cursor.execute("SELECT * FROM shopping_list WHERE id=?", (list_id,) )

		return self.cursor.fetchall()


if __name__ == "__main__":
	my_database = ShoppingList()
	my_database.createTables()
	my_database.closeConnection()