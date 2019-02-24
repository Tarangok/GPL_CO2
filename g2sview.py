import pickle


class Point:
    def __init__( self, x, y, time, value ):
        self.x = x
        self.y = y
        self.time = time
        self.value = value
    def Print( self ):
        #print( self.x, " ", self.y, " ", self.time, " ", self.value )
        print("lat =% 4.6f;\t long =% 4.6f;\t val = % 4.6f;\t time = %s " % ( self.x, self.y, self.value, self.time ))



if __name__ == "__main__":
    FILENAME = "points.g2s" # *.gosa2sur
    with open( FILENAME, "rb" ) as file:
        numScan = pickle.load( file )
        
    points = list()

    with open( FILENAME, "rb" ) as file:
        points = pickle.load( file )

    for p in points:
        p.Print()
