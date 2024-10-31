import requests
import os
import time
import shutil

# scarico il mese corrente completo

with open("/var/www/html/Forecast/NM_ALL.txt") as fp:
    line = fp.readline()
stat = line.split()

# for each station NM


for i in range(len(stat)):
    file4 = open("/var/www/html/Forecast/DTXT/" + stat[i] + "PHI.txt", "w")
    file4.write(
        "Modulation Potential values downloaded from HVO:\n Starting from "
        + stat[i]
        + " station monthly rate: \ncolumn 1 - Date in fraction of year.\ncolumn 2 - Modulation potential values [MV].\n\n"
    )

    with open("/var/www/html/Forecast/data_PLOT/" + stat[i] + "PHI.txt", "r") as infile:
        SSN_all = infile.readlines()
        for i in range(len(SSN_all)):
            sline = SSN_all[i].split()
            print(sline)
            file4.write("%8.3f" % (float(sline[0])))
            file4.write("\t" + str(float(sline[1])) + "\n")

    #  file4.write('%8.3f  %8.3f' % (float(sline[0]), float(sline[1])))
    #  file4.write("\n")


for i in range(len(stat)):
    file4 = open("/var/www/html/Forecast/DTXT/JMOD" + stat[i] + ".txt", "w")
    file4.write(
        "Differential intensity (J) of cosmic ray (protons) near-Earth values downloaded from HVO:\n Starting from "
        + stat[i]
        + " station monthly rate: \ncolumn 1 - Date in fraction of year.\ncolumn 2 - J values [GeV^-1 m^-2 s^-1 sr^-1].\n\n"
    )

    with open(
        "/var/www/html/Forecast/data_PLOT/JMOD" + stat[i] + ".txt", "r"
    ) as infile:
        SSN_all = infile.readlines()
        for i in range(len(SSN_all)):
            sline = SSN_all[i].split()
            print(sline)
            file4.write("%8.3f" % (float(sline[0])))
            file4.write("\t" + str(float(sline[1])) + "\n")
# file4.write('%8.3f  %8.3f' % (float(sline[0]), float(sline[1])))
#    file4.write("\n")


"""
  ssnr = open("/var/www/html/NeutronMonitor_Rate/DTXT/"+stat[i]+".txt","w")
  with open("/var/www/html/NeutronMonitor_Rate/"+stat[i]+".txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     if(  float(date[0])<= float(sline[0]) <= float(date[1])) :
         ssnr.write('%8.3f  %8.3f'   % (float(sline[0]), float(sline[1])   ))
         ssnr.write('\n')


# ssn monthly
ssnr = open("/var/www/html/SSN/data_PLOT/SSN_Monthly_range.txt","w")
with open("/var/www/html/SSN/SSN_Monthly.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     if(  float(date[0])<= float(sline[0]) <= float(date[1])) :
         ssnr.write('%8.3f   %8.3f   %8.3f  %8.3f'   % (float(sline[0]), float(sline[1]), float(sline[2]), float(sline[3])))
         ssnr.write('\n')

# 13 smoothed
ssnr = open("/var/www/html/SSN/data_PLOT/SSN_Smooth_range.txt","w")
with open("/var/www/html/SSN/SSN_13.txt", "r") as infile:
    SSN_all = infile.readlines()
   # print("123456789")
   # print(len(SSN_all))
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     if(  float(date[0])<= float(sline[0]) <= float(date[1])) :
          ssnr.write('%8.3f   %8.3f   %8.3f  %8.3f'   % (float(sline[0]), float(sline[1]), float(sline[2]), float(sline[3])))
          ssnr.write('\n')
"""

## ***************************************************   txt download download version

"""
file4 = open("/var/www/html/SSN/DTXT/SSN_Smooth_range.txt","w")
file4.write("SUNSPOT NUMBER DATA (Smoothed) downloaded from HVO: \n 1 - Date in fraction of year. \n 2 -  Smoothed sunspot number. \n 3 - Daily standard  deviation of the input sunspot numbers from individual stations.\n\n")
with open("/var/www/html/SSN/data_PLOT/SSN_Smooth_range.txt", "r") as infile:
 SSN_all = infile.readlines()
 for i in range(len(SSN_all)):
  sline = SSN_all[i].split()
  print(sline)
  file4.write('%8.3f   %8.3f    %8.3f'   % (float(sline[0]), float(sline[1]), float(sline[3])))
  file4.write("\n")

file5 = open("/var/www/html/SSN/DTXT/SSN_range.txt","w")
file5.write("SUNSPOT NUMBER DATA downloaded from HVO: \n 1 - Date in fraction of year. \n 2 - Daily total sunspot number. \n 3 - Daily standard deviation of the input sunspot numbers from individual stations. \n \n")
with open("/var/www/html/SSN/data_PLOT/SSN_range.txt", "r") as infile:
 SSN_all = infile.readlines()
print(len(SSN_all))
for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     print(sline[0] + "   " + sline[1] + "   " + sline[2])
     file5.write('%8.3f   %8.3f    %8.3f'   % (float(sline[0]), float(sline[1]), float(sline[3])))
     file5.write('\n')


with open("/var/www/html/SSN/DTXT/SSN_Smooth_range.txt", "r") as i:
 old = i.readlines()
 print(len(old))



file6 = open("/var/www/html/SSN/DTXT/SSN_Monthly_range.txt","w")
file6.write("SUNSPOT NUMBER DATA (monthly) downloaded from HVO: \n 1 - Date in fraction of year. \n 2 - Monthly total sunspot number. \n 3 - Daily standard deviation of the input sunspot numbers from individual stations. \n \n")
with open("/var/www/html/SSN/data_PLOT/SSN_Monthly_range.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     file6.write('%8.3f   %8.3f    %8.3f'   % (float(sline[0]), float(sline[1]), float(sline[3])))
     file6.write('\n')


#os.mkdir("/var/www/html/SSN/TESTING")
"""
