
number_to_roman = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}

roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

number = int(input("Enter a Number: "))

roman = ""

while number > 0:

	for value in roman_values:
		if number >= value:
			number = number - value
			roman = roman + number_to_roman[value]
			break

print(roman)