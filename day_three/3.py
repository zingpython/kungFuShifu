#take in file name
filename = input("Enter a file name: ")
#Take in number of words to output
output_number = int( input("Enter a number: ") ) 

#Open our file
with open(filename, "r", encoding="ISO 8859-1") as article_file:
	#Read each line in the file
	lines = article_file.readlines()

	#Dictionary of wards that starts empty
	word_dict = {}

	#For each word on each line insert it into the dictionary or if it exists increment the count by 1
	for line in lines:
		words = line.split(" ")
		for word in words:
			count = word_dict.get(word,0)
			word_dict[word] = count + 1

	# print(word_dict)

	#Create output list. empty
	output_list = []

	#For each word in the dictionary word_dict add to the output list
	for word in word_dict.keys():
		
		#IF the length of output list is less than output number add word to list in place and do not remove item from list
		if len(output_list) < output_number:
			
			#For each word in output list check if the value of word is greater than the word in output list
			for index in range( len(output_list) ):
				#If the value is greater add infront of the current index and stop loop
				if word_dict[word] > word_dict[ output_list[index] ]:
					output_list.insert(index, word)
					break
				#If the word's value is less than all other words in output_list add to the end of output list
				elif word_dict[word] < word_dict[ output_list[index] ] and index == len(output_list)-1:
					output_list.append(word)

			#IF the list is empty insert the first word found into the list.
			#We need to do this so the loop can run.
			if len(output_list) == 0:
				output_list.append(word)
		#If output_list's length is greater than or equal to output_number
		else:
			#Then sort the word into the list and remove the last item if you insert word into the list
			#Removing the last item preserves the length of the list
			for index in range( len(output_list) ):
				if word_dict[word] > word_dict[ output_list[index] ]:
					output_list.insert(index, word)
					output_list.pop()
					break
			
	#Output in proper format	
	for item in output_list:
		print(item+", "+ str(word_dict[item]) )