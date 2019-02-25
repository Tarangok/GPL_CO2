import tarfile, os

os.system("ls archives/ >> archiveslist.txt")



with open("archiveslist.txt") as file:
    array = [row.strip() for row in file]

for tr in array:
    tr = 'archives/'+tr
    tar = tarfile.open(tr, "r")
    tar.extractall()

os.remove("archiveslist.txt")