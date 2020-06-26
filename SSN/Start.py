import requests
import os
import time
import shutil

url = 'http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt'
r = requests.get(url, allow_redirects=True)
#scarico storico
open('SSN_ALL.txt', 'wb').write(r.content)

line = tuple(open(time.strftime('SSN_ALL.txt'), "r"))
a = line

error = -1

with open(time.strftime('SSN_ALL.txt'), "w") as file:
 for j in range(len(a)):
   sline = a[j].split()
   if not  sline[4] == '-1' or sline[4] == '-1.0':
        file.write(a[j])
