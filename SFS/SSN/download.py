import requests
import shutil
import os
import time

shutil.rmtree("/var/www/html/SSN/Download")
os.mkdir("/var/www/html/SSN/Download")
m =int(time.strftime('%m'))
d =int(time.strftime('%d'))
shutil.copy("/var/www/html/SSN/ROOT/SSN.root",time.strftime('/var/www/html/SSN/Download/SSN_'+str(m)+'-'+str(d)+'-'+'%Y.root'))
