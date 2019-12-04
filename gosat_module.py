import os


class Point:
	def __init__(self, x, y, time, value):
		self.x = x
		self.y = y
		self.time = time
		self.value = value

	def __str__(self):
	 return "lat =% 4.8f;\t long =% 4.8f;\t val = % 4.8f;\t time = %s " % ( self.x, self.y, self.value, self.time )



	
