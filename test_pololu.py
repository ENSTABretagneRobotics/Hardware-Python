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

pPololu = CreatePololu()
# Check and modify the configuration file if needed...
result = ConnectPololu(pPololu, 'Pololu0.txt')

pause(0.1)
result = SetPWMPololu(pPololu, 0, 1350)
pause(0.5)
nbchannels = 24
selectedchannels = zeros(nbchannels, int)
selectedchannels[0] = 1; selectedchannels[1] = 1; selectedchannels[2] = 1
pws = zeros(nbchannels, int)
pws[0] = int(1000); pws[1] = int(2000); pws[2] = int(1000)
result = SetAllPWMsPololu(pPololu, selectedchannels, pws)
pause(0.1)
result = GetValuePololu(pPololu, 11)
value = result[1]
print('value = ',value,'\n')

ion() # Turn the interactive mode on.

# Create a figure that will use the function on_key() when a key is
# pressed.
fig = figure('Test')
cid = fig.canvas.mpl_connect('key_press_event',on_key)

# If GetValuePololu(), SetAllPWMsPololu()... take too much time, use a thread to access data faster...
result = StartThreadPololu(pPololu)

a = 0
while (bExit == 0):
    clf(); axis('square'); axis([-200,200,-200,200])
    if (mod(a, 2) == 0):
        pws[0] = int(1000); pws[1] = int(2000); pws[2] = int(1250)
    else:
        pws[0] = int(2000); pws[1] = int(1000); pws[2] = int(1750)
    result = SetAllPWMsFromThreadPololu(pPololu, selectedchannels, pws)    
    a = a+1
    result = GetValueFromThreadPololu(pPololu, 11)
    value = result[1]
    str = 'a = %d, value = %d\n'%(a, value)
    text(-150,0,str)
    pause(2)

result = StopThreadPololu(pPololu)
result = DisconnectPololu(pPololu)
DestroyPololu(pPololu)
