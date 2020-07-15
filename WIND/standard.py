import requests
import shutil
from SETDATE import fractional
import os
import time

m =int(time.strftime('%m'))
d =int(time.strftime('%d'))
Y =int(time.strftime('%Y'))

with open("/var/www/html/WIND/E.txt", "w") as f:
 f.write('1990.')
 f.write("\n")
 f.write(str(fractional(Y,m,d)))


with open("/var/www/html/WIND/Set.txt", "w") as g:
 g.write('1')
 g.write('2')



