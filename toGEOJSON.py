import pickle
import sys
from geojson import Point as geoPoint

class Point:
    def __init__( self, x, y, time, value ):
        self.x = x
        self.y = y
        self.time = time
        self.value = value
    def Print( self ):
        print("lat =% 4.8f;\t long =% 4.8f;\t val = % 4.8f;\t time = %s " % ( self.x, self.y, self.value, self.time ))
    
    def GetX(self):
        return self.x
    def GetY(self):
        return self.y
    def GetT(self):
        return self.time
    def GetV(self):
        return self.value

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("FATAL ERROR: No input file!")
        exit()
    else:
        FILENAME = sys.argv[1] # *.gosa2sur   
        points = list()

        with open( FILENAME, "rb" ) as file:
            points = pickle.load( file )
        i = 1
        f = open('geojson.json', 'w+')
        geo_points = list()
        for p in points:
            #print(i, end=' ')          
            #print( geoPoint( ( float( p.GetX() ), float( p.GetY() ) ), value=int( p.GetV() ), time=str( p.GetT() ) ) )
            f.write( '{\n"type": "Feature",\n"geometry": ' + str( geoPoint( ( float( p.GetY() ), float( p.GetX() ) )) ) + ',\n"properties": {\n"value":'+str(p.GetV())+'}\n},\n')
            i += 1
