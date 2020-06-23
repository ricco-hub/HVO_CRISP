import requests
import shutil
import os
import time

shutil.rmtree("/var/www/html/WIND/Download")
os.mkdir("/var/www/html/WIND/Download")
m =int(time.strftime('%m'))
d =int(time.strftime('%d'))
shutil.copy("/var/www/html/WIND/WIND-DENSITY.root",time.strftime('/var/www/html/WIND/Download/WIND-DENSITY_'+str(m)+'-'+str(d)+'-'+'%Y.root'))
