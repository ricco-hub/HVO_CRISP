import requests
import os
import time
import shutil
#begin

#NORTH L
file4 = open("/var/www/html/Wilcox_TILT/DTXT/Tilt_L_n.txt","w")
file4.write("Wilcox Solar Observatory data downloaded from HVO:\ncolumn 1 - Date in fraction of year. \ncolumn 2 - Maximum extent in latitude reached by the computed heliospheric current sheet (HCS) i.e. Tilt Angle of the heliospheric current sheet. Values are provided for the maximum northern extent of the HCS (line-of-sight model).\n\n")
with open("/var/www/html/Wilcox_TILT/data_PLOT/Tilt_L_n.txt", "r") as infile:
 SSN_all = infile.readlines()
 for i in range(len(SSN_all)):
  sline = SSN_all[i].split()
  print(sline)
  file4.write('%8.3f'   % (float(sline[0])))
  file4.write( "\t"  +  str( float(sline[1]))  + "\n" )
 # file4.write('%8.3f  %8.3f'   % (float(sline[0]), float(sline[1])))
 # file4.write("\n")


# l s
file4 = open("/var/www/html/Wilcox_TILT/DTXT/Tilt_L_s.txt","w")
file4.write("Wilcox Solar Observatory data downloaded from HVO:\ncolumn 1 - Date in fraction of year. \ncolumn 2 - Maximum extent in latitude reached by the computed heliospheric current sheet (HCS) i.e. Tilt Angle of the heliospheric current sheet. Values are provided for the maximum southern extent of the HCS (line-of-sight model).\n\n")
with open("/var/www/html/Wilcox_TILT/data_PLOT/Tilt_L_s.txt", "r") as infile:
 SSN_all = infile.readlines()
 for i in range(len(SSN_all)):
  sline = SSN_all[i].split()
  print(sline)
  file4.write('%8.3f'   % (float(sline[0])))
  file4.write( "\t"  +  str( float(sline[1]))  + "\n" )
# file4.write('%8.3f  %8.3f'   % (float(sline[0]), float(sline[1])))
#  file4.write("\n")

# l avg
file4 = open("/var/www/html/Wilcox_TILT/DTXT/Tilt_L_av.txt","w")
file4.write("Wilcox Solar Observatory data downloaded from HVO:\ncolumn 1 - Date in fraction of year. \ncolumn 2 - Maximum extent in latitude reached by the computed heliospheric current sheet (HCS) i.e. Tilt Angle of the heliospheric current sheet. Values are provided for the average maximum extent of the HCS (line-of-sight model).\n\n")
with open("/var/www/html/Wilcox_TILT/data_PLOT/Tilt_L_av.txt", "r") as infile:
 SSN_all = infile.readlines()
 for i in range(len(SSN_all)):
  sline = SSN_all[i].split()
  print(sline)
  file4.write('%8.3f'   % (float(sline[0])))
  file4.write( "\t"  +  str( float(sline[1]))  + "\n" )
 # file4.write('%8.3f  %8.3f'   % (float(sline[0]), float(sline[1])))
 # file4.write("\n")


# R avg
file4 = open("/var/www/html/Wilcox_TILT/DTXT/Tilt_R_av.txt","w")
file4.write("Wilcox Solar Observatory data downloaded from HVO:\ncolumn 1 - Date in fraction of year. \ncolumn 2 - Maximum extent in latitude reached by the computed heliospheric current sheet (HCS) i.e. Tilt Angle of the heliospheric current sheet. Values are provided for the average maximum extent of the HCS (radial model).\n\n")
with open("/var/www/html/Wilcox_TILT/data_PLOT/Tilt_R_av.txt", "r") as infile:
 SSN_all = infile.readlines()
 for i in range(len(SSN_all)):
  sline = SSN_all[i].split()
  print(sline)
  file4.write('%8.3f'   % (float(sline[0])))
  file4.write( "\t"  +  str( float(sline[1]))  + "\n" ) 
# file4.write('%8.3f  %8.3f'   % (float(sline[0]), float(sline[1])))
 # file4.write("\n")



  # R n
  file4 = open("/var/www/html/Wilcox_TILT/DTXT/Tilt_R_n.txt","w")
  file4.write("Wilcox Solar Observatory data downloaded from HVO:\ncolumn 1 - Date in fraction of year. \ncolumn 2 - Maximum extent in latitude reached by the computed heliospheric current sheet (HCS) i.e. Tilt Angle of the heliospheric current sheet. Values are provided for the maximum southern extent of the HCS (radial model).\n\n")
  with open("/var/www/html/Wilcox_TILT/data_PLOT/Tilt_R_n.txt", "r") as infile:
   SSN_all = infile.readlines()
   for i in range(len(SSN_all)):
    sline = SSN_all[i].split()
    print(sline)
    file4.write('%8.3f'   % (float(sline[0])))
    file4.write( "\t"  +  str( float(sline[1]))  + "\n" )
  #  file4.write('%8.3f  %8.3f'   % (float(sline[0]), float(sline[1])))
  # file4.write("\n")



  # R s
  file4 = open("/var/www/html/Wilcox_TILT/DTXT/Tilt_R_s.txt","w")
  file4.write("Wilcox Solar Observatory data downloaded from HVO:\ncolumn 1 - Date in fraction of year. \ncolumn 2 - Maximum extent in latitude reached by the computed heliospheric current sheet (HCS) i.e. Tilt Angle of the heliospheric current sheet. Values are provided for the maximum southern extent of the HCS (radial model).\n\n")
  with open("/var/www/html/Wilcox_TILT/data_PLOT/Tilt_R_s.txt", "r") as infile:
   SSN_all = infile.readlines()
   for i in range(len(SSN_all)):
    sline = SSN_all[i].split()
    print(sline)
    file4.write('%8.3f'   % (float(sline[0])))
    file4.write( "\t"  +  str( float(sline[1]))  + "\n" )   
# file4.write('%8.3f  %8.3f'   % (float(sline[0]), float(sline[1])))
#    file4.write("\n")
