
#For every value of X do 1 to 10 as y
for x in range(1, 11):
	for y in range(1, 11):
		#multiply x*y and put a tab space at the end  of the print statement for formatting
		print(x*y, end="\t")
	#Once a row in the multiplication table is finished move to the next line
	print()
