import requests
import os
import time
import shutil

# begin

#  speed
file4 = open("/var/www/html/WIND/DTXT/Speed_range.txt", "w")
file4.write(
    "Solar Wind Speed data downloaded from HVO: \ncolumn 1 - Date in fraction of year. \ncolumn 2 - Solar wind speed data [km/s].\n\n"
)

with open("/var/www/html/WIND/data_PLOT/Speed_range.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
        sline = SSN_all[i].split()
        print(sline)
        file4.write("%8.3f   %8.3f" % (float(sline[0]), float(sline[1])))
        file4.write("\n")


#  proton density
file4 = open("/var/www/html/WIND/DTXT/Proton_range.txt", "w")
file4.write(
    "Proton density data downloaded from HVO: \ncolumn 1 - Date in fraction of year. \ncolumn 2 - Proton density data [part/cm^3].\n\n"
)
with open("/var/www/html/WIND/data_PLOT/Proton_range.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
        sline = SSN_all[i].split()
        print(sline)
        file4.write("%8.3f   %8.3f" % (float(sline[0]), float(sline[1])))
        file4.write("\n")
