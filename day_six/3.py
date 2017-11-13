#BUBBLE SORT

unsorted = [19,13,24,44,7,53,17,88,1,63]

swapped = True

#If there has been at least one swap keep running the while loop
while swapped == True:
	#At the start of each while loop set swapped equal to false
	#If there are any swaps this will become True again.
	#If no swaps it will still be false and the loop will end
	swapped = False

	#For every item in list except for our last item
	for index in range(len(unsorted)-1):
		#Check if the item at index +1 is greater than item at index
		if unsorted[index] > unsorted[index+1]:
			#If it is greater swap
			temp = unsorted[index+1]
			unsorted[index+1] = unsorted[index]
			unsorted[index] = temp
			#And set swapped equal to true
			swapped = True

	#Debug print
	# print(unsorted)

#output
print(unsorted)