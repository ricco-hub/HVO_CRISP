R_LDFLAGS =     `root-config --ldflags`
R_LIBS    =     `root-config --libs`
R_CFLAGS  =     `root-config --cflags`
R_ALL     =     $(R_LADFLAGS) $(R_LIBS) $(R_CFLAGS)

MONITOR_RANGE_year: drawing4.cpp
	g++ -o MONITOR_RANGE_year drawing4.cpp $(R_ALL)
