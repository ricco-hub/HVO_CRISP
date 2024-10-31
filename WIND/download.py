import requests
import shutil
import os
import time

shutil.rmtree("/var/www/html/WIND/Download")
os.mkdir("/var/www/html/WIND/Download")
m = int(time.strftime("%m"))
d = int(time.strftime("%d"))
shutil.copy(
    "/var/www/html/WIND/Graph/SolarWind.root",
    time.strftime(
        "/var/www/html/WIND/Download/SolarWind_"
        + str(m)
        + "-"
        + str(d)
        + "-"
        + "%Y.root"
    ),
)
