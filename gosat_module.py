import h5py, pickle, os, sys, tarfile
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

def Download():
	os.system("wget -i wgetlist.txt -P archives/ --http-user=tarangok@yandex.ru --http-passwd=GPOtusur19 ")

def FromTar():
	os.system("ls archives/ >> archiveslist.txt")
	with open("archiveslist.txt") as file:
		array = [row.strip() for row in file]
	for tr in array:
		tr = 'archives/'+tr
		tar = tarfile.open(tr, "r")
		tar.extractall()
	os.remove("archiveslist.txt")

def Convert(file_type):
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

		
		return points


	os.system("rm hdflist.txt")
	os.system("rm points.g2s")
	os.system("ls SWIRL2CO2/ >> hdflist.txt")

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

	date = ''
	preDate = ''
	for p in g2s:
		preDate = date
		date = p.GetT()[0:7]
		f = open('' + date + '.json', 'a+')
		f.write( '{\n"type": "Feature",\n"geometry": ' + str( geoPoint( ( float( p.GetY() ), float( p.GetX() ) )) ) + ',\n"properties": {\n"value":'+str(p.GetV())+'}\n},\n')
		i += 1
	