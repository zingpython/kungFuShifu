from model import ShoppingList
from view import View

def checkOrUncheck(check):
	my_view = View()
	my_database = ShoppingList()

	user_input = my_view.takeInput("Enter an ID of an ite in your list: ")

	try:
		user_input = int(user_input)
	except ValueError:
		return "Not a number. Try again"

	found_result = my_database.checkID(user_input)

	if len(found_result) == 0:
		return "ID not found"
	else:
		my_database.updateChecked(check, user_input)
		return check


my_view = View()

my_database = ShoppingList()

running = True

while running == True:
	user_input = my_view.menu()

	if user_input == "1":
		item = my_view.takeInput("Enter an item to add to the list: ")

		my_database.insertRow(item)

	elif user_input == "2":
		rows = my_database.selectTable()

		my_view.printList(rows)

	elif user_input == "3":
		output = checkOrUncheck("CHECKED")
		my_view.printOut(output)

	elif user_input == "4":
		output = checkOrUncheck("UNCHECKED")
		my_view.printOut(output)

	elif user_input == "5":
		running = False
	else:
		my_view.printOut("Invalid menu item, try again")


my_database.closeConnection()