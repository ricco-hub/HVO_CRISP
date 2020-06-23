import requests
import shutil
import os
import time

shutil.rmtree("/var/www/html/SFS/Download")
os.mkdir("/var/www/html/SFS/Download")
m =int(time.strftime('%m'))
d =int(time.strftime('%d'))

shutil.copy("/var/www/html/SFS/ROOT/SPFS.root",time.strftime('/var/www/html/SFS/Download/SPFS_'+str(m)+'-'+str(d)+'-'+'%Y.root'))
