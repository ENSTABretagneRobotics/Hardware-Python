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

pMDM = CreateMDM()
# Check and modify the configuration file if needed...
result = ConnectMDM(pMDM, 'MDM0.txt')

ion() # Turn the interactive mode on.

# Create a figure that will use the function on_key() when a key is
# pressed.
fig = figure('Test')
cid = fig.canvas.mpl_connect('key_press_event',on_key)

while (bExit == 0):
    clf(); axis('square'); axis([-200,200,-200,200])
    buf = zeros(4)
    result = RecvDataMDM(pMDM, buf, 4)
    nbbytes = result[1]
    str='%d'%(buf[0])
    text(-150,0,str)
    pause(1)

result = DisconnectMDM(pMDM)
DestroyMDM(pMDM)
