import requests
import os
import time
import shutil
from zipfile import ZipFile

os.remove("Wind_csv.zip")

z = ZipFile("Wind_csv.zip", "w")


with open("/var/www/html/WIND/Set.txt", "r") as infile:
    kind2 = infile.readlines()

for i in range(len(kind2)):
    kind = kind2[i].split()
    if kind[0] == "1":
        print("1")
        z.write("Speed_range.csv")
    # z.write("/var/www/html/SSN/DTXT/SSN_range.txt")
    if kind[0] == "2":
        print("2")
        z.write("Proton_range.csv")

z.close()
# os.mkdir("/var/www/html/SSN/DTXT/Davidinho")
