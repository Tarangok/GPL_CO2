import h5py, pickle, os, datetime

class Point:
	def __init__( self, x, y, time, value):
		self.x = x
		self.y = y
		self.time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f').date()
		self.value = value
	def Print( self ):
		print("lat =% 4.8f;\t long =% 4.8f;\t val = % 4.8f;\t time = %s " % ( self.x, self.y, self.value, self.time ))

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
		print("Progress: ", end='')

		for one_point in range(0,int((j*100)/countFiles)):
			print(".", end='')

		print(" %3.1f"% ((j*100)/countFiles), " %  (", j,"/",countFiles, ')')
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
			
	FILENAME = "points.g2s" # *.gosa2sur
	FILENAME_LITE = "pointslite.g2s" # *.gosa2sur
	with open(FILENAME, "wb") as file:
		pickle.dump(points, file)