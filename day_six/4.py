#MERGE SORT

unsorted = [19,13,24,44,7,53,17,88,1,63]

#Convert to a list of lists
for index in range(len(unsorted)):
	unsorted[index] = [ unsorted[index] ]

print(unsorted)

#While the list of lists has more than 1 list in it.
while len(unsorted) > 1:

	#Create a placehold list to hold the new unsorted list
	new_unsorted = []

	#FOr every other index in unsorted
	for index in range(0, len(unsorted), 2):

		#Create a new list to be added to new_unsorted
		merged_list = []

		#If index is not the last item begin merging the list at index with the list at index+1
		if index+1 != len(unsorted):

			#While either the list at index or index+1 has at least one item in it run the while loop
			while len(unsorted[index]) > 0 or len(unsorted[index+1]) > 0:

				#If the list at index is empty add the contents of index+1 to merged_list
				if len(unsorted[index]) == 0:
					merged_list.append( unsorted[index+1][0] )
					unsorted[index+1].pop(0)

				#If the list at index+1 is empty add the contents of index to merged_list
				elif len(unsorted[index+1]) == 0:
					merged_list.append( unsorted[index][0] )
					unsorted[index].pop(0)

				#If both lists are not empty check which item at the index 0 is less than the other
				#And insert that item into merged_list
				elif unsorted[index][0] < unsorted[index+1][0]:
					merged_list.append( unsorted[index][0] )
					unsorted[index].pop(0)

				elif unsorted[index][0] >= unsorted[index+1][0]:
					merged_list.append( unsorted[index+1][0] )
					unsorted[index+1].pop(0)

		#If the index is the last item in unsorted add its contents to merged_list
		else:
			merged_list = unsorted[index]

		#Append merged_list to new_unsorted
		new_unsorted.append(merged_list)

	# print(new_unsorted)
	#Set unsorted equal to new_unsorted
	unsorted = new_unsorted


print(unsorted)