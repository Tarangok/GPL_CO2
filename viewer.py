import pickle


class Point:
    def __init__( self, x, y, time, value ):
        self.x = x
        self.y = y
        self.time = time
        self.value = value
    def Print( self ):
        print("lat =% 4.8f;\t long =% 4.8f;\t val = % 4.8f;\t time = %s " % ( self.x, self.y, self.value, self.time ))

FILENAME = "points.g2s" # *.gosa2sur   
points = list()

with open( FILENAME, "rb" ) as file:
    points = pickle.load( file )

for p in points:
    p.Print()
