with open("word.txt", "r") as word_file:
	lines = word_file.readlines()

	target_word = input("Enter a word: ")

	output = "not found"

	for word in lines:
		if word[:-1] == target_word:
			output = target_word

	print(output)