# dict_of_list = {}

# def insert_or_create(dictionary, key, value):
# 	if key not in dictionary.keys():
# 		dictionary[key] = [value]
# 	else:
# 		dictionary[key].append(value)

# insert_or_create(dict_of_list, "Hello", "world")

# print(dict_of_list)


# choosing = True
# number = ""
# while choosing == True:
# 	try:
# 		number = int(input("Enter a number: "))
# 		choosing = False
# 	except ValueError:
# 		print("Invalid number, try again")

# print(number)

class Car:
	wheels = ""
	horsepwr = int()
	four_wd = False
	fuel = ""
	color = ""
	make = ""
	model = ""
	year = ""
	licenseplate = ""

	def __init__(self, wheels, horsepwr, four_wd, fuel, color, make, model, year, licenseplate):
		self.wheels = wheels
		self.horsepwr = horsepwr
		self.four_wd = four_wd
		self.fuel = fuel
		self.color = color
		self.make = make
		self.model = model
		self.year = year
		self.licenseplate = licenseplate

	def printOut(self):
		print("You have a "+ self.year + " " +self.make +" "+ self.model )

	def getColor(self):
		return self.color

	def setColor(self, color):
		self.color = color


my_car = Car("Firestone wheels", 132, False, "Gas", "red", "Toyota", "Carolla", "2010", "123-4566")
print( my_car.fuel )
my_car.fuel = "Biodiesel"
print( my_car.fuel )
my_car.printOut()

hector_car = Car("Standard Tires", 155, False, "Jet Fuel", "White", "Chevy", "Cobalt", "2010", "123-4567")