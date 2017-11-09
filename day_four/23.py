
#Convert an interger to a binary in the form of a string
def intToBinary(number):
	#Create empty string to hold our new binary number
	binary_number = ""

	#While our number is greater than 0 Keep dividing by 2 and adding the remainder to binary_number
	while number > 0:
		#Divmod divindes the 1st number by the 2nd number and returns a tuple with the format (quotient, remainder)
		temp_number = divmod(number, 2)
		#Set number equal to the quotient from divmod
		number = temp_number[0]
		#Next add the remainder to the front of binary_number
		binary_number = str( temp_number[1] )+ binary_number

	#return binary_number
	return binary_number

#Convert a binary string to an integer
def binaryToInteger(binary):
	#Create a total that will be returned at the end
	total = 0

	#Increase is the number to increase the total by if the digit of the binary string is a 1
	increase = 1

	#For each digit in the binary string we will iterate over it backwards
	for index in range(len(binary)-1, -1 ,-1 ):
		#If the current digit is a 1 then we need to increase total by the variable increase
		if binary[index] == "1":
			total = total + increase

		#Double increase
		increase = increase * 2

	#return total
	return total


print( intToBinary(2000) )

print( binaryToInteger("11111010000") )