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
	os.system("wget -i " + wgetlist + " -P OCO2/tmp/NC4/")



def Convert():
	if not os.path.exists("OCO2/Data"):
		os.makedirs("OCO2/Data")

	nc4_l = os.listdir('OCO2/tmp/NC4/')

	for nc4 in nc4_l:
		with netCDF4.Dataset('OCO2/tmp/NC4/' + nc4) as f:
			lon_l = f.variables['longitude'] 
			lat_l = f.variables['latitude']
			co2_l = f.variables['xco2']
			date_l = f.variables['date']

			
		with open(f'OCO2/Data/{date_l[0][0]:4d}-{date_l[0][1]:02d}-{date_l[0][2]:02d}.json', 'w') as f:
			f.write("[\n")
			for i in range(len(co2_l)):
				f.write(str(Point(lon_l[i], lat_l[i], date_l[i][0], co2_l[i])))
				if i != len(co2_l)-1:
					f.write(',\n')
			f.write(']')

		

		 

		
				

