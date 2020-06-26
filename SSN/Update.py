import requests
import os
import time
import shutil
#scarico il mese corrente completo
url = 'http://www.sidc.be/silso/DATA/EISN/EISN_current.txt'
r = requests.get(url, allow_redirects=True)
open('/var/www/html/SSN/SSN_current.txt', 'wb').write(r.content)


#cancello vecchio append
with open("/var/www/html/SSN/SSN_ALL.txt", "r") as infile:
    linesALL = infile.readlines()
al = linesALL #numero righe di ALL

with open("/var/www/html/SSN/SSN_current.txt", "r") as infile:
    linesCURR = infile.readlines()
cur = linesCURR #numero righe di current 

#eliminazione righe già inserite
#viene appeso tutto il monthly ogni volta per includere correzioni sporadiche di SILSO
for i in range(len(al)-1,-1,-1):
    if al[i] == cur[0]:
     for j in range(i,len(al)):
      del al[j:len(al)]
    

#remove line from ALL txt
with open("/var/www/html/SSN/SSN_ALL.txt", "w") as f:
    for i  in range(len(al)):
     f.write(al[i])
     
#merging
filenames = ['/var/www/html/SSN/SSN_ALL.txt', '/var/www/html/SSN/SSN_current.txt']
with open('/var/www/html/SSN/SSN_Hist.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

shutil.copyfile("/var/www/html/SSN/SSN_ALL.txt", "/var/www/html/SSN/SSN_Hist.txt")

#riordinamento txt per SSN con errore e senza errore

import re
infile = open ('/var/www/html/SSN/SSN_Hist.txt', 'r')
outfile = open ('/var/www/html/SSN/SSN.txt', 'w')
column1 = 3
column2 = 4
column3 = 5

lines = infile.readlines()
new = lines
for i in range(len(new)):
        sline = lines[i].split()
        outfile.write(sline[column1] + ' ')
        outfile.write(sline[column2] + ' ')
        outfile.write('0' + ' ')
        outfile.write(sline[column3] + '\n')

infile.close()
outfile.close()
