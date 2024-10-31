import requests
import shutil
import os
import time

# os.chmod("/var/www/html/SSN/Download", 0o0777)

shutil.rmtree("/var/www/html/SSN/Download")
os.umask(0)
os.makedirs("/var/www/html/SSN/Download", 0o0777)
# os.mkdir("/var/www/html/SSN/Download")
m = int(time.strftime("%m"))
d = int(time.strftime("%d"))
shutil.copy(
    "/var/www/html/SSN/SSN.root",
    time.strftime(
        "/var/www/html/SSN/Download/SSN_" + str(m) + "-" + str(d) + "-" + "%Y.root"
    ),
)
