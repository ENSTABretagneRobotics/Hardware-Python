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

pRPLIDAR = CreateRPLIDAR()
# Check and modify the configuration file if needed...
result = ConnectRPLIDAR(pRPLIDAR, 'RPLIDAR0.txt')

result = GetScanDataResponseRPLIDAR(pRPLIDAR)
distance = result[1]
angle = result[2]
print('Distance at',angle*180.0/pi,'deg =',distance,'m \n')
#result = GetExpressScanDataResponseRPLIDAR(pRPLIDAR)
#distances = result[1]
#angles = result[2]
#print('Distance at',angles[0]*180.0/pi,'deg =',distances[0],'m \n')

ion() # Turn the interactive mode on.

# Create a figure that will use the function on_key() when a key is
# pressed.
fig = figure('Test')
cid = fig.canvas.mpl_connect('key_press_event',on_key)
scale = 6

# If GetLatestDataRPLIDAR() takes too much time, use a thread to access data faster...
#result = StartScanThreadRPLIDAR(pRPLIDAR)
#result = StartExpressScanThreadRPLIDAR(pRPLIDAR)

count = 0
clf()
axis('square')
axis([-scale,scale,-scale,scale])
while (bExit == 0):
    if count > 360:
        count = 0
        clf()
        axis('square')
        axis([-scale,scale,-scale,scale])
    result = GetScanDataResponseRPLIDAR(pRPLIDAR)
    #result = GetScanDataResponseFromThreadRPLIDAR(pRPLIDAR)
    distance = result[1]
    angle = result[2]
    bNewScan = result[3]
    #print('Distance at',angle*180.0/pi,'deg =',distance,'m \n')
    plot(distance*cos(angle), distance*sin(angle), '.')
    #result = GetExpressScanDataResponseFromThreadRPLIDAR(pRPLIDAR)
    #distances = result[1]
    #angles = result[2]
    #bNewScan = result[3]
    ##print('Distance at',angles[0]*180.0/pi,'deg =',distances[0],'m \n')
    #plot(distances[0]*cos(angles[0]), distances[0]*sin(angles[0]), '.')
    count = count+1;
    pause(0.001)

#result = StopScanThreadRPLIDAR(pRPLIDAR)
#result = StopExpressScanThreadRPLIDAR(pRPLIDAR)
result = DisconnectRPLIDAR(pRPLIDAR)
DestroyRPLIDAR(pRPLIDAR)
