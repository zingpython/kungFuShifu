
sieve = list(range(2,101))

index = 0

print(sieve)

while index < len(sieve):


	counter = index + 1

	while counter < len(sieve):
		if sieve[counter] % sieve[index] == 0:
			del sieve[counter]
		else:
			counter = counter + 1

	index = index + 1

print(sieve)
