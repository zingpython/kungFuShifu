class CreditCard:
	card_number = ""
	card_type = ""
	valid = False

	def __init__(self, card_number):
		self.card_number = card_number

	def getCardNumber(self):
		return self.card_number

	def setCardNumber(self, card_number):
		self.card_number = card_number

	def getCardType(self):
		return self.card_type

	def setCardType(self, card_type):
		self.card_type = card_type

	def getValid(self):
		return self.valid

	def setValid(self, valid):
		self.valid = valid