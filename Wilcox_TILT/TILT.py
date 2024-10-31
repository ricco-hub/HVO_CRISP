import requests
import shutil
import os
import time
from DECIMAL import decimal_year
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from import2  import simple_get
#cancellare vecchio salvataggio in Download e aggiornare file con data


url = simple_get("http://wso.stanford.edu/Tilts.html")
html = BeautifulSoup(url, 'html.parser')
f = open(time.strftime('/var/www/html/Wilcox_TILT/tilt.txt'), "w")
for i, pre in enumerate(html.select('pre')):
    f.write("%s" %(pre.text))
#lo script importa i dati - tabelle complete - e le salva con la data attuale


#elimino la prima riga per avere un format diviso in colonne
lines1 = tuple(open(time.strftime('/var/www/html/Wilcox_TILT/tilt.txt'), "r"))
with open(time.strftime('/var/www/html/Wilcox_TILT/tilt.txt'), "w+") as file:
 for i in range(len(lines1)):
    if i > 1:
        file.write(lines1[i])

#ho otteuto il file completo txt
#creo il file SFSN.txt converto date in julian date
lines1 = tuple(open(time.strftime('/var/www/html/Wilcox_TILT/tilt.txt'), "r"))
fileRav = open(time.strftime('/var/www/html/Wilcox_TILT/Tilt_R_av.txt'), "w")
fileRn =  open(time.strftime('/var/www/html/Wilcox_TILT/Tilt_R_n.txt'), "w")
fileRs =  open(time.strftime('/var/www/html/Wilcox_TILT/Tilt_R_s.txt'), "w")
fileLav = open(time.strftime('/var/www/html/Wilcox_TILT/Tilt_L_av.txt'), "w")
fileLn =  open(time.strftime('/var/www/html/Wilcox_TILT/Tilt_L_n.txt'), "w")
fileLs =  open(time.strftime('/var/www/html/Wilcox_TILT/Tilt_L_s.txt'), "w")
lines2 = tuple(open(time.strftime('/var/www/html/Wilcox_TILT/Tilt_L_s.txt'), "r"))


#splitto in colonne le varie righe
for j in range(len(lines1)):
   sline = lines1[j].split()
   year  = int(sline[2][0]+sline[2][1]+sline[2][2]+sline[2][3])
   month = int(sline[2][5]+sline[2][6])
   day   = int(sline[2][8]+sline[2][9])
   print(str(decimal_year(year,month,day)))
   a = str(decimal_year(year,month,day))
   fileRav.write(a + "  " + sline[4] + "\n")
   fileRn.write(a  + "  " + sline[5] + "\n")
   fileRs.write(a  + "  " + sline[6] + "\n")
   fileLav.write(a + "  " + sline[7] + "\n")
   fileLn.write(a  + "  " + sline[8] + "\n")
   fileLs.write(a  + "  " + sline[9] + "\n")
#chiudo e salvo file
f.close()
fileRav.close()
fileRn.close()
fileRs.close()
fileLav.close()
fileLn.close()
fileLs.close()
