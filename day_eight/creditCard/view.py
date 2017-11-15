class View:

	def printOut(self, output):
		print(output)

	def takeInput(self, prompt):
		return input(prompt)

	def printMenu(self):
		print("1. Enter a card number")
		print("2. Validate your card")
		print("3. Print card information")
		print("4. Exit")
		return input("Enter a menu choice: ")