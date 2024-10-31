import requests
import os
import time
import shutil

# begin

# smoothed13
file4 = open("/var/www/html/SSN/DTXT/SSN_Smooth_range.txt", "w")
file4.write(
    "MONTHLY SMOOTHED SUNSPOT NUMBER DATA downloaded from HVO: \ncolumn 1 - Date in fraction of year. \ncolumn 2 - Monthly smoothed total sunspot number.\ncolumn 3 - Monthly mean standard deviation of the input sunspot numbers.\n\n"
)

with open("/var/www/html/SSN/data_PLOT/SSN_Smooth_range.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
        sline = SSN_all[i].split()
        print(sline)
        file4.write("%8.3f" % (float(sline[0])))
        file4.write("\t" + str(float(sline[1])))
        file4.write("\t" + str(float(sline[3])) + "\n")


# yearly
file4 = open("/var/www/html/SSN/DTXT/SSN_Year_range.txt", "w")
file4.write(
    "YEARLY SUNSPOT NUMBER DATA downloaded from HVO: \ncolumn 1 - Date in fraction of year. \ncolumn 2 - Yearly total sunspot number.\ncolumn 3 - Yearly mean standard deviation of the input sunspot numbers.\n\n"
)

with open("/var/www/html/SSN/data_PLOT/SSN_Yearly_range.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
        sline = SSN_all[i].split()
        print(sline)
        file4.write("%8.3f" % (float(sline[0])))
        file4.write("\t" + str(float(sline[1])))
        file4.write("\t" + str(float(sline[3])) + "\n")


# file4.write('%8.3f   %8.3f    %8.3f'   % (float(sline[0]), float(sline[1]), float(sline[3])))
#  file4.write("\n")

# daily
file4 = open("/var/www/html/SSN/DTXT/SSN_range.txt", "w")
file4.write(
    "DAILY SUNSPOT NUMBER DATA downloaded from HVO: \ncolumn 1 - Date in fraction of year \ncolumn 2 - Daily total sunspot number. \ncolumn 3 - Daily standard deviation of the input sunspot numbers from individual stations.\n\n"
)
with open("/var/www/html/SSN/data_PLOT/SSN_range.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
        sline = SSN_all[i].split()
        print(sline)
        #  file4.write('%8.3f   %8.3f    %8.3f'   % (float(sline[0]), float(sline[1]), float(sline[3])))
        #  file4.write("\n")
        #   file4.write(round(float(sline[0])) , 3 )
        file4.write("%8.3f" % (float(sline[0])))
        file4.write("\t" + str(float(sline[1])))
        file4.write("\t" + str(float(sline[3])) + "\n")

# monthly
file4 = open("/var/www/html/SSN/DTXT/SSN_Monthly_range.txt", "w")
file4.write(
    "MONTHLY SUNSPOT NUMBER DATA downloaded from HVO: \ncolumn 1 - Date in fraction of year. \ncolumn 2 - Monthly total sunspot number.\ncolumn 3 - Monthly mean standard deviation of the input sunspot numbers from individual stations.\n\n"
)
with open("/var/www/html/SSN/data_PLOT/SSN_Monthly_range.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
        sline = SSN_all[i].split()
        print(sline)
        file4.write("%8.3f" % (float(sline[0])))
        file4.write("\t" + str(float(sline[1])))
        file4.write("\t" + str(float(sline[3])) + "\n")

#  file4.write('%8.3f   %8.3f    %8.3f'   % (float(sline[0]), float(sline[1]), float(sline[3])))
#  file4.write("\n")
