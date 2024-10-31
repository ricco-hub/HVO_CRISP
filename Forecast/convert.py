import requests
import shutil
import os
import time
from DECIMAL import decimal_year
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

# cancellare vecchio salvataggio in Download e aggiornare file con data

# ho otteuto il file completo txt

# converto date in julian dat

lines1 = tuple(open("Etime.txt", "r"))
n1 = len(lines1)

f = open("Etime.txt", "w")

# inizio dei cici for per importare i corretti valori per i grafici
for j in range(n1):
    year = int(lines1[j][0] + lines1[j][1] + lines1[j][2] + lines1[j][3])
    month = int(lines1[j][5] + lines1[j][6])
    day = int(lines1[j][8] + lines1[j][9])
    print(str(decimal_year(year, month, day)))
    a = str(decimal_year(year, month, day))
    f.write(a + "\n")
# chiudo e salvo file
f.close()
