
dictonary = {"A":6,"B":4,"C":1,"D":3,"E":4,"F":1}

search_value = 5

result = []

for key in dictonary.keys():

	if dictonary[key] == search_value:
		result.append(key)

print(result)
