def decimal_year(year, month, day):
 vmonth = [0,0,0.085,0.162,0.247,0.329,0.414,0.496,0.581,0.666,0.748,0.833,0.915]
 vmonthbisesto = [0,0,0.085,0.164,0.249,0.331,0.415,0.497,0.582,0.667,0.749,0.833,0.915]

 if (year-1976)%4 == 0 :
      decimal_year = year + ((day - 0.5)/365) + vmonthbisesto[month]
 else:
     decimal_year = year + ((day - 0.5)/365) + vmonth[month]


 decimal_year = round(decimal_year,3)
 return decimal_year
