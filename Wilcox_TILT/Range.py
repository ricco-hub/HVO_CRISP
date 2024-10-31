import requests
import os
import time
import shutil
#scarico il mese corrente completo

with open("/var/www/html/Wilcox_TILT/E.txt", "r") as infile:
   date = infile.readlines()
   
print(date[0])
print(date[1])


# tilt L av
ssnr = open("/var/www/html/Wilcox_TILT/data_PLOT/Tilt_L_av.txt","w")
with open("/var/www/html/Wilcox_TILT/Tilt_L_av.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     if(  float(date[0])<= float(sline[0]) <= float(date[1])) :
         ssnr.write('%8.3f'   % (float(sline[0])))
         ssnr.write( "\t"  +  str( float(sline[1]))  + "\n" )
#ssnr.write('%8.3f   %8.3f'   % (float(sline[0]), float(sline[1])))
#         ssnr.write('\n')

print("end")

# tilt L south                                                                                           
ssnr = open("/var/www/html/Wilcox_TILT/data_PLOT/Tilt_L_s.txt","w")
with open("/var/www/html/Wilcox_TILT/Tilt_L_s.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     if(  float(date[0])<= float(sline[0]) <= float(date[1])) :
         ssnr.write('%8.3f'   % (float(sline[0])))
         ssnr.write( "\t"  +  str( float(sline[1]))  + "\n" )
     #    ssnr.write('%8.3f   %8.3f'   % (float(sline[0]), float(sline[1])))
     #    ssnr.write('\n')


# tilt L north                                                                                                             
ssnr = open("/var/www/html/Wilcox_TILT/data_PLOT/Tilt_L_n.txt","w")
with open("/var/www/html/Wilcox_TILT/Tilt_L_n.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     if(  float(date[0])<= float(sline[0]) <= float(date[1])) :
         ssnr.write('%8.3f'   % (float(sline[0])))
         ssnr.write( "\t"  +  str( float(sline[1]))  + "\n" )      
#   ssnr.write('%8.3f   %8.3f'   % (float(sline[0]), float(sline[1])))
#         ssnr.write('\n')


# tilt R  av                                                                                 
ssnr = open("/var/www/html/Wilcox_TILT/data_PLOT/Tilt_R_av.txt","w")
with open("/var/www/html/Wilcox_TILT/Tilt_R_av.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     if(  float(date[0])<= float(sline[0]) <= float(date[1])) :
         ssnr.write('%8.3f'   % (float(sline[0])))
         ssnr.write( "\t"  +  str( float(sline[1]))  + "\n" )       
 # ssnr.write('%8.3f   %8.3f'   % (float(sline[0]), float(sline[1])))
 #        ssnr.write('\n')

# tilt R _ north                                                                                  
ssnr = open("/var/www/html/Wilcox_TILT/data_PLOT/Tilt_R_n.txt","w")
with open("/var/www/html/Wilcox_TILT/Tilt_R_n.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     if(  float(date[0])<= float(sline[0]) <= float(date[1])) :
         ssnr.write('%8.3f'   % (float(sline[0])))
         ssnr.write( "\t"  +  str( float(sline[1]))  + "\n" )  
     #  ssnr.write('%8.3f   %8.3f'   % (float(sline[0]), float(sline[1])))
     #    ssnr.write('\n')


# tilt R south                                                                                   
ssnr = open("/var/www/html/Wilcox_TILT/data_PLOT/Tilt_R_s.txt","w")
with open("/var/www/html/Wilcox_TILT/Tilt_R_s.txt", "r") as infile:
    SSN_all = infile.readlines()
    for i in range(len(SSN_all)):
     sline = SSN_all[i].split()
     if(  float(date[0])<= float(sline[0]) <= float(date[1])) :
         ssnr.write('%8.3f'   % (float(sline[0])))
         ssnr.write( "\t"  +  str( float(sline[1]))  + "\n" )      
  # ssnr.write('%8.3f   %8.3f'   % (float(sline[0]), float(sline[1])))
      #   ssnr.write('\n')
