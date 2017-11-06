side1 = input("Enter the length of the first side: ")
side2 = input("Enter the length of the second side: ")
side3 = input("Enter the length of the third side: ")

if side1 == side2 and side2 == side3:
	print("Equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
	print("Isosceles")
else:
	print("Scalene")