import requests
import shutil
import os
import time
#os.chmod("/var/www/html/SSN/Download", 0o0777)

shutil.rmtree("/var/www/html/Wilcox_SFS/Download")
os.umask(0)
os.makedirs("/var/www/html/Wilcox_SFS/Download",0o0777)
#os.mkdir("/var/www/html/SSN/Download")
m =int(time.strftime('%m'))
d =int(time.strftime('%d'))
shutil.copy("/var/www/html/Wilcox_SFS/SFS.root",time.strftime('/var/www/html/Wilcox_SFS/Download/SPFS_'+str(m)+'-'+str(d)+'-'+'%Y.root'))
