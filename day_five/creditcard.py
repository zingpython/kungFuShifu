#Create creditcard class
class CreditCard:
	card_number = ""
	card_type = ""
	valid = False

	#init function should only take the card number and then using the card number find the card type and if the card is valid or not
	def __init__(self, card_number):
		self.card_number = card_number
		self.findCardType()
		self.luhn()


	def findCardType(self):
		#Create a dictionary of starting numbers with the value as the card type
		starting_numbers = {"4":"VISA", "51":"MASTERCARD", 
		"52":"MASTERCARD", "53":"MASTERCARD", "54":"MASTERCARD", "55":"MASTERCARD",
		"34":"AMEX", "37":"AMEX", "6":"DISCOVER"}

		#Create a dictionary with the key of a card type and the value of the length of the card number
		card_length = {"VISA":16, "MASTERCARD":16, "DISCOVER":16, "AMEX":15}

		#Set the default value of card_type to INVALID
		self.card_type = "INVALID"

		#FOr each starting number in dictionary starting numbers check the card_number's starting numbers
		for starting_number in starting_numbers.keys():
			#get the starting numbers of cardnumber equal to the length of starting number.
			#Check if starting number is equal to the first characters of card_number
			if self.card_number[ :len(starting_number) ] == starting_number:
				#If they match then the card_type is the value in starting_numbers at the key starting_number
				self.card_type = starting_numbers[ starting_number ]
				
		#Check if the length of card_number matches the dictioary card_length at the key of the card_type
		if len( self.card_number ) !=  card_length.get(self.card_type, -1 ):
			self.card_type = "INVALID"

	def luhn(self):
		#Create two strings from a slice of card_number
		#Double_string contains every other digit starting from the second to last digit
		double_string = self.card_number[ -2::-2 ]
		#Single string contains every other digit starting from the last digit
		single_string = self.card_number[ -1::-2 ]

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
			self.valid = True
		#Otherwise it is invalid
		else:
			self.valid = False

my_card = CreditCard("448504099328761")
print(my_card.card_type)
print(my_card.valid)