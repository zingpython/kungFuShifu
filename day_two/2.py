#Take in user input
sentence = input("Enter a sentence: ")

#Create empty string that will be our capitalized sentence
new_sentence = ""

#If this is true the next letter we find must be captialized
capitalize_next = True

#FOr each letter in the user's sentence
for index in range( len(sentence) ):
	#If the letter is an alphabetic character and captialize next is true
	if sentence[index].isalpha() == True and capitalize_next == True:
		#Add it to the new_sentence as a captial letter
		new_sentence = new_sentence + sentence[index].upper()
		#Do not captialize the next letter so set captialize_next equal to false
		capitalize_next = False

	#If we find a . ! or ? we know that that is the end of a sentence and we need to capitailize the next letter.
	elif sentence[index] == "." or sentence[index] == "!" or sentence[index] == "?":
		capitalize_next = True
		new_sentence = new_sentence + sentence[index]

	#if a lowercase i has a non letter character to the left and right we can capitalize that i.
	elif sentence[index] == "i" and sentence[index+1].isalpha() == False and sentence[index-1].isalpha() == False:
		new_sentence = new_sentence + sentence[index].upper()

	#If all other ifs fail add the letter as is to the new sentence
	else:
		new_sentence = new_sentence + sentence[index]

#print new sentence
print(new_sentence)

