import pandas as pd
import datetime
from rev import revert
#import csv

s = "OULU"

file1 = open(s+'PHI.txt', 'r')
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
    date.append(revert(insert[0]))
    ssn.append(insert[1])
    
st = "name"    
dati = pd.DataFrame({'Date': date, s+' phi potential ': ssn})
dati.head()
#dati = dati.drop(columns="Unnamed: 0")
dati["date"] = pd.to_datetime(dati["Date"], format="%Y-%m-%d")
dati = dati.set_index('date')
dati = dati.drop(columns=['Date'])
dati.to_csv(s+'PHI.csv')
dati.head()


file1 = open('JMOD'+s+'.txt', 'r')
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
    date.append(revert(insert[0]))
    ssn.append(insert[1])
    

dati = pd.DataFrame({'Date': date,'Flux CR ('+s+')': ssn})
dati.head()
#dati = dati.drop(columns="Unnamed: 0")
dati["date"] = pd.to_datetime(dati["Date"], format="%Y-%m-%d")
dati = dati.set_index('date')
dati = dati.drop(columns=['Date'])
dati.to_csv('JMOD'+s+".csv")
dati.head()
