from view import View
from model import CreditCard

def validateCard(credit_card):
	#Create a dictionary of starting numbers with the value as the card type
	starting_numbers = {"4":"VISA", "51":"MASTERCARD", 
	"52":"MASTERCARD", "53":"MASTERCARD", "54":"MASTERCARD", "55":"MASTERCARD",
	"34":"AMEX", "37":"AMEX", "6":"DISCOVER"}

	#Create a dictionary with the key of a card type and the value of the length of the card number
	card_length = {"VISA":16, "MASTERCARD":16, "DISCOVER":16, "AMEX":15}

	#Set the default value of card_type to INVALID
	credit_card.setCardType("INVALID")

	#FOr each starting number in dictionary starting numbers check the card_number's starting numbers
	for starting_number in starting_numbers.keys():
		#get the starting numbers of cardnumber equal to the length of starting number.
		#Check if starting number is equal to the first characters of card_number
		if credit_card.getCardNumber()[ :len(starting_number) ] == starting_number:
			#If they match then the card_type is the value in starting_numbers at the key starting_number
			credit_card.setCardType( starting_numbers[ starting_number ] )
			
	#Check if the length of card_number matches the dictioary card_length at the key of the card_type
	if len( credit_card.getCardNumber() ) !=  card_length.get(credit_card.getCardType(), -1 ):
		credit_card.setCardType("INVALID")


def luhn(credit_card):

	#Create two strings from a slice of card_number
	#Double_string contains every other digit starting from the second to last digit
	double_string = credit_card.getCardNumber()[ -2::-2 ]
	#Single string contains every other digit starting from the last digit
	single_string = credit_card.getCardNumber()[ -1::-2 ]

	#Create an empty list that will hold all of the doubled numbers
	double_list = []

	#For each digit in double string
	for digit in double_string:
		#Convert to an integer
		number = int(digit)
		#And append to double_list as twice that integers
		double_list.append( number*2 )

	#Create a total of all digits
	total = 0

	#For each digit in single_string convert to integer and add to total
	for digit in single_string:
		total = total + int(digit)

	#For each number in double_list
	for number in double_list:
		#If it is greater than 10 ad the total of its digits
		if number >= 10:
			total = total + 1 + (number-10)
		#If it is less than 10 add it directly to the total
		else:
			total = total + number

	#If the total % 10 returns a remainder of 0 then it is valid
	if total % 10 == 0:
		credit_card.setValid(True)
	#Otherwise it is invalid
	else:
		credit_Card.setValid(False)



my_view = View()

my_card = CreditCard("")

choosing = True

while choosing == True:

	menu_choice = my_view.printMenu()

	if menu_choice =="1":
		new_card_number = my_view.takeInput("Enter a card number: ")
		my_card.setCardNumber(new_card_number)

	elif menu_choice == "2":
		validateCard(my_card)
		luhn(my_card)

	elif menu_choice == "3":
		my_view.printOut("Your card number is "+ my_card.getCardNumber()+". Your card is a "+my_card.getCardType()+". Your card is valid: "+str( my_card.getValid() ) )

	elif menu_choice == "4":
		choosing = False

	else:
		my_view.printOut("Not a valid choice, try again")

# my_view.printOut("This is a test of the MVC")

# my_card_number = my_view.takeInput("Enter a creditcard number: ")

# my_card = CreditCard(my_card_number)

# my_view.printOut( my_card.getCardNumber() )

# validateCard(my_card)

# luhn(my_card)

# my_view.printOut( my_card.getValid() )

# my_view.printOut( my_card.getCardType() )
