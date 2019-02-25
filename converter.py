import h5py, pickle, os

class Point:
    def __init__( self, x, y, t, v ):
        self.x = x
        self.y = y
        self.time = t
        self.value = v
    def Print( self ):
        print( self.x, " ", self.y, " ", self.time, " ", self.value )

def convert(filename):
    f = h5py.File("SWIRL2CO2/"+filename, 'r')
    Data = f['Data']
    geolocation = Data['geolocation']
    longitude = geolocation['longitude']
    latitude = geolocation['latitude']
    scanAttribute = f['scanAttribute']
    mixingRatio = Data['mixingRatio']

    # Кол-во сканирований
    numScan = list(scanAttribute['numScan'])[0]							

    # Время
    timeList = list(scanAttribute['time'])

    # Значение
    valueList = list(mixingRatio['XCO2'])

    # Списки долготы и ширины
    longitudeList = list( longitude )									
    latitudeList = list( latitude )

    points = [ Point( latitudeList[0], longitudeList[0], timeList[0].decode("utf-8"), valueList[0] ) ]				
    for i in range( 1, numScan ):										
        points.append( Point(latitudeList[i], longitudeList[i], timeList[i].decode("utf-8"), valueList[i] ) )		

    FILENAME = "points.g2s" # *.gosa2sur

    with open(FILENAME, "ab") as file:
        pickle.dump(points, file)

if __name__ == "__main__":
    os.system("ls SWIRL2CO2/ >> hdflist.txt")

    with open("hdflist.txt") as file:
        array = [row.strip() for row in file]

    countFiles = len(array)
    i = 1

    for hdfFile in array:
        print(i,"/",countFiles)
        convert(hdfFile)
        i+=1
