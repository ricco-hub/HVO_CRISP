import pandas as pd
#import csv
from rev import revert
import datetime

file1 = open('/var/www/html/SSN/DTXT/SSN_Monthly_range.txt', 'r')
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
    
data = pd.DataFrame({'Date': date, 'SSN monthly': ssn,'Err': err})
data.head()
#dati = dati.drop(columns="Unnamed: 0")
#a = "6-6-2004"
#b = pd.to_datetime(a, format="%d-/%m-/%Y")

data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])


data.to_csv('ssn_monthly.csv')
data.head() 
