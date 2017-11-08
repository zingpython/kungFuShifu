with open("letters.txt", "r") as letter_file:
	lines = letter_file.readlines()

	letter_dict = {}

	for line in lines:
		for letter in line:
			count = letter_dict.get(letter, 0)
			letter_dict[letter] = count + 1

	for key in letter_dict.keys():
		print(key+", "+str(  letter_dict[key] ))


