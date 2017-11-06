letter = input("Enter a letter: ")

# if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
if letter in ["a","e","i","o","u"]:
	print(letter+" is a vowel")
elif letter == "y":
	print(letter+" is sometimes a vowel and sometimes a consonant")
else:
	print(letter+" is consonant")