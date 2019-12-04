import h5py, os, sys, tarfile

from classes import Point
	


def Check():
    pass

def Download(wgetlist: str):
	os.system("wget -i " + wgetlist + " -P gosat/tpm/archives/ --http-user=tarangok@yandex.ru --http-passwd=GPOtusur19 ")

def FromTar():
	os.system("ls gosat/tmp/archives/ >> gosat/tmp/archiveslist.txt")
	with open("gosat/tmp/archiveslist.txt") as file:
		array = [row.strip() for row in file]
	for tr in array:
		tr = 'archives/'+tr
		tar = tarfile.open(tr, "r")
		tar.extractall()
	os.remove("gosat/tmp/archiveslist.txt")

def Convert():
	os.system("rm hdflist.txt")
	#os.system("rm points.g2s")
	os.system("ls gosat/tmp/SWIRL2CO2/ >> hdflist.txt")

	with open("hdflist.txt") as file:
		array = [row.strip() for row in file]

	countFiles = len(array)
	j = 1
	tmplist = []
	tmplist.append("FirstValue")
	points = dict()
	dict_str = 'FirstKey'
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
		
		#print("dict_str", dict_str)
		for i in range(0, numScan):
			if dict_str == timeList[i].decode("utf-8")[0:7]:
				#print(timeList[i].decode("utf-8")[0:7], "!")
				
				tmplist.append( Point ( longitudeList[i], latitudeList[i], timeList[i].decode("utf-8"), valueList[i] ))
			else:
				if dict_str != 'FirstKey':
					points[str(dict_str)] = list(tmplist)
				tmplist.clear()
				dict_str = timeList[i].decode("utf-8")[0:7]
				tmplist.append( Point ( longitudeList[i], latitudeList[i], timeList[i].decode("utf-8"), valueList[i] ))
		points[str(dict_str)] = list(tmplist)
	
	

	
	for key in points.keys():
		i = 1
		f = open('' + key + '.json', 'a+')
		f.write("[\n")
		for p in points[key]:

			f.write(str(p))
			if i != len(points[key]): 
				f.write(',')

			i += 1
		f.write("]")