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

	hdf5_l = os.listdir('gosat/tmp/HDF/SWIRL2CO2/')


	for hdf5 in hdf5_l:

		with h5py.File('gosat/tmp/HDF/SWIRL2CO2/' + hdf5, 'r') as f:
			Data = f['Data']
			geolocation = Data['geolocation']
			longitude = geolocation['longitude']
			latitude = geolocation['latitude']
			scanAttribute = f['scanAttribute']
			mixingRatio = Data['mixingRatio']

			timeList = list(scanAttribute['time'])
			# Значение 
			co2_l = list(mixingRatio['XCO2'])
			lon_l = list( longitude )									
			lat_l = list( latitude )
		
		with open(f'gosat/Data/{timeList[0].decode("utf-8")[:10]}.json', 'w') as f:
			f.write('[\n')
			for i in range(len(co2_l)):
				f.write(str(Point(lon_l[i], lat_l[i], timeList[i], co2_l[i])))
				if i != len(co2_l)-1:
					f.write(',\n')
			f.write(']')