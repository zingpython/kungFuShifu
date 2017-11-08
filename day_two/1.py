
#Dictonaries to convert a letter to a number and a number to a letter
alpha_to_num = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

num_to_alpha = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}

#Take user input
word = input("Enter a sentence to be scrambled: ")

shift = int( input("Enter how much to shift: ") )

#Create the empty string that will become our new message
new_message = ""

#For each letter in word process it and add it to new message
for index in range( len(word) ):
	#If the character is a letter shift it. If not add it to our new message
	if word[index].isalpha() == True:
		#Check if the letter is uppercase
		uppercase = False
		if word[index].isupper() == True:
			uppercase = True

			#Get the number associated to the letter
		number = alpha_to_num.get( word[index].lower(),False)
		if number != False:
			#Shift the nuber by shift
			number = number + shift

			#Check if number is out of range
			if number > 26:
				number = number - 26
			elif number < 1:
				number = number + 26
			
			#Convert number back to letter and if uppercase make the etter upper
			if uppercase == True: 
				letter = num_to_alpha[number].upper()
			else:
				letter = num_to_alpha[number]

			#Add letter to new message
			new_message = new_message + letter

	else:
		new_message = new_message + word[index]

#Print message
print(new_message)