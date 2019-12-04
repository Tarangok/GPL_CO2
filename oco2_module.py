import os, tarfile
from classes import Point

DEBUG = True

def FromTar(path_to_archives, path_to_extract):
	
	archives_list = os.listdir(path_to_archives)
	
	for archive in archives_list:
		archive = path_to_archives + archive
		tar = tarfile.open(archive, "r")
		tar.extractall(path=path_to_extract)
		tar.close()

		if not DEBUG:
			os.remove(archive)

