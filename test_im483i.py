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

pIM483I = CreateIM483I()
# Check and modify the configuration file if needed...
result = ConnectIM483I(pIM483I, 'IM483I0.txt')

pause(0.1)
result = SetMaxAngleIM483I(pIM483I, 0.25)

ion() # Turn the interactive mode on.

# Create a figure that will use the function on_key() when a key is
# pressed.
fig = figure('Test')
cid = fig.canvas.mpl_connect('key_press_event',on_key)

# If SetMaxAngleIM483I() takes too much time, use a thread to access data faster...
result = StartThreadIM483I(pIM483I)

a = 0
while (bExit == 0):
    clf(); axis('square'); axis([-200,200,-200,200])
    if (mod(a, 2) == 0):
        result = SetMaxAngleFromThreadIM483I(pIM483I, 0.25)
    else:
        result = SetMaxAngleFromThreadIM483I(pIM483I, -0.25)    
    a = a+1
    str = 'a = %d\n'%(a)
    text(-150,0,str)
    pause(2)

result = StopThreadIM483I(pIM483I)
result = DisconnectIM483I(pIM483I)
DestroyIM483I(pIM483I)
