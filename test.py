#!py/Python-3.8.0
import requests
import os
import time
import shutil

url = 'http://www.sidc.be/silso/DATA/EISN/EISN_current.txt'
r = requests.get(url, allow_redirects=True)
#sovrascrive il mese monthly
open('SSN_Monthly.txt', 'wb').write(r.content)
