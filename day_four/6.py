import math

class Circle:
	radius = float()
	circumference = float()
	area = float()

	def __init__(self, radius):
		self.radius = radius
		self.findCircumference()
		self.findArea()


	def findCircumference(self):
		self.circumference = self.radius * 2 * math.pi

	def findArea(self):
		self.area = math.pi * ( self.radius ** 2 )


my_circle = Circle(20)

print(my_circle.radius)
print(my_circle.circumference)
print(my_circle.area)