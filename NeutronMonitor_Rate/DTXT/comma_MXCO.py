import pandas as pd
import datetime
from rev import revert
#import csv
s = "MXCO"

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
    
dati = pd.DataFrame({'Date': date, s+' (carr rot)': ssn})
dati.head()
#dati = dati.drop(columns="Unnamed: 0")
dati["date"] = pd.to_datetime(dati["Date"], format="%Y-%m-%d")
dati = dati.set_index('date')
dati = dati.drop(columns=['Date'])
dati.to_csv(s+'carr.csv')
dati.head() 


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
