import requests
import os
import time
import shutil
import datetime 


open('/var/www/html/SSN/SSN_Hist.txt', 'w').close()
current_time = datetime.datetime.now()  

if(current_time.day != 1 and current_time.day != 2):
 url = 'http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt'
 r = requests.get(url, allow_redirects=True)
 #scarico storico
 open('/var/www/html/SSN/SSN_ALL.txt', 'wb').write(r.content)

 line = tuple(open(time.strftime('SSN_ALL.txt'), "r"))
 a = line

 error = -1

#dallo storico elimino le righe in cui non si hanno dati mancanti che inSILSO vengono indicati con '-1'
 with open(time.strftime('SSN_ALL.txt'), "w") as file:
  for j in range(len(a)):
   sline = a[j].split()
   if not  sline[4] == '-1' or sline[4] == '-1.0':
        file.write(a[j])
