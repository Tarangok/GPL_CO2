import h5py, pickle, os

class Point:
    def __init__( self, x, y, time, value ):
        self.x = x
        self.y = y
        self.time = time
        self.value = value
    def Print( self ):
        print("lat =% 4.8f;\t long =% 4.8f;\t val = % 4.8f;\t time = %s " % ( self.x, self.y, self.value, self.time ))

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

    

    #for p in points:
    #    p.Print()
    return points
    #with open(FILENAME, "ab") as file:
    #    pickle.dump(points, file)

if __name__ == "__main__":
    #os.system("rm hdflist.txt")
    #os.system("rm points.g2s")
    #os.system("ls SWIRL2CO2/ >> hdflist.txt")

    with open("hdflist.txt") as file:
        array = [row.strip() for row in file]

    countFiles = len(array)
    i = 1
    g2s = list()
    for hdfFile in array:
        os.system("clear || cls")
        print("Progress: ", "%3.1f"% ((i*100)/countFiles), " %  (", i,"/",countFiles, ')')
        g2s += convert(hdfFile)
        i+=1
    
    '''
    i = 1
    for e in g2s:
        print(i, end=' ')
        e.Print()
        i += 1
    '''
    FILENAME = "points.g2s" # *.gosa2sur
    FILENAME_LITE = "pointslite.g2s" # *.gosa2sur
    with open(FILENAME_LITE, "ab") as file:
        pickle.dump(g2s, file)