
number_of_words = int( input("How many words will you input? ") )

word_list = []

for x in range(number_of_words):
	word = input("Enter a word: ")

	if word not in word_list:
		word_list.append(word)


print(word_list)