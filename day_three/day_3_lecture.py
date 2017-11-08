

# text_file = open("word.txt","r")

with open("reverse_word.txt", "r", encoding="UTF-8") as text_file:
	with open("word.txt", "w", encoding="UTF-8") as write_file:
		lines = text_file.readlines()
		for line in lines:
			# print(line[:-1])
			write_file.write( line[-2::-1] + "\n" )


# with open("word.txt", "a", encoding="UTF-8") as append_file:
# 	new_word = input("Enter a word: ")
# 	append_file.write("\n"+new_word)

#Does not work. Still not sure why
# with open("word.txt", "r+", encoding="UTF-8") as read_write_file:
# 	line = read_write_file.read()
# 	count = 1
# 	while line != "":
# 		print(line)
# 		read_write_file.write( str(count) +". "+line)
# 		line = read_write_file.read()
# 		count = count +1