from random import randrange

random_list = []

for x in range(10):
	random_list.append( randrange(1, 101) )

print(random_list)

maximum = -1

for number in random_list:
	if maximum < number:
		maximum = number

print(maximum)