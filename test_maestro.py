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

pMaestro = CreateMaestro()
# Check and modify the configuration file if needed...
result = ConnectMaestro(pMaestro, 'Maestro0.txt')

result = SetAllPWMsMaestro(pMaestro, [1,1,1,0,0], [1000,2000,1000,1500,1500])
result = GetValueMaestro(pMaestro, 11)
value = result[1]
print('value = ',value,'\n')

ion() # Turn the interactive mode on.

# Create a figure that will use the function on_key() when a key is
# pressed.
fig = figure('Test')
cid = fig.canvas.mpl_connect('key_press_event',on_key)

# If GetValueMaestro(), SetAllPWMsMaestro()... take too much time, use a thread to access data faster...
result = StartThreadMaestro(pMaestro)

a = 0
while (bExit == 0):
    clf()
    axis('square')
    axis([-200,200,-200,200])
    if (mod(a, 2) == 0):
        result = SetAllPWMsFromThreadMaestro(pMaestro, [1,1,1,0,0], [1000,2000,1250,1500,1500])
    else:
        result = SetAllPWMsFromThreadMaestro(pMaestro, [1,1,1,0,0], [2000,1000,1750,1500,1500])    
    a = a+1
    result = GetValueFromThreadMaestro(pMaestro, 11)
    value = result[1]
    str = 'a = %d, value = %d\n'%(a, value)
    text(-150,0,str)
    pause(2);

result = StopThreadMaestro(pMaestro)
result = DisconnectMaestro(pMaestro)
DestroyMaestro(pMaestro)
