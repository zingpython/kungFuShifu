#Take user input
word = input("Enter a word: ")

#Set boolean to true
palindrome = True

#For each index in word
for index in range( len(word) ):
	#If the current index is not equal to the opposite index then it is not a palindrome
	if word[index] != word[ -(index+1) ]:
		palindrome = False

#Output if palindome or not
if palindrome == True:
	print("PALINDROME")
else:
	print("Not a Palindrome")