#!/usr/bin/python

from blinkstick import *
import psutil

print "Display CPU usage with BlinkStick"
print "(c) Agile Innovative Ltd"
print ""

bstick = BlinkStick.find_first()

if (bstick == None):
    print "No BlinkSticks found..."
else:
    print "Displaying CPU usage (Green = 0%, Amber = 50%, Red = 100%)"
    print "Press Ctrl+C to exit"

    while True:
        cpu = psutil.cpu_percent(interval=1)
        intensity = int(255 * cpu / 100)

        bstick.set_color(intensity, 255 - intensity, 0)