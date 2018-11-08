#!/usr/bin/env python
from __future__ import print_function
from matplotlib.pyplot import *
from numpy import *
from numpy.random import *

from hardwarex import *

bExit = 0

# This function should be called when a key is pressed.
def on_key(event):
    # Global variables to share with other functions.
    global bExit
    # Actions to do depending on the key pressed.
    #print('You pressed', event.key, event.xdata, event.ydata)
    if event.key == 'escape':
        bExit = 1

pP33x = CreateP33x()
# Check and modify the configuration file if needed...
result = ConnectP33x(pP33x, 'P33x0.txt')

result = GetPressureP33x(pP33x)
pressure = result[1]
print('Pressure =',pressure,', bar\n')

ion() # Turn the interactive mode on.

# Create a figure that will use the function on_key() when a key is
# pressed.
fig = figure('Test')
cid = fig.canvas.mpl_connect('key_press_event',on_key)

# If GetPressureP33x() takes too much time, use a thread to access data faster...
result = StartThreadP33x(pP33x)

while (bExit == 0):
    clf(); axis('square'); axis([-200,200,-200,200])
    result = GetPressureFromThreadP33x(pP33x)
    pressure = result[1]
    str='Pressure = %.2f bar'%(pressure)
    text(-150,0,str)
    pause(0.01)

result = StopThreadP33x(pP33x)
result = DisconnectP33x(pP33x)
DestroyP33x(pP33x)
