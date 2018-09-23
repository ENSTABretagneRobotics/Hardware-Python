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
distance = result[1]; angle = result[2]; bNewScan = result[3]; quality = result[4]
print('Distance at',angle*180.0/pi,'deg =',distance,'m \n')
#result = GetExpressScanDataResponseRPLIDAR(pRPLIDAR)
#distances = result[1]; angles = result[2]; bNewScan = result[3]
#print('Distance at',angles[0]*180.0/pi,'deg =',distances[0],'m \n')

ion() # Turn the interactive mode on.

# Create a figure that will use the function on_key() when a key is
# pressed.
fig = figure('Test')
cid = fig.canvas.mpl_connect('key_press_event',on_key)
scale = 6

#result = StartScanThreadRPLIDAR(pRPLIDAR)
#result = StartExpressScanThreadRPLIDAR(pRPLIDAR)

count = 0; alldistances = []; allangles = []
while (bExit == 0):
    result = GetScanDataResponseRPLIDAR(pRPLIDAR)
    #result = GetScanDataResponseFromThreadRPLIDAR(pRPLIDAR)
    #result = GetExpressScanDataResponseRPLIDAR(pRPLIDAR)
    #result = GetExpressScanDataResponseFromThreadRPLIDAR(pRPLIDAR)
    distances = result[1]; angles = result[2]; bNewScan = result[3];
    alldistances.append(distances); allangles.append(angles)
    if count > 360:
    #if count > 720/32:
        clf(); axis('square'); axis([-scale,scale,-scale,scale])
        plot(alldistances*cos(allangles), alldistances*sin(allangles), '.')
        pause(0.01)
        count = 0; alldistances = []; allangles = []
    count = count+1;

#result = StopScanThreadRPLIDAR(pRPLIDAR)
#result = StopExpressScanThreadRPLIDAR(pRPLIDAR)
result = DisconnectRPLIDAR(pRPLIDAR)
DestroyRPLIDAR(pRPLIDAR)