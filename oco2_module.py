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
	if not os.path.exists("oco2/data"):
		os.makedirs("oco2/data")
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

		if prev_date == None:
			with open('oco2/data/' + str(date[0][0]) + '-' + str(date[0][1]) + '.js', 'a+') as f_out:
				prev_date = date[0][:1]
				f_out.write("[\n")
				for i in range(len(co2)):
					f_out.write(str(Point(lon[i], lat[i], date[i], co2[i])))
					f_out.write(',')
		elif prev_date == date[0][:1]:
			with open('oco2/data/' + str(date[0][0]) + '-' + str(date[0][1]) + '.js', 'a+') as f_out:
				prev_date = date[0][:1]
				for i in range(len(co2)):
					f_out.write(str(Point(lon[i], lat[i], date[i], co2[i])))
					f_out.write(',')
		else:
			with open('oco2/data/' + str(prev_date[0]) + '-' + str(prev_date[1]) + '.js', 'a+') as f_out:
				f_out.write("]")
			with open('oco2/data/' + date[0][0] + '-' + date[0][1] + '.js', 'a+') as f_out:
				prev_date = date[0][:1]
				f_out.write("[\n")
				for i in range(len(co2)):
					f_out.write(str(Point(lon[i], lat[i], date[i], co2[i])))
					f_out.write(',')
		

		 

		
				

