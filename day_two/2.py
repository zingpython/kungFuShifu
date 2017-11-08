
sentence = input("Enter a sentence: ")

new_sentence = ""

capitalize_next = True

for index in range( len(sentence) ):
	if sentence[index].isalpha()  and capitalize_next == True:
		new_sentence = new_sentence + sentence[index].upper()
		capitalize_next = False

	elif sentence[index] == "." or sentence[index] == "!" or sentence[index] == "?":
		capitalize_next = True
		new_sentence = new_sentence + sentence[index]

	elif sentence[index] == "i" and sentence[index+1].isalpha() == False and sentence[index-1].isalpha() == False:
		new_sentence = new_sentence + sentence[index].upper()

	else:
		new_sentence = new_sentence + sentence[index]

print(new_sentence)

