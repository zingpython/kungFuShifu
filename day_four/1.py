def findWord(target_word, filename):

	with open(filename, "r") as word_file:
		lines = word_file.readlines()

		output = "not found"

		for word in lines:
			if word[:-1] == target_word:
				output = target_word

		print(output)

findWord("hello","word.txt")

def countLetter(filename):
	with open(filename, "r") as letter_file:
		lines = letter_file.readlines()

		letter_dict = {}

		for line in lines:
			for letter in line:
				count = letter_dict.get(letter, 0)
				letter_dict[letter] = count + 1

		for key in letter_dict.keys():
			print(key+", "+str(  letter_dict[key] ))


countLetter("word.txt")