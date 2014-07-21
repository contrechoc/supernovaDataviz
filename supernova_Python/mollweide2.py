#!/usr/bin/python

import numpy as np
import pylab as pl
import math
import io
import ephem

import serial

import time
from threading import Timer

def timeout():
    global t
    ser.write(b'5')
    t = Timer(10, timeout)
    t.start()


t = Timer(10, timeout)

ser = serial.Serial('/dev/tty.usbserial-A600cKvw', 9600)

x = np.array([0]) # longitude
#np.concatenate(x,np.array( [200]))
y = np.array([0]) # latitude
#np.concatenate(y,np.array( [89]))
lab = ['0']
timeArray = np.array([0])


p1 = ephem.Galactic(80,-15)
p2 = ephem.Galactic(-80,-15)
p3 = ephem.Galactic(150,40)
p4 = ephem.Galactic(0,70)
p5 = ephem.Galactic(-150,40)

mollweidePointsX = np.array( [p1.lon,p2.lon,p3.lon,p4.lon,p5.lon] )
mollweidePointsY = np.array( [p1.lat,p2.lat,p3.lat,p4.lat,p5.lat] )

monthNum = 1
monthNumSearch = "2014 0"+str(monthNum)

# Read mode opens a file for reading only.
try:
    f = open("supernova.txt", "r")
    try:
        # Read the entire contents of a file at once.
        string = f.read()
        timestart = 0
        for i in range(1,7,1):
            startpoint = 0
            counter = 0
            monthNumSearch = "2014 0"+str(i)
            if i == 2:
                timestart = timestart + 31
            if i == 3:
                timestart = timestart + 28
            if i == 4:
                timestart = timestart + 31
            if i == 5:
                timestart = timestart + 30
            if i == 6:
                timestart = timestart + 31
            while  string.find(monthNumSearch,startpoint)>0 :
        
                print "01234567890123456789012345678901234567890"
                print string[startpoint-1:startpoint+50] + " " + string[startpoint+5:startpoint+15]
                decl =  string[startpoint+29:startpoint+29+11]
                rac =  string[startpoint+17:startpoint+17+11]
                rac = rac.replace(" ", ":");
                decl = decl.replace(" ", ":");
                print "rac=" + rac + " decl= " + decl
                nE = ephem.Equatorial(rac, decl, epoch='2000')
                g = ephem.Galactic(nE)
                print('galactic %f %f %s %s' % (float(g.lon), float(g.lat), g.lon, g.lat ) )
                g1 = ephem.degrees(g.lon) #0. + int(float(g.lon+0.)/math.pi*180.)
                gVal = float( g.lon)*180./ephem.pi
                if gVal > 180:
                    gVal = -(360 - gVal)
                #p1 = ephem.Galactic(120,-15)
                for j in range(0,5,1):
                    if  float(ephem.separation( (mollweidePointsX[j], mollweidePointsY[j] ), (g.lon,g.lat) )) < .9:
                        x = np.append(x, gVal )
                        g2 = ephem.degrees(float(g.lat)*180/ephem.pi)
                        print "galactic " + str(g1) + "   " +  str(g2)
                        y = np.append(y, g2)
                        #print str(rac)+" - "+str(decl)+" - "
                        lab = np.append(lab, str(j))
                        timeArray = np.append(timeArray, timestart + int( string[startpoint+7:startpoint+9])) 
                startpoint = 1+string.find(monthNumSearch, startpoint)
            print "month "+str(i) + " " + str (counter) + " supernovas"

    finally:
        f.close()
except IOError:
    pass

# the spot to plot

# To plot the celestial equator in galactic coordinates
degtorad = math.pi/180.
alpha = np.arange(-180,180.,1.)
alpha *= degtorad
# From Meeus, Astronomical algorithms (with delta = 0)
x1 = np.sin(192.25*degtorad - alpha)
x2 = np.cos(192.25*degtorad - alpha)*np.sin(27.4*degtorad)
yy = np.arctan2(x1, x2)
longitude = 303*degtorad - yy 
x3 = np.cos(27.4*degtorad) * np.cos(192.25*degtorad - alpha)
latitude  = np.arcsin(x3)

# We put the angles in the right direction
for i in range(0,len(alpha)):
    if longitude[i] > 2.*math.pi:
        longitude[i] -= 2.*math.pi
    longitude[i] -= math.pi
    latitude[i] = -latitude[i]

# To avoid a line in the middle of the plot (the curve must not loop)
for i in range(0,len(longitude)-1):
    if (longitude[i] * longitude[i+1] < 0 and longitude[i] > 170*degtorad and longitude[i+1] < -170.*degtorad):
        indice = i
        break

# The array is put in increasing longitude 
longitude2 = np.zeros(len(longitude))
latitude2 = np.zeros(len(latitude))
longitude2[0:len(longitude)-1-indice] = longitude[indice+1:len(longitude)]
longitude2[len(longitude)-indice-1:len(longitude)] = longitude[0:indice+1]
latitude2[0:len(longitude)-1-indice] = latitude[indice+1:len(longitude)]
latitude2[len(longitude)-indice-1:len(longitude)] = latitude[0:indice+1]

xrad = x * degtorad
yrad = y * degtorad

fig2 = pl.figure(2)
ax1 = fig2.add_subplot(111, projection="mollweide")

ax1.scatter(xrad,yrad)
ax1.plot([-math.pi, math.pi], [0,0],'r-')
ax1.plot([0,0],[-math.pi, math.pi], 'r-')

# plot celestial equator
ax1.plot(longitude2,latitude2,'g-')

print "{"

for i in range(1,len(x)-1):
    ax1.text(xrad[i], yrad[i], lab[i] )
    print lab [i] + ", " +str(timeArray[i])+ ", "
 
print"}"

pl.title("Supernova 2014 jan-june e-textile summercamp ")
pl.grid(True)

pl.show()

#ser.write(b'5')
 
#while True:
#    time.sleep(1)
#    ser.write(b'3')
