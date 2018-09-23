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

pMT = CreateMT()
# Check and modify the configuration file if needed...
result = ConnectMT(pMT, 'MT0.txt')

result = GetLatestDataMT(pMT)
mtdata = result[1]
print('Yaw =',mtdata.Yaw*180.0/pi,', Pitch =',mtdata.Pitch*180.0/pi,', Roll =',mtdata.Roll*180.0/pi,'\n')

ion() # Turn the interactive mode on.

# Create a figure that will use the function on_key() when a key is
# pressed.
fig = figure('Test')
cid = fig.canvas.mpl_connect('key_press_event',on_key)

# If GetLatestDataMT() takes too much time, use a thread to access data faster...
result = StartThreadMT(pMT)

while (bExit == 0):
    clf(); axis('square'); axis([-200,200,-200,200])
    result = GetLatestDataFromThreadMT(pMT)
    mtdata = result[1]
    str='Yaw = %.2f, Pitch = %.2f, Roll = %.2f'%(mtdata.Yaw*180.0/pi,mtdata.Pitch*180.0/pi,mtdata.Roll*180.0/pi)
    text(-150,0,str)
    pause(0.01)

result = StopThreadMT(pMT)
result = DisconnectMT(pMT)
DestroyMT(pMT)
