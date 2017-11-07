# For each number between 1 and 100 check if it is prime
for x in range(1,101):
	#Set the boolean prime to True
	prime = True
	#For each number between 2 and x check if x is divisible by y
	for y in range(2,x):
		#If x is divisble by y then x is not prime
		if x%y == 0:
			prime = False
	#If prime is True then prime Prime otherwise print x
	if prime == True:
		print("PRIME")
	else:
		print(x)