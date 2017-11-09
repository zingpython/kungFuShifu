class Bucket:
	name = ""
	max_volume = float()
	current_volume = float()

	def __init__(self, name, max_volume, current_volume):
		self.name = name
		self.max_volume = max_volume
		self.current_volume = current_volume

	def getName(self):
		return self.name

	def getMaxVolume(self):
		return self.max_volume

	def getCurrentVolume(self):
		return self.current_volume

	def setCurrentVolume(self, current_volume):
		self.current_volume = current_volume

	#Transfer contents of another bucket to this bucket
	def transferBucket(self, another_bucket):
		max_transfer = self.max_volume - self.current_volume
		other_volume = another_bucket.getCurrentVolume()

		if max_transfer >= other_volume:
			self.current_volume = self.current_volume + other_volume
			another_bucket.setCurrentVolume(0)

		else:
			self.current_volume = self.max_volume
			another_bucket.setCurrentVolume( another_bucket.getCurrentVolume() - max_transfer )


my_bucket_1 = Bucket("Pail", 3, 1)
my_bucket_2 = Bucket("Cistern", 10000, 3000)

print(my_bucket_1.getCurrentVolume() )
print(my_bucket_2.getCurrentVolume() )
my_bucket_1.transferBucket( my_bucket_2 )
print(my_bucket_1.getCurrentVolume() )
print(my_bucket_2.getCurrentVolume() )
my_bucket_2.transferBucket( my_bucket_1 )
print(my_bucket_1.getCurrentVolume() )
print(my_bucket_2.getCurrentVolume() )