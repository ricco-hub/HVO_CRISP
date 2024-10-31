import requests
import os
import time
import shutil
from zipfile import ZipFile

os.remove("Tilt.zip")

z = ZipFile("Tilt.zip", "w")


with open("/var/www/html/Wilcox_TILT/Set.txt", "r") as infile:
    kind2 = infile.readlines()

for i in range(len(kind2)):
    kind = kind2[i].split()
    if kind[0] == "1":
        z.write("Tilt_L_av.txt")

    if kind[0] == "2":
        z.write("Tilt_L_n.txt")

    if kind[0] == "3":
        z.write("Tilt_L_s.txt")

    if kind[0] == "4":
        z.write("Tilt_R_av.txt")
    if kind[0] == "5":
        z.write("Tilt_R_n.txt")

    if kind[0] == "6":
        z.write("Tilt_R_s.txt")

z.close()
# os.mkdir("/var/www/html/SSN/DTXT/Davidinho")
