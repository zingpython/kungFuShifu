
class View:

	def printOut(self, output):
		print(output)

	def takeInput(self, prompt):
		return input(prompt)

	def menu(self):
		print("1. Add item to list")
		print("2. Display list")
		print("3. Check off item")
		print("4. Uncheck item")
		print("5. Exit")

		return input("Eenter a menu number: ")

	def printList(self, list_of_rows):
		print("id \t |item \t |checked ")
		for row in list_of_rows:
			print( str(row[0]) + "\t |"+row[1]+"\t |"+row[2] )