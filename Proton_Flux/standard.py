import requests
import shutil
from DECIMAL import decimal_year
import os
import time

m = int(time.strftime("%m"))
d = int(time.strftime("%d"))
Y = int(time.strftime("%Y"))

with open("/var/www/html/SSN/E.txt", "w") as f:
    f.write("1950.001")
    f.write("\n")
    f.write(str(decimal_year(Y, m, d)))


with open("/var/www/html/SSN/Set.txt", "w") as g:
    g.write("1")
