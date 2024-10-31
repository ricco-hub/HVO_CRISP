import requests
import shutil
import os
import time

# os.chmod("/var/www/html/SSN/Download", 0o0777)

shutil.rmtree("/var/www/html/NeutronMonitor_Rate/Download")
os.umask(0)
os.makedirs("/var/www/html/NeutronMonitor_Rate/Download", 0o0777)
# os.mkdir("/var/www/html/SSN/Download")
m = int(time.strftime("%m"))
d = int(time.strftime("%d"))
shutil.copy(
    "/var/www/html/NeutronMonitor_Rate/Monitor_Rate.root",
    time.strftime(
        "/var/www/html/NeutronMonitor_Rate/Download/NM_"
        + str(m)
        + "-"
        + str(d)
        + "-"
        + "%Y.root"
    ),
)
