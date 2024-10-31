import requests
import os
import time
import shutil
from zipfile import ZipFile

os.remove("Tilt_csv.zip")

z = ZipFile("Tilt_csv.zip", "w")


with open("/var/www/html/Wilcox_TILT/Set.txt", "r") as infile:
    kind2 = infile.readlines()

for i in range(len(kind2)):
    kind = kind2[i].split()
    if kind[0] == "1":
        z.write("Tilt_L_av.csv")

    if kind[0] == "2":
        z.write("Tilt_L_n.csv")

    if kind[0] == "3":
        z.write("Tilt_L_s.csv")

    if kind[0] == "4":
        z.write("Tilt_R_av.csv")
    if kind[0] == "5":
        z.write("Tilt_R_n.csv")

    if kind[0] == "6":
        z.write("Tilt_R_s.csv")

z.close()
# os.mkdir("/var/www/html/SSN/DTXT/Davidinho")
