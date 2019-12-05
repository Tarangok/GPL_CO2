import h5py, os, sys, tarfile

from classes import Point
	
DEBUG = True


def Check():
    pass

def Download(wgetlist: str):
	os.system("wget -i " + wgetlist + " -P gosat/tmp/archives/ --http-user=tarangok@yandex.ru --http-passwd=GPOtusur19 ")

def FromTar(path_to_archives, path_to_extract):
	
	archives_list = os.listdir(path_to_archives)
	
	for archive in archives_list:
		archive = path_to_archives + archive
		tar = tarfile.open(archive, "r")
		tar.extractall(path=path_to_extract)
		tar.close()

		if not DEBUG:
			os.remove(archive)
	return archives_list

def Convert():
	if not os.path.exists("gosat/Data"):
		os.makedirs("gosat/Data")

	array = os.listdir('gosat/tmp/HDF/SWIRL2CO2/')

	countFiles = len(array)
	j = 1
	tmplist = []
	tmplist.append("FirstValue")
	points = dict()
	dict_str = 'FirstKey'


	k = 0

	for hdfFile in array:
		

		with h5py.File("gosat/tmp/HDF/SWIRL2CO2/" + hdfFile, 'r') as f:
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
		
		with open('gosat/Data' + timeList[k].decode("utf-8")[0:7] + '.json', 'a+') as f:
			f.write('[\n')
			for i in range(numScan):
				f.write(str(Point(longitudeList[i], latitudeList[i], timeList[i], valueList[i] )))
				if i != len(points[key]): 
					f.write(',')
				f.write(']')
				
				
		
	
	

	
	# for key in points.keys():
	# 	i = 1
	# 	f = open('gosat/data/' + key + '.json', 'a+')
	# 	f.write("[\n")
	# 	for p in points[key]:

	# 		f.write(str(p))
	# 		if i != len(points[key]): 
	# 			f.write(',')

	# 		i += 1
	# 	f.write("]")