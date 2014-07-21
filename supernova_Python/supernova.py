#!/usr/bin/python

import io
import ephem

# Read mode opens a file for reading only.
try:
    f = open("supernova.txt", "r")
    try:
        # Read the entire contents of a file at once.
        string = f.read()
        startpoint = 0 
        while  string.find("2014 06",startpoint)>0:
            print "01234567890123456789012345678901234567890"
            print  string[startpoint-1:startpoint+50]
            decl = int(  string[startpoint+29:startpoint+32])
            rac = int( string[startpoint+16:startpoint+20])
            rac10 =  int( string[startpoint+20:startpoint+23])
            rac = rac+(0.0+rac10)/60.0
            np = ephem.Equatorial(rac, decl, epoch='2000')
            g = ephem.Galactic(np)
            print('%s %s' % (g.lon, g.lat))
            print str(rac+(0.0+rac10)/60.0)+" --  "+" - "+str(decl)+" - "
            startpoint = 1+string.find("2014 06", startpoint)


            #np = Equatorial('0', '90', epoch='2000')
# OR read one line at a time.
        line = f.readline()
        print line
        # OR read all the lines into a list.
        lines = f.readlines()
    finally:
        f.close()
except IOError:
    pass
