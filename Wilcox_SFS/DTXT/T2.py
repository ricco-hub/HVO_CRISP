import requests
import os
import time
import shutil
from zipfile import ZipFile

os.remove("SPFS.zip")

z = ZipFile("SPFS.zip", "w")


with open("/var/www/html/Wilcox_SFS/Set.txt", "r") as infile:
    kind2 = infile.readlines()

for i in range(len(kind2)):
    kind = kind2[i].split()
    if kind[0] == "1":
        z.write("North_range.txt")

    if kind[0] == "2":
        z.write("North_F_range.txt")

    if kind[0] == "3":
        z.write("South_range.txt")

    if kind[0] == "4":
        z.write("South_F_range.txt")
    if kind[0] == "5":
        z.write("Avg_range.txt")

    if kind[0] == "6":
        z.write("Avg_F_range.txt")

z.close()
# os.mkdir("/var/www/html/SSN/DTXT/Davidinho")
