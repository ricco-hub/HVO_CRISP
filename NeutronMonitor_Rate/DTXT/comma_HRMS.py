import pandas as pd
#import csv
import datetime
from rev import revert
s = "HRMS"

file1 = open(s+'carr.txt', 'r')
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
    
data = pd.DataFrame({'Date': date, s+' (carr rot)': ssn})
data.head()
#dati = dati.drop(columns="Unnamed: 0")
data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])
data.to_csv(s+'carr.csv')
data.head() 


file1 = open(s+'day.txt', 'r')
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

dati = pd.DataFrame({'Date': date, s+' (day)': ssn})
dati.head()
#dati = dati.drop(columns="Unnamed: 0")
dati["date"] = pd.to_datetime(dati["Date"], format="%Y-%m-%d")
dati = dati.set_index('date')
dati = dati.drop(columns=['Date'])
dati.to_csv(s+'day.csv')
dati.head()


file1 = open(s+'month.txt', 'r')
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

dati = pd.DataFrame({'Date': date, s+' (month)': ssn})
dati.head()
#dati = dati.drop(columns="Unnamed: 0")
dati["date"] = pd.to_datetime(dati["Date"], format="%Y-%m-%d")
dati = dati.set_index('date')
dati = dati.drop(columns=['Date'])
dati.to_csv(s+'month.csv')
dati.head()




file1 = open(s+'year.txt', 'r')
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

dati = pd.DataFrame({'Date': date, s+' (year)': ssn})
dati.head()
#dati = dati.drop(columns="Unnamed: 0")
dati["date"] = pd.to_datetime(dati["Date"], format="%Y-%m-%d")
dati = dati.set_index('date')
dati = dati.drop(columns=['Date'])
dati.to_csv(s+'year.csv')
dati.head()
