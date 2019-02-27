import h5py, pickle, os, datetime

class Point:
	def __init__( self, x, y, time, value):
		self.x = x
		self.y = y
		self.time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f').date()
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

	tmplist = list()
	points = dict()
	dict_str = timeList[0].decode("utf-8")[0:6]
	for i in range(1, numScan):
		if dict_str == timeList[i].decode("utf-8")[0:6]:
			tmplist.append( Point ( longitudeList[i], latitudeList[i], timeList[i].decode("utf-8"), valueList[i] ))
		else:
			points[dict_str] = tmplist
			tmplist.clear()
			dict_str = timeList[i].decode("utf-8")[0:6]
			tmplist.append( Point ( longitudeList[i], latitudeList[i], timeList[i].decode("utf-8"), valueList[i] ))
			

#	points = [ Point( latitudeList[0], longitudeList[0], timeList[0].decode("utf-8"), valueList[0] ) ]				
#	for i in range( 1, numScan ):										
#		points.append( Point(latitudeList[i], longitudeList[i], timeList[i].decode("utf-8"), valueList[i] ) )		
#
	

	#for p in points:
	#    p.Print()
	return points
	#with open(FILENAME, "ab") as file:
	#    pickle.dump(points, file)

if __name__ == "__main__":
	os.system("rm hdflist.txt")
	#os.system("rm points.g2s")
	os.system("ls SWIRL2CO2/ >> hdflist.txt")

	with open("hdflist.txt") as file:
		array = [row.strip() for row in file]

	countFiles = len(array)
	j = 1
	
	tmplist = []
	tmplist.append("None")
	points = dict()
	dict_str = 'None'
	for hdfFile in array:
		os.system("clear || cls")
		print("Progress: ")
		for one_point in range(0,j):
			print(".", end='')

		print("\n %3.1f"% ((j*100)/countFiles), " %  (", j,"/",countFiles, ')')
		j+=1
		f = h5py.File("SWIRL2CO2/"+hdfFile, 'r')
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
		#print(points)
		#print(points.items())
		
		
		print(dict_str)
		for i in range(1, numScan):
			if dict_str == timeList[i].decode("utf-8")[0:7]:
				#print("0:6_1 ", timeList[i].decode("utf-8")[0:7], " str", dict_str, " OK!" )
				
				tmplist.append( Point ( longitudeList[i], latitudeList[i], timeList[i].decode("utf-8"), valueList[i] ))
			else:
				#print("0:6_1 ", timeList[i].decode("utf-8")[0:6])
				points[str(dict_str)] = list(tmplist)
				tmplist.clear()
				dict_str = timeList[i].decode("utf-8")[0:7]
				tmplist.append( Point ( longitudeList[i], latitudeList[i], timeList[i].decode("utf-8"), valueList[i] ))
			
	
	'''
	i = 1
	for e in g2s:
		print(i, end=' ')
		e.Print()
		i += 1
	'''
	
	FILENAME = "points.g2s" # *.gosa2sur
	FILENAME_LITE = "pointslite.g2s" # *.gosa2sur
	with open(FILENAME, "wb") as file:
		pickle.dump(points, file)