import pickle


class Point:
    def __init__( self, x, y, t, v ):
        self.x = x
        self.y = y
        self.time = t
        self.value = v
    def Print( self ):
        print( self.x, " ", self.y, " ", self.time, " ", self.value )



if __name__ == "__main__":
    FILENAME = "points.g2s" # *.gosa2sur
    with open( FILENAME, "rb" ) as file:
        numScan = pickle.load( file )
        
    points = list()

    with open( FILENAME, "rb" ) as file:
        points = pickle.load( file )

    for p in points:
        p.Print()
