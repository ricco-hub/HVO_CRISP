R_LDFLAGS =     `root-config --ldflags`
R_LIBS    =     `root-config --libs`
R_CFLAGS  =     `root-config --cflags`
R_ALL     =     $(R_LADFLAGS) $(R_LIBS) $(R_CFLAGS)

Graph: Graph.cpp
	g++ -o Graph Graph.cpp $(R_ALL)
