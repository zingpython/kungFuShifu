#BINARY SEARCH

def binarySearch(ordered_list, target):

	running = True
	# While running is true
	while running == True:
		#Get the left half and right half of the list
		left_half = ordered_list[ 0: len(ordered_list)//2 ]
		right_half = ordered_list[ len(ordered_list)//2:  ]

		# print(left_half)
		# print(right_half)
		# print("--------------------")

		#If there is only one item in the left half and it matches target return the item
		if len(left_half) == 1 and target == left_half[0]:
			return left_half[0]

		#If there is only one item in the right half and it atches the target return it
		elif len(right_half) == 1 and target == right_half[0]:
			return right_half[0]

		#If the target is in between the range of the least and greatest value of the left half
		elif target >= left_half[0] and target <= left_half[-1]:
			#Set ordered list equal to the left half and run the while loop again
			ordered_list = left_half

		#If the target is inbetween the range of the least and greatest values of the right half
		elif target >= right_half[0] and target <= right_half[-1]:
			#set ordered list equal to the right half and run the while loop again
			ordered_list = right_half

		#If the target is not in either the left half or right half return FALSE
		else:
			return False




ordered_list = [1,2,4,5,6,7,8,9,10,11]
target = 3
print(binarySearch(ordered_list, target))