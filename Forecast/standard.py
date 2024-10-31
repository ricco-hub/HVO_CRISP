import requests
import shutil
from DECIMAL import decimal_year
import os
import time

m = int(time.strftime("%m"))
d = int(time.strftime("%d"))
Y = int(time.strftime("%Y"))

with open("/var/www/html/Forecast/Etime.txt", "w") as f:
    f.write("1980.001")
    f.write("\n")
    f.write(str(decimal_year(Y, m, d)))


with open("/var/www/html/Forecast/NM_Set.txt", "w") as g:
    g.write("OULU\n")
    g.write("NEWK\n")
    g.write("APTY\n")
    g.write("JUNG")
