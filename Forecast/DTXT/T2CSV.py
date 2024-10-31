import requests
import os
import time
import shutil
from zipfile import ZipFile

os.remove("ForceField_csv.zip")

z = ZipFile("ForceField_csv.zip", "w")


with open("/var/www/html/Forecast/NM_Set.txt", "r") as infile:
    kind2 = infile.readlines()

for i in range(len(kind2)):
    kind = kind2[i].split()
    print(kind[0])
    z.write(kind[0] + "PHI.csv")
    z.write("JMOD" + kind[0] + ".csv")

"""
 if(kind[0] =='1' or kind[0] =='2'):
  print("1 or 2")
  z.write("SSN_range.txt")
 # z.write("/var/www/html/SSN/DTXT/SSN_range.txt")
 if(kind[0] == '3' or kind[0] == '4'):
  print("3 or 4")
  z.write("SSN_Monthly_range.txt")
  #z.write("/var/www/html/SSN/DTXT/SSN_Monthly_range.txt")
 if(kind[0] == '5' or kind[0] == '6'):
   print("5 or 6")
   z.write("SSN_Smooth_range.txt")
   #z.write("/var/www/html/SSN/DTXT/SSN_Smooth_range.txt")
"""
z.close()
# os.mkdir("/var/www/html/SSN/DTXT/Davidinho")
