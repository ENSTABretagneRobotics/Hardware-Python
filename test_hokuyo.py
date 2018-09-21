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

pHokuyo = CreateHokuyo()
# Check and modify the configuration file if needed...
result = ConnectHokuyo(pHokuyo, 'Hokuyo0.txt')

result = GetLatestDataHokuyo(pHokuyo)
distances = result[1]
print('Distance on the left =',distances[angle2kHokuyo(pHokuyo, pi/2.0)],'m \n')

ion() # Turn the interactive mode on.

# Create a figure that will use the function on_key() when a key is
# pressed.
fig = figure('Test')
cid = fig.canvas.mpl_connect('key_press_event',on_key)
scale = 6

# If GetLatestDataHokuyo() takes too much time, use a thread to access data faster...
result = StartThreadHokuyo(pHokuyo)

while (bExit == 0):
    clf(); axis('square'); axis([-scale,scale,-scale,scale])
    result = GetLatestDataFromThreadHokuyo(pHokuyo)
    distances = result[1]; angles = result[2]
    plot(distances*cos(angles), distances*sin(angles), '.')
    pause(0.01)

result = StopThreadHokuyo(pHokuyo)
result = DisconnectHokuyo(pHokuyo)
DestroyHokuyo(pHokuyo)
