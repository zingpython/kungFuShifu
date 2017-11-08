
#Take user input
word = input("Enter a sentence to be scrambled: ")

shift = int( input("Enter how much to shift: ") )

#Create the empty string that will become our new message
new_message = ""

for letter in word:
	#If uppercase letter
	if ord(letter) >= 65 and ord(letter) <= 90:
		#Convert to number and shift
		shifted_number = ord(letter) + shift
		#If shifted number is out of range return to range
		if shifted_number <65:
			shifted_number = shifted_number + 26
		elif shifted_number > 90:
			shifted_number = shifted_number - 26

		#Convert shifted number back to a letter and add to new message
		new_message = new_message + chr(shifted_number)

	#If lowercase letter
	elif ord(letter) >= 97 and ord(letter) <= 122:
		#Convert to number and shift
		shifted_number = ord(letter) + shift
		#If shifted number is out of range return to range
		if shifted_number <97:
			shifted_number = shifted_number + 26
		elif shifted_number > 122:
			shifted_number = shifted_number - 26

		#Convert shifted number back to a letter and add to new message
		new_message = new_message + chr(shifted_number)

	else:
		new_message = new_message + letter

print(new_message)