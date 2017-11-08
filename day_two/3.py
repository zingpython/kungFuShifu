#Take user input
word1 = input("Enter a word: ")
word2 = input("Enter a word: ")
#Create two empty dictionaries. These will have a key of a letter and a value of how many times that letter has appeared
letters1 = {}
letters2 = {}

#For each letter in word1 check if letter is in letters1. If not add it with a value of 1. Else increase its value by 1
for letter in word1:
	if letter not in letters1.keys():
		letters1[letter] = 1
	else:
		letters1[letter] = letters1[letter] + 1

for letter in word2:
	if letter not in letters2.keys():
		letters2[letter] = 1
	else:
		letters2[letter] = letters2[letter] + 1

#Check if dictonaries have the exact same key value pairs
if letters1 == letters2:
	print("ANAGRAM")