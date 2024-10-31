import requests                 
import shutil
import datetime
import os
import time
from DECIMAL import decimal_year
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from import2 import simple_get

now = datetime.datetime.now()
#------------------NM Station----------
with open('/var/www/html/NeutronMonitor_Rate/NMStations.txt') as fp:
   line = fp.readline()

stat = line.split()
#print(stat)
with open('/var/www/html/NeutronMonitor_Rate/Resolution.txt') as fp2:
   lineres = fp2.readline()
res = lineres.split()
#print(res)

with open('/var/www/html/NeutronMonitor_Rate/ResT.txt') as fp3:
   linet = fp3.readline()
title = linet.split()
#print(title[0])




#stat contiene i nomi delle stazioni
for w in range(len(res)):
 for i in range(len(stat)):
  print(stat[i])
  print(res[w])
  print(title[w])
  NM = "http://www.nmdb.eu/nest/draw_graph.php?formchk=1&stations[]="+stat[i]+"&tabchoice=1h&dtype=corr_for_efficiency&tresolution="+res[w]+"&yunits=0&date_choice=bydate&start_day=1&start_month=1&start_year=1960&start_hour=0&start_min=0&end_day=4&end_month=12&end_year=2019&end_hour=23&end_min=59&output=ascii"
  year = str(now.year)
  month = str(now.month)
  day = str(now.day)
 # print(year+month+day)
  NM = NM.replace("end_year=2019","end_year="+year)
  NM= NM.replace("end_month=12","end_month="+month)
  NM= NM.replace("end_day=4","end_day="+day)
  url = simple_get(NM)
 # print(NM)
  html = BeautifulSoup(url, 'html.parser')
  path = "/var/www/html/NeutronMonitor_Rate/"+stat[i]+title[w]+".txt"
 

  f = open(path, "w")
  for i, pre in enumerate(html.select('pre')):
    f.write("%s" %(pre.text))
  f.close()

#elimino righe inutili
  lines1 = tuple(open(path, "r"))
  print(lines1[0])
  print(lines1[24])
  print(lines1[25])
  with open(path, "w") as file:
   for i in range(len(lines1)):
     if i > 24:
        file.write(lines1[i])
#su Oulu.txt ho scaricato i dati correnti devo confrontarli con Oulu.txt storico

  lines1 = tuple(open(path, "r"))

    
  file = open(path, "w")
 
  for j in range(len(lines1)):
   sline = lines1[j].split()
   if len(sline) == 2:
     year  = int(lines1[j][0]+lines1[j][1]+lines1[j][2]+lines1[j][3])
     month = int(lines1[j][5]+lines1[j][6])
     day   = int(lines1[j][8]+lines1[j][9])
     value = sline[1][9]
     for i in range(10,len(sline[1])):
        value += sline[1][i]
     a = str(decimal_year(year,month,day))
     file.write(a + "  " + value + "\n")

   if len(sline) != 2:
     year  = int(lines1[j][0]+lines1[j][1]+lines1[j][2]+lines1[j][3])
     month = int(lines1[j][5]+lines1[j][6])
     day   = int(lines1[j][8]+lines1[j][9])
     a = str(decimal_year(year,month,day))
     file.write(a + "  " + sline[2] + "\n")

