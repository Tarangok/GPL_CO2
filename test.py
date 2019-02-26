import pickle, datetime

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

	def GetT( self ):
		return self.time

if __name__ == "__main__":
	with open( "points.g2s", "rb" ) as file:
		points = pickle.load( file )
	
	for p in points:
		if datetime.datetime.strptime(p.GetT(), '%Y-%m-%d %H:%M:%S.%f').date().year == 2010:
			print(p.Print())

	
	#datetime.date(2012, 1, 30)