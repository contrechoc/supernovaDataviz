#!/usr/bin/python

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

while True:
    time.sleep(3)
    ser.write(b'3')
