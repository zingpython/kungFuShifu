import math

class SpaceShip:
	target = [] #2 values, X and then Y
	coordinate = [] #2 values X and then Y
	speed = float()
	name = ""

	def __init__(self, coordinate, target, speed, name):
		self.coordinate = coordinate
		self.target = target
		self.speed = speed
		self.name = name

		#To find the distence calculate the hypotenuse and divide by the speed
	def calculateSteps(self):
		#Get the two sides of out "triangle"
		difference_x = self.target[0] - self.coordinate[0]
		difference_y = self.target[1] - self.coordinate[1]

		#Find the hypotenuse
		hypotenuse = math.sqrt( (difference_x ** 2) + (difference_y ** 2) )

		#Divide by speed and return the result
		return hypotenuse / self.speed

	def moveSpeed(self):
		#Get the two sides of our "triangle"
		difference_x = self.target[0] - self.coordinate[0]
		difference_y = self.target[1] - self.coordinate[1]

		#Find the hypotenuse
		hypotenuse = math.sqrt( (difference_x ** 2) + (difference_y ** 2) )

		#Find the angle of our new triangle
		angle = math.asin( difference_y / hypotenuse )

		#using the angle and speed as out hypotenuse calculate the opposite side of the new triangle
		change_y = math.sin(angle) * self.speed

		#using the angle and speed as our hypotenuse caclute the adjacent sisde of the new triable
		change_x = math.cos(angle) * self.speed

		#Add the sides of the new triangle to our x and y coordinates to get our new location
		self.coordinate[0] = self.coordinate[0] + change_x

		self.coordinate[1] = self.coordinate[1] + change_y

my_ship = SpaceShip([1,1], [5,5], 3, "Enterprise")

print( my_ship.calculateSteps() )
my_ship.moveSpeed()
print(my_ship.coordinate)