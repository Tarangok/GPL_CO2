import pickle

class Point:
	def __init__( self, x, y, time, value ):
		self.x = x
		self.y = y
		self.time = time
		self.value = value

	def Print( self ):
		print("lat =% 4.8f;\t long =% 4.8f;\t val = % 4.8f;\t time = %s " % ( self.x, self.y, self.value, self.time ))

	def GetX( self ):
		return self.x

	def GetY( self ):
		return self.y

	def GetV( self ):
		return self.value

if __name__ == "__main__":

	with open( "points.g2s", "rb" ) as file:
		points = pickle.load( file )
	i = 1
	maxValue = points[0].GetV()
	minValue = points[0].GetV()
	for p in points:
		if p.GetV() > maxValue:
			maxValue = p.GetV()
		if p.GetV() < minValue:
			minValue = p.GetV()
	print(minValue, " ", maxValue)