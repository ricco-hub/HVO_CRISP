def fractional(year, month, day):

 

 if (year-1976)%4 == 0 :
     #print("bisesto")
     if month == 1:
       return(    round(year +  (day/366.)  , 3   )   )
     if month == 2:
       return(     round(year   +   ( (day + 31)  / 366.) , 3)   )
     if month == 3:
       return( round(year   +   ( (day + 60)  / 366.)  , 3)  )
     if month == 4:
       return( round(year   +   ( (day + 91)  / 366.) ,3)  )
     if month == 5:
       return( round(year   +   ( (day + 121)  / 366.),3) )
     if month == 6:
       return( round(year   +   ( (day + 152)  / 366.)  ,3))
     if month == 7:
       return( round(year   +   ( (day + 182)  / 366.),3)  )
     if month == 8:
       return( round(year   +   ( (day + 213)  / 366.) ,3) )
     if month == 9:
       return( round(year   +   ( (day + 244)  / 366.) , 3) )
     if month == 10:
       return(round( year   +   ( (day + 274)  / 366.), 3)  )
     if month == 11:
       return( round(year   +   ( (day + 304)  / 366.), 3)  )
     if month == 12:
       return(round( year   +   ( (day + 335)  / 366.) ,3) )

 else:
     if month == 1:
       return( round(year    +  (day/365.) , 3)  )
     if month == 2:
       return( round(year   +   ( (day + 31)  / 365.) , 3)  )
     if month == 3:
       return( round( year   +   ( (day + 59)  / 365.) ,3))
     if month == 4:
       return( round( year   +   ( (day + 90)  / 365.) ,3)  )
     if month == 5:
       return( round(year   +   ( (day + 120)  / 365.)  ,3))
     if month == 6:
       return( round(year   +   ( (day + 151)  / 365.) , 3) )
     if month == 7:
       return( round(year   +   ( (day + 181)  / 365.) , 3)  )
     if month == 8:
       return( round(year   +   ( (day + 212)  / 365.) , 3) )
     if month == 9:
       return( round(year   +   ( (day + 243)  / 365.)  ,3))
     if month == 10:
       return( round(year   +   ( (day + 273)  / 365.) , 3) )
     if month == 11:
       return(round( year   +   ( (day + 303)  / 365.), 3)  )
     if month == 12:
       return( round(year   +   ( (day + 334)  / 365.), 3)  )





'''
      decimal_year = year + ((day - 0.5)/365) + vmonthbisesto[month]
 else:
     decimal_year = year + ((day - 0.5)/365) + vmonth[month]

 lines2 = tuple(open('/var/www/html/SSN/SSN_History.txt', "r"))
 fyear = []
 fmonth = []
 fday = []
 fractional = []
 for h in range(len(lines2)):
   sline2 = lines2[h].split()
   fyear.append(sline2[0])
   fmonth.append(sline2[1])
   fday.append(sline2[2])
   fractional.append(sline2[3])

#ricercare il giusto valore di fractional
 for i in range(len(fyear)):
  if int(fyear[i]) == year:
   for k in range(i,len(fyear)):
    if int(fmonth[k]) == month:
     for j in range(k,len(fyear)):
      if int(fday[j]) == day:
       return(fractional[j])
      # break
      #break
  # break

  #se il valore è oltre la lista restituire comunque il current - date

 '''
