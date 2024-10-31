import requests
import os
import time
import shutil
import re
from DECIMAL import decimal_year

url = 'http://www.sidc.be/silso/DATA/SN_m_tot_V2.0.txt'
r = requests.get(url, allow_redirects=True)
open('/var/www/html/SSN/SSN_Monthly.txt', 'wb').write(r.content)
#scrivo monthly

line = tuple(open(time.strftime('/var/www/html/SSN/SSN_Monthly.txt'), "r"))
monthly = line

with open(time.strftime('/var/www/html/SSN/SSN_Monthly.txt'), "w") as file:
 for j in range(len(monthly)):
   sline = monthly[j].split()
   if not sline[3] == '-1' or sline[3] == '-1.0':    #non stampo i valori non disponibili che SILSO indica con -1 o -1.0
        file.write(monthly[j])
#monthly completed

url3 = 'http://sidc.oma.be/silso/DATA/SN_y_tot_V2.0.txt'
r3 = requests.get(url3, allow_redirects=True)
open('/var/www/html/SSN/SSN_Y.txt', 'wb').write(r3.content)
#scrivoyear                                                                                                                        
line = tuple(open(time.strftime('/var/www/html/SSN/SSN_Y.txt'), "r"))
smooth = line
with open(time.strftime('/var/www/html/SSN/SSN_Y.txt'), "w") as file:
 for j in range(len(smooth)):
   sline = smooth[j].split()
   if not sline[1] == '-1.0' or sline[1] == '-1':  #non stampo i valori non disponibili che SILSO indica con -1 o -1.0                   
     file.write(smooth[j])
#smooth completed   

#fine 

url2 = 'http://www.sidc.be/silso/DATA/SN_ms_tot_V2.0.txt'
r2 = requests.get(url2, allow_redirects=True)
open('/var/www/html/SSN/SSN_13.txt', 'wb').write(r2.content)
#scrivo smoothed


line = tuple(open(time.strftime('/var/www/html/SSN/SSN_13.txt'), "r"))
smooth = line
with open(time.strftime('/var/www/html/SSN/SSN_13.txt'), "w") as file:
 for j in range(len(smooth)):
   sline = smooth[j].split()
   if not sline[3] == '-1.0' or sline[3] == '-1':  #non stampo i valori non disponibili che SILSO indica con -1 o -1.0
     file.write(smooth[j])
#smooth completed

day = 15


#creare subito il database da cui fare il grafico
import re
line = tuple(open(time.strftime('/var/www/html/SSN/SSN_13.txt'), "r"))

with open(time.strftime('/var/www/html/SSN/SSN_13.txt'), "w") as outfile:
 for j in range(len(line)):
   sline = line[j].split()
   outfile.write(str(decimal_year(int(sline[0]),int(sline[1]),day)) + ' ')
   outfile.write(sline[3] + ' ')
   if sline[4] == '-1.0' or sline[4] == '-1':   #stampo 0 se non sono disponibili gli errori che SILSO indica con -1 o -1.0 
      outfile.write('0' + ' '+'0 ' +'\n')
   else: outfile.write('0' + ' ' +sline[4] + ' '+'\n')

outfile.close()



import re
line = tuple(open(time.strftime('/var/www/html/SSN/SSN_Monthly.txt'), "r"))

with open(time.strftime('/var/www/html/SSN/SSN_Monthly.txt'), "w") as outfile2:
  for j in range(len(line)):
   sline = line[j].split()
   outfile2.write(str(decimal_year(int(sline[0]),int(sline[1]),day)) + ' ')
   outfile2.write(sline[3] + ' ')
   if sline[4] == '-1.0' or sline[4] == '-1':  #stampo 0 se non sono disponibili gli errori che SILSO indica con -1 o -1.0 
      outfile2.write('0' + ' '+'0 ' +'\n')
   else: outfile2.write('0' + ' ' +sline[4] + ' '+'\n')

outfile2.close()


import re
line = tuple(open(time.strftime('/var/www/html/SSN/SSN_Y.txt'), "r"))

with open(time.strftime('/var/www/html/SSN/SSN_Y.txt'), "w") as outfile3:
  for j in range(len(line)):
   sline = line[j].split()
  # outfile2.write(str(decimal_year(int(sline[0]),int(sline[1]),day)) + ' ')
   outfile3.write(sline[0] + ' ')
   outfile3.write(sline[1] + ' ')
   if sline[2] == '-1.0' or sline[2] == '-1':  #stampo 0 se non sono disponibili gli errori che SILSO indica con -1 o -1.0                                                
      outfile3.write('0' +' '+ '0'+'\n')
   else: outfile3.write('0' + ' ' +sline[2] + ' '+'\n')

outfile3.close()  
