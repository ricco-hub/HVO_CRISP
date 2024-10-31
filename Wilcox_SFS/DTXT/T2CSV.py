import requests
import os
import time
import shutil
from zipfile import ZipFile

os.remove("SPFS_csv.zip")

z = ZipFile("SPFS_csv.zip", "w")


with open("/var/www/html/Wilcox_SFS/Set.txt", "r") as infile:
    kind2 = infile.readlines()

for i in range(len(kind2)):
    kind = kind2[i].split()
    if kind[0] == "1":
        z.write("north.csv")

    if kind[0] == "2":
        z.write("north_f.csv")

    if kind[0] == "3":
        z.write("south.csv")

    if kind[0] == "4":
        z.write("south_f.csv")
    if kind[0] == "5":
        z.write("avg.csv")

    if kind[0] == "6":
        z.write("avg_f.csv")

z.close()
# os.mkdir("/var/www/html/SSN/DTXT/Davidinho")
