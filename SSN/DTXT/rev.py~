def revert(input):
    vmonth = [0,0,0.085,0.162,0.247,0.329,0.414,0.496,0.581,0.666,0.748,0.833,0.915]
    vmonthbisesto = [0,0,0.085,0.164,0.249,0.331,0.415,0.497,0.582,0.667,0.749,0.833,0.915]
    y = 0
    d = 0
    m = 0
    comp = input
    rnd = int(input)
#print( round(comp - rnd,3))
#print(rnd)
    for month in range(1,13):
        for day in range(1,32):
            if (rnd-1976)%4 == 0 :
                if  round(comp - rnd,3) ==  round(((day - 0.5)/365) + vmonthbisesto[month],3):
                    y = rnd
                    d = day
                    m = month
                    break
            else:
                if  round(comp - rnd,3) ==  round(((day - 0.5)/365) + vmonth[month],3):
                    y = rnd
                    d = day
                    m = month
                    break
    res = str(y)+"-"+str(m)+"-"+str(d)
    return res
