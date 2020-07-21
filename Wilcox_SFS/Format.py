import requests
import os
import time
import shutil
#begin 

#NORTH
file4 = open("/var/www/html/Wilcox_SFS/DTXT/North_range.txt","w")
file4.write("Wilcox Solar Observatory data downloaded from HVO: \ncolumn 1 - Date in fraction of year. \ncolumn 2 - Sun's Polar Field strength in North emisphere.\n\n")

with open("/var/www/html/Wilcox_SFS/data_PLOT/North_range.txt", "r") as infile:
 SSN_all = infile.readlines()
 for i in range(len(SSN_all)):
  sline = SSN_all[i].split()
  print(sline)
  file4.write('%8.3f'   % (float(sline[0])))
  file4.write( "\t"  +  str( float(sline[1]))  + "\n" )
 # file4.write('%8.3f  %8.3f'   % (float(sline[0]), float(sline[1])))
 # file4.write("\n")



#NORTH filtered                                                                                                                                                                
file4 = open("/var/www/html/Wilcox_SFS/DTXT/North_F_range.txt","w")
file4.write("Wilcox Solar Observatory data downloaded from HVO: \ncolumn 1 - Date in fraction of year. \ncolumn 2 - Sun's Polar Field strength in North emisphere. A 20nhz low pass filtered values eliminate yearly geometric projection effects.\n\n")

with open("/var/www/html/Wilcox_SFS/data_PLOT/North_F_range.txt", "r") as infile:
 SSN_all = infile.readlines()
 for i in range(len(SSN_all)):
  sline = SSN_all[i].split()
  print(sline)
  file4.write('%8.3f'   % (float(sline[0])))
  file4.write( "\t"  +  str( float(sline[1]))  + "\n" ) 

# file4.write('%8.3f  %8.3f'   % (float(sline[0]), float(sline[1])))
 # file4.write("\n")


#SOUTH                                                                                                                                                          
file4 = open("/var/www/html/Wilcox_SFS/DTXT/South_range.txt","w")
file4.write("Wilcox Solar Observatory data downloaded from HVO: \ncolumn 1 - Date in fraction of year. \ncolumn 2 - Sun's Polar Field strength in South emisphere.\n\n")

with open("/var/www/html/Wilcox_SFS/data_PLOT/South_range.txt", "r") as infile:
 SSN_all = infile.readlines()
 for i in range(len(SSN_all)):
  sline = SSN_all[i].split()
  print(sline)
  file4.write('%8.3f'   % (float(sline[0])))
  file4.write( "\t"  +  str( float(sline[1]))  + "\n" ) 

# file4.write('%8.3f  %8.3f'   % (float(sline[0]), float(sline[1])))
 # file4.write("\n")


#NORTH filtered                                                                                                                                                     
file4 = open("/var/www/html/Wilcox_SFS/DTXT/South_F_range.txt","w")
file4.write("Wilcox Solar Observatory data downloaded from HVO: \ncolumn 1 - Date in fraction of year. \ncolumn 2 - Sun's Polar Field strength in South emisphere. A 20nhz low pass filtered values eliminate yearly geometric projection effects.\n\n")

with open("/var/www/html/Wilcox_SFS/data_PLOT/South_F_range.txt", "r") as infile:
 SSN_all = infile.readlines()
 for i in range(len(SSN_all)):
  sline = SSN_all[i].split()
  print(sline)
  file4.write('%8.3f'   % (float(sline[0])))
  file4.write( "\t"  +  str( float(sline[1]))  + "\n" ) 

# file4.write('%8.3f  %8.3f'   % (float(sline[0]), float(sline[1])))
 # file4.write("\n")



#Avg                                                                                                                                                  
file4 = open("/var/www/html/Wilcox_SFS/DTXT/Avg_range.txt","w")
file4.write("Wilcox Solar Observatory data downloaded from HVO: \ncolumn 1 - Date in fraction of year. \ncolumn 2 - Sun's Polar Field strength (average).\n\n")

with open("/var/www/html/Wilcox_SFS/data_PLOT/Avg_range.txt", "r") as infile:
 SSN_all = infile.readlines()
 for i in range(len(SSN_all)):
  sline = SSN_all[i].split()
  print(sline)
  file4.write('%8.3f'   % (float(sline[0])))
  file4.write( "\t"  +  str( float(sline[1]))  + "\n" ) 

# file4.write('%8.3f  %8.3f'   % (float(sline[0]), float(sline[1])))
 # file4.write("\n")


#Avg filtered                                                                                                                                                     
file4 = open("/var/www/html/Wilcox_SFS/DTXT/Avg_F_range.txt","w")
file4.write("Wilcox Solar Observatory data downloaded from HVO: \ncolumn 1 - Date in fraction of year. \ncolumn 2 - Sun's Polar Field strength in North emisphere. A 20nhz low pass filtered values eliminate yearly geometric projection effects.\n\n")

with open("/var/www/html/Wilcox_SFS/data_PLOT/Avg_F_range.txt", "r") as infile:
 SSN_all = infile.readlines()
 for i in range(len(SSN_all)):
  sline = SSN_all[i].split()
  print(sline)
  file4.write('%8.3f'   % (float(sline[0])))
  file4.write( "\t"  +  str( float(sline[1]))  + "\n" )
 
# file4.write('%8.3f  %8.3f'   % (float(sline[0]), float(sline[1])))
#  file4.write("\n")


'''

#daily 
file4 = open("/var/www/html/SSN/DTXT/SSN_range.txt","w")
file4.write("DAILY SUNSPOT NUMBER DATA downloaded from HVO: \n 1 - Date in fraction of year \n 2 - Daily total sunspot number. \n 3 - Daily standard deviation of the input sunspot numbers from individual stations.\n\n")
with open("/var/www/html/SSN/data_PLOT/SSN_range.txt", "r") as infile:
 SSN_all = infile.readlines()
 for i in range(len(SSN_all)):
  sline = SSN_all[i].split()
  print(sline)
  file4.write('%8.3f   %8.3f    %8.3f'   % (float(sline[0]), float(sline[1]), float(sline[3])))
  file4.write("\n")



#monthly
file4 = open("/var/www/html/SSN/DTXT/SSN_Monthly_range.txt","w")
file4.write("MONTHLY SUNSPOT NUMBER DATA downloaded from HVO: \n 1 - Date in fraction of year. \n 2 - Daily total sunspot number.\n 3 - Monthly mean standard deviation of the input sunspot numbers from individual stations.\n\n")
with open("/var/www/html/SSN/data_PLOT/SSN_Monthly_range.txt", "r") as infile:
 SSN_all = infile.readlines()
 for i in range(len(SSN_all)):
  sline = SSN_all[i].split()
  print(sline)
  file4.write('%8.3f   %8.3f    %8.3f'   % (float(sline[0]), float(sline[1]), float(sline[3])))
  file4.write("\n")
'''