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

pSBG = CreateSBG()
# Check and modify the configuration file if needed...
result = ConnectSBG(pSBG, 'SBG0.txt')

result = GetLatestDataSBG(pSBG)
sbgdata = result[1]
print('Yaw =',sbgdata.Yaw*180.0/pi,', Pitch =',sbgdata.Pitch*180.0/pi,', Roll =',sbgdata.Roll*180.0/pi,'\n')

ion() # Turn the interactive mode on.

# Create a figure that will use the function on_key() when a key is
# pressed.
fig = figure('Test')
cid = fig.canvas.mpl_connect('key_press_event',on_key)

# If GetLatestDataSBG() takes too much time, use a thread to access data faster...
result = StartThreadSBG(pSBG)

while (bExit == 0):
    clf(); axis('square'); axis([-200,200,-200,200])
    result = GetLatestDataFromThreadSBG(pSBG)
    sbgdata = result[1]
    str='Yaw = %.2f, Pitch = %.2f, Roll = %.2f'%(sbgdata.Yaw*180.0/pi,sbgdata.Pitch*180.0/pi,sbgdata.Roll*180.0/pi)
    text(-150,0,str)
    pause(0.01)

result = StopThreadSBG(pSBG)
result = DisconnectSBG(pSBG)
DestroySBG(pSBG)
