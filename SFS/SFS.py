import requests
import shutil
import os
from DECIMAL import decimal_year
import time
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from mathematicians import simple_get


url = simple_get("http://wso.stanford.edu/Polar.html")
html = BeautifulSoup(url, 'html.parser')
f = open('/var/www/html/SFS/SFS.txt', "w")
for i, pre in enumerate(html.select('pre')):
    f.write("%s" %(pre.text))

