#SELECTION SORT

unsorted = [19,13,24,44,7,53,17,88,1,63]

#Create empty list that will hold all values sorted
sorted_list = []

#While unsorted is not empty find the lowest value
while len(unsorted) > 0:
	#Index of the lowest value
	lowest = 0

	#For each item in unsorted
	for item in range(len(unsorted)):
		#If the item at the index of item is less than lowest
		if unsorted[item] < unsorted[lowest]:
			#Set lowest equal to item
			lowest = item

	#Remove item at index lowest from unsorted and add to the end of sorted
	sorted_list.append( unsorted.pop(lowest) )

print(sorted_list)