import pandas as pd
from rev import revert
import datetime
#import csv

file1 = open('/var/www/html/SSN/DTXT/SSN_Smooth_range.txt', 'r')
Lines = file1.readlines()
string = []
insert = []
date=[]
ssn=[]
err=[]


for i  in range(len(Lines)-5):
    Lines2 = Lines[i+5].replace("\t", " ")
    string.append(Lines2.replace("\n", " "))
    insert = string[i].split()
    date.append(revert(float(insert[0])))
    ssn.append(insert[1])
    err.append(insert[2])
    
data = pd.DataFrame({'Date': date, 'SSN smoothed': ssn,'Err': err})
data.head()
#dati = dati.drop(columns="Unnamed: 0")

data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])

data.to_csv('ssn_smooth.csv')
data.head() 
