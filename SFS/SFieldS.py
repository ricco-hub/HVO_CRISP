import requests
import shutil
import os
from DECIMAL import decimal_year
import time
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from mathematicians import simple_get


url = simple_get("http://wso.stanford.edu/Polar.html")
html = BeautifulSoup(url, 'html.parser')
f = open('/var/www/html/SFS/SFieldS.txt', "w")
for i, pre in enumerate(html.select('pre')):
    f.write("%s" %(pre.text))
#lo script importa i dati - tabelle complete - e le salva con la data attuale

#elimino la prima riga per avere un format diviso in colonne
lines1 = tuple(open('/var/www/html/SFS/SFieldS.txt', "r"))
with open(time.strftime('/var/www/html/SFS/SFieldS.txt'), "w+") as file:
 for i in range(len(lines1)):
    if i > 2:
        file.write(lines1[i])

#ho otteuto il file completo txt


'''
#creo il file SFSN.txt converto date in julian date
lines1 = tuple(open('/var/www/html/SFS/SFieldS.txt', "r"))
filen = open('/var/www/html/SFS/SFSNorth.txt', "w")
files = open('/var/www/html/SFS/SFSSouth.txt', "w")
filea =  open('/var/www/html/SFS/SFSAvg.txt', "w")
filenf = open('/var/www/html/SFS/SFSNf.txt', "w")
filesf =  open('/var/www/html/SFS/SFSSf.txt', "w")
fileaf =  open('/var/www/html/SFS/SFSAvgf.txt', "w")

print(lines1)

#inizio dei cici for per importare i corretti valori per i grafici
for j in range(1550):
   year  = int(lines1[j][0]+lines1[j][1]+lines1[j][2]+lines1[j][3])
   print(len(lines1[0]))
   month = int(lines1[j][5]+lines1[j][6])
   day   = int(lines1[j][8]+lines1[j][9])
   sline = lines1[j].split()
   sline[1] = sline[1].replace("N","")
   #sline[2] = sline[2].replace(sline[2][len(sline[2])-1],"")
   sline[2] = sline[2].replace("S","")
   sline[3] = sline[3].replace("A","")
   sline[3] = sline[3].replace("v","")
   sline[3] = sline[3].replace("g","")
#grafico filtrato 20nhz
   sline[6] = sline[6].replace("N","")
   sline[6] = sline[6].replace("f","")
   sline[7] = sline[7].replace("S","")
   sline[7] = sline[7].replace("f","")
   sline[8] = sline[8].replace("A","")
   sline[8] = sline[8].replace("v","")
   sline[8] = sline[8].replace("g","")
   sline[8] = sline[8].replace("f","")
   #print(str(decimal_year(year,month,day)))
   a = str(decimal_year(year,month,day)
 
