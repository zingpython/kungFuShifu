
n = 30

for x in range( 1 , 2*n ):
	
	if x <= n:

		# output = ""
		for y in range(x):
			# output = output + "* "
			print("* ",end="")

		print()
		# print(output)
	else:

		for z in range( n-(x-n) ):
			print("* ",end="")

		print()