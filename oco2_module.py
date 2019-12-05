# Смысл в чем? Есть фнкция download. Она скачивает НЕ АРХИВЫ, а уже готовые для обработки файлы.
# Так что FromTar нахой не нужон. Скачивание работает и конверт чуть-чуть (выписывает список файлов в текстовик)
# Осталось разобраться с netCDF4, но он не сложный https://github.com/Unidata/netcdf4-python/blob/master/examples/reading_netCDF.ipynb
#
# Ниже пример который выводит ширину, долготу и значение в консоль, так что ничего сложного не должно быть
#
# import netCDF4
#
# f = netCDF4.Dataset('oco2_LtCO2_140906_B9003r_180927215925s.nc4')
# 
# lon = f.variables['longitude'] 
# lat = f.variables['latitude']
# co2 = f.variables['xco2']

# print(len(co2))

# for i in range(len(co2)):
#     print(f"longitude: {lon[i]} latitude: {lat[i]} CO2: {co2[i]}")

#
#

import os, tarfile, netCDF4
from classes import Point

DEBUG = True

def Download(wgetlist: str):
	os.system("wget -i " + wgetlist + " -P oco2/tmp/NC4/")



def Convert():
	if not os.path.exists("oco2/Data"):
		os.makedirs("oco2/Data")
	os.system("rm oco2/tmp/nc4list.txt")
	os.system("ls oco2/tmp/NC4/ >> oco2/tmp/nc4list.txt")

	with open("oco2/tmp/nc4list.txt") as file:
		nc4_l = [row.strip() for row in file]

	tmp = []
	prev_date = None

	for nc4 in nc4_l:
		f = netCDF4.Dataset('oco2/tmp/NC4/' + nc4)
		lon = f.variables['longitude'] 
		lat = f.variables['latitude']
		co2 = f.variables['xco2']
		date = f.variables['date']

		
		with open(f'oco2/data/{date[0][0]:4d}-{date[0][1]:02d}-{date[0][2]:02d}.json', 'a+') as f:
			f.write("[\n")
			for i in range(len(co2)):
				f.write(str(Point(lon[i], lat[i], date[i][0], co2[i])))
				if i != len(co2)-1:
					f.write(',\n')
			f.write("]")

		

		 

		
				

