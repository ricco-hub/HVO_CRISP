import requests
import os
import time
import shutil
#scarico il mese corrente completo

with open("/var/www/html/Wilcox_SFS/E.txt", "r") as infile:
   date = infile.readlines()
   
print(date[0])
print(date[1])

stop1 ='2020.029'
stop2 = '2020.056'

#SFS NORTH       
ssnr = open("/var/www/html/Wilcox_SFS/data_PLOT/North_range.txt","w")
with open("/var/www/html/Wilcox_SFS/SFSNorth.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     if(sline[0] != stop1 and sline[0] != stop2 ):
       if(  float(date[0])<= float(sline[0]) <= float(date[1])) :
         ssnr.write('%8.3f'   % (float(sline[0])))
         ssnr.write( "\t"  +  str( float(sline[1]))  + "\n" )

#         ssnr.write('%8.3f   %8.3f'   % (float(sline[0]), float(sline[1])))
#         ssnr.write('\n')

print("end")

#SFS NORTH  Filtered                                                                                                                     
ssnr = open("/var/www/html/Wilcox_SFS/data_PLOT/North_F_range.txt","w")
with open("/var/www/html/Wilcox_SFS/SFSNf.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     if(sline[0] != stop1 and sline[0] != stop2):
      if(  float(date[0])<= float(sline[0]) <= float(date[1])) :
         ssnr.write('%8.3f'   % (float(sline[0])))
         ssnr.write( "\t"  +  str( float(sline[1]))  + "\n" )
# ssnr.write('%8.3f   %8.3f'   % (float(sline[0]), float(sline[1])))
#         ssnr.write('\n')


#SFS SOUTH                                                                                                             
ssnr = open("/var/www/html/Wilcox_SFS/data_PLOT/South_range.txt","w")
with open("/var/www/html/Wilcox_SFS/SFSSouth.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     if(sline[0] != stop1 and sline[0] != stop2):
      if(  float(date[0])<= float(sline[0]) <= float(date[1])) :
         ssnr.write('%8.3f'   % (float(sline[0])))
         ssnr.write( "\t"  +  str( float(sline[1]))  + "\n" )

       # ssnr.write('%8.3f   %8.3f'   % (float(sline[0]), float(sline[1])))
       #  ssnr.write('\n')


#SFS South  Filtered                                                                                                          
ssnr = open("/var/www/html/Wilcox_SFS/data_PLOT/South_F_range.txt","w")
with open("/var/www/html/Wilcox_SFS/SFSSf.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     if(sline[0] != stop1 and  sline[0] != stop2):
      if(  float(date[0])<= float(sline[0]) <= float(date[1])) :
         ssnr.write('%8.3f'   % (float(sline[0])))
         ssnr.write( "\t"  +  str( float(sline[1]))  + "\n" )

 #ssnr.write('%8.3f   %8.3f'   % (float(sline[0]), float(sline[1])))
 #        ssnr.write('\n')

#SFS Avg                                                                                                                        
ssnr = open("/var/www/html/Wilcox_SFS/data_PLOT/Avg_range.txt","w")
with open("/var/www/html/Wilcox_SFS/SFSAvg.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     if(sline[0] != stop1 and sline[0] != stop2):
      if(  float(date[0])<= float(sline[0]) <= float(date[1])) :
         ssnr.write('%8.3f'   % (float(sline[0])))
         ssnr.write( "\t"  +  str( float(sline[1]))  + "\n" )
#ssnr.write('%8.3f   %8.3f'   % (float(sline[0]), float(sline[1])))
#         ssnr.write('\n')


#SFS AVg   Filtered                                                                                                             
ssnr = open("/var/www/html/Wilcox_SFS/data_PLOT/Avg_F_range.txt","w")
with open("/var/www/html/Wilcox_SFS/SFSAvgf.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     if(sline[0] != stop1 or sline[0] != stop2):     
       if(  float(date[0])<= float(sline[0]) <= float(date[1])) :
         ssnr.write('%8.3f'   % (float(sline[0])))
         ssnr.write( "\t"  +  str( float(sline[1]))  + "\n" )
#        ssnr.write('%8.3f   %8.3f'   % (float(sline[0]), float(sline[1])))
#         ssnr.write('\n')
