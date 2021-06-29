import pandas as pd
#import csv

from rev import revert
import datetime

file1 = open('Proton_range.txt', 'r')
Lines = file1.readlines()
string = []
insert = []
date=[]
ssn=[]
err=[]


for i  in range(len(Lines)-4):
    Lines2 = Lines[i+4].replace("\t", " ")
    string.append(Lines2.replace("\n", " "))
    insert = string[i].split()
    date.append(revert(insert[0]))
    ssn.append(insert[1])
    
    
data = pd.DataFrame({'Date': date, 'Proton density': ssn})
data.head()
#dati = dati.drop(columns="Unnamed: 0")
data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])
data.to_csv('Proton_range.csv')
data.head() 



file1 = open('Speed_range.txt', 'r')
Lines = file1.readlines()
string = []
insert = []
date=[]
ssn=[]
err=[]


for i  in range(len(Lines)-4):
    Lines2 = Lines[i+4].replace("\t", " ")
    string.append(Lines2.replace("\n", " "))
    insert = string[i].split()
    date.append(revert(insert[0]))
    ssn.append(insert[1])


data = pd.DataFrame({'Date': date, 'Solar wind speed': ssn})
data.head()
#dati = dati.drop(columns="Unnamed: 0")
data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])
data.to_csv('Speed_range.csv')
data.head()
