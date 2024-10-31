import requests
import os
import time
from DECIMAL import decimal_year
import shutil

# scarico il mese corrente completo

url = "http://www.sidc.be/silso/DATA/EISN/EISN_current.txt"
r = requests.get(url, allow_redirects=True)
open("/var/www/html/SSN/SSN_current.txt", "wb").write(r.content)


# carico vecchio storico
with open("/var/www/html/SSN/SSN_ALL.txt", "r") as infile:
    linesALL = infile.readlines()
al = linesALL  # numero righe di ALL

# carico righe del mese corrente
with open("/var/www/html/SSN/SSN_current.txt", "r") as infile:
    linesCURR = infile.readlines()
cur = linesCURR  # numero righe di current


# eliminazione righe già inserite
# viene appeso tutto il monthly ogni volta per includere correzioni sporadiche di SILSO
sl = cur[0].split()


for i in range(len(al) - 1, -1, -1):
    cur_split = cur[0].split()
    al_split = al[i].split()

    if (
        al_split[0] == cur_split[0]
        and al_split[1] == cur_split[1]
        and al_split[2] == cur_split[2]
    ):
        print(al[i])
        for j in range(i, len(al)):
            del al[j : len(al)]


# remove line from ALL txt
with open("/var/www/html/SSN/SSN_ALL.txt", "w") as f:
    for i in range(len(al)):
        f.write(al[i])


# merging
filenames = ["/var/www/html/SSN/SSN_ALL.txt", "/var/www/html/SSN/SSN_current.txt"]
with open("/var/www/html/SSN/SSN_Hist.txt", "w+") as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
                print(line)

shutil.copyfile("/var/www/html/SSN/SSN_Hist.txt", "/var/www/html/SSN/SSN_ALL.txt")

# riordinamento txt per SSN

import re

infile = open("/var/www/html/SSN/SSN_Hist.txt", "r")
outfile = open("/var/www/html/SSN/SSN.txt", "w")
column1 = 3
column2 = 4
column3 = 5

lines = infile.readlines()
new = lines
for i in range(len(new)):
    sline = lines[i].split()
    outfile.write(str(decimal_year(int(sline[0]), int(sline[1]), int(sline[2]))) + " ")
    outfile.write(sline[column2] + " ")
    outfile.write("0" + " ")
    outfile.write(sline[column3] + "\n")

infile.close()
outfile.close()
