import h5py, pickle


class Point:
    def __init__( self, x, y, t, v ):
        self.x = x
        self.y = y
        self.time = t
        self.value = v
    def Print( self ):
        print( self.x, " ", self.y, " ", self.time, " ", self.value )

if __name__ == "__main__":
	f = h5py.File('SWIRL2CO2/GOSATTFTS20181124_02C01SV0280R181124GU000.h5', 'r')
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

	# Проверка
	#for point in points:												
	#	point.Print()

	# Запись в файл
	FILENAME = "points.g2s" # *.gosa2sur
	with open(FILENAME, "wb") as file:
		pickle.dump(numScan, file)

	
	with open(FILENAME, "wb") as file:
		pickle.dump(points, file)
