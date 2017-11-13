#INSERTION SORT

#Do not create a new list, it is not needed for an insertion sort
unsorted = [19,13,24,44,7,53,17,88,1,63]

#For each item in unsorted find the proper place to insert it
for i in range(len(unsorted)):
	#Starting from one less than the index I, iterate backwards to 0
	for j in range(i-1,-1,-1):
		#If the value at index I is greater than the value at the index J insert the item at index I infront of index J
		if unsorted[i] > unsorted[j]:
			#Add index I after index J
			unsorted.insert( j+1, unsorted.pop(i) )
			#End the loop to prevent extra swaps
			break
		#If at the end of the list I is not greater and any J insert at the begin of the list
		#This only triggers if the value at I is less than every other value before it.
		elif j == 0 and unsorted[i] < unsorted[j]:
			unsorted.insert( 0, unsorted.pop(i) )

	#Show current progress (For debugging)
	# print(unsorted)

print(unsorted)