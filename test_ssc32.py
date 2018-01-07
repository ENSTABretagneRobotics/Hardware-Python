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

pSSC32 = CreateSSC32()
# Check and modify the configuration file if needed...
result = ConnectSSC32(pSSC32, 'SSC320.txt')

result = SetAllPWMsSSC32(pSSC32, [1,1,1,0,0], [1000,2000,1000,1500,1500])

ion() # Turn the interactive mode on.

# Create a figure that will use the function on_key() when a key is
# pressed.
fig = figure('Test')
cid = fig.canvas.mpl_connect('key_press_event',on_key)

# If SetPWMSSC32(), SetAllPWMsSSC32()... take too much time, use a thread to access data faster...
result = StartThreadSSC32(pSSC32)

a = 0
while (bExit == 0):
    clf()
    axis('square')
    axis([-200,200,-200,200])
    if (mod(a, 2) == 0):
        result = SetAllPWMsFromThreadSSC32(pSSC32, [1,1,1,0,0], [1000,2000,1250,1500,1500])
    else:
        result = SetAllPWMsFromThreadSSC32(pSSC32, [1,1,1,0,0], [2000,1000,1750,1500,1500])    
    a = a+1
    str = 'a = %d\n'%(a)
    text(-150,0,str)
    pause(2);

result = StopThreadSSC32(pSSC32)
result = DisconnectSSC32(pSSC32)
DestroySSC32(pSSC32)
