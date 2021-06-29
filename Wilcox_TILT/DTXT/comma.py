import pandas as pd
#import csv
from rev import revert
import datetime

file1 = open('Tilt_L_av.txt', 'r')
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

    
data = pd.DataFrame({'Date': date, 'Tilt L model - Avg  ': ssn})
data.head()
#dati = dati.drop(columns="Unnamed: 0")
data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])
data.to_csv('Tilt_L_av.csv')
data.head() 


file1 = open('Tilt_L_n.txt', 'r')
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
    

data = pd.DataFrame({'Date': date, 'Tilt L model - N  ': ssn})
data.head()
#dati = dati.drop(columns="Unnamed: 0")
data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])
data.to_csv('Tilt_L_n.csv')



file1 = open('Tilt_L_s.txt', 'r')
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
    

data = pd.DataFrame({'Date': date, 'Tilt L model - S  ': ssn})
data.head()
#dati = dati.drop(columns="Unnamed: 0")
data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])
data.to_csv('Tilt_L_s.csv')
data.head()




file1 = open('Tilt_R_av.txt', 'r')
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
    

data = pd.DataFrame({'Date': date, 'Tilt R model - Avg  ': ssn})
data.head()
#dati = dati.drop(columns="Unnamed: 0")
data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])
data.to_csv('Tilt_R_av.csv')
data.head()



file1 = open('Tilt_R_n.txt', 'r')
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

data = pd.DataFrame({'Date': date, 'Tilt R model - N  ': ssn})
data.head()
#dati = dati.drop(columns="Unnamed: 0")
data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])
data.to_csv('Tilt_R_n.csv')
data.head()





file1 = open('Tilt_R_s.txt', 'r')
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
    

data = pd.DataFrame({'Date': date, 'Tilt R model - S  ': ssn})
data.head()
#dati = dati.drop(columns="Unnamed: 0")
data["date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data = data.set_index('date')
data = data.drop(columns=['Date'])
data.to_csv('Tilt_R_s.csv')
data.head()
