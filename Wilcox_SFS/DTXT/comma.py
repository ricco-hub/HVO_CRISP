import pandas as pd
#import csv
import datetime
from rev import revert

file1 = open('Avg_F_range.txt', 'r')
Lines = file1.readlines()
string = []
insert = []
date=[]
ssn=[]

for i  in range(len(Lines)-4):
    Lines2 = Lines[i+4].replace("\t", " ")
    string.append(Lines2.replace("\n", " "))
    insert = string[i].split()
    date.append(revert(insert[0]))
    ssn.append(insert[1])
        
data = pd.DataFrame({'Date': date, "SPFS - Avg - 20 nhz low pass filtered  ": ssn})
#dati = dati.drop(columns="Unnamed: 0")
data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])
data.to_csv('avg_f.csv')


file1 = open('Avg_range.txt', 'r')
Lines = file1.readlines()
string = []
insert = []
date=[]
ssn=[]

for i  in range(len(Lines)-4):
    Lines2 = Lines[i+4].replace("\t", " ")
    string.append(Lines2.replace("\n", " "))
    insert = string[i].split()
    date.append(revert(insert[0]))
    ssn.append(insert[1])

data = pd.DataFrame({'Date': date, "SPFS - Avg ": ssn})
#dati = dati.drop(columns="Unnamed: 0")
data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])
data.to_csv('avg.csv')



file1 = open('North_F_range.txt', 'r')
Lines = file1.readlines()
string = []
insert = []
date=[]
ssn=[]

for i  in range(len(Lines)-4):
    Lines2 = Lines[i+4].replace("\t", " ")
    string.append(Lines2.replace("\n", " "))
    insert = string[i].split()
    date.append(revert(insert[0]))
    ssn.append(insert[1])

data = pd.DataFrame({'Date': date, "SPFS - North -  20 nhz low pass filtered ": ssn})
#dati = dati.drop(columns="Unnamed: 0")
data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])
data.to_csv('north_f.csv')



file1 = open('North_range.txt', 'r')
Lines = file1.readlines()
string = []
insert = []
date=[]
ssn=[]

for i  in range(len(Lines)-4):
    Lines2 = Lines[i+4].replace("\t", " ")
    string.append(Lines2.replace("\n", " "))
    insert = string[i].split()
    date.append(revert(insert[0]))
    ssn.append(insert[1])

data = pd.DataFrame({'Date': date, "SPFS - North": ssn})
#dati = dati.drop(columns="Unnamed: 0")
data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])
data.to_csv('north.csv')


file1 = open('South_F_range.txt', 'r')
Lines = file1.readlines()
string = []
insert = []
date=[]
ssn=[]

for i  in range(len(Lines)-4):
    Lines2 = Lines[i+4].replace("\t", " ")
    string.append(Lines2.replace("\n", " "))
    insert = string[i].split()
    date.append(revert(insert[0]))
    ssn.append(insert[1])

data = pd.DataFrame({'Date': date, "SPFS - South -  20 nhz low pass filtered ": ssn})
#dati = dati.drop(columns="Unnamed: 0")
data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])
data.to_csv('south_f.csv')


file1 = open('South_range.txt', 'r')
Lines = file1.readlines()
string = []
insert = []
date=[]
ssn=[]

for i  in range(len(Lines)-4):
    Lines2 = Lines[i+4].replace("\t", " ")
    string.append(Lines2.replace("\n", " "))
    insert = string[i].split()
    date.append(revert(insert[0]))
    ssn.append(insert[1])

data = pd.DataFrame({'Date': date, "SPFS - South": ssn})
#dati = dati.drop(columns="Unnamed: 0")
data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])
data.to_csv('south.csv')