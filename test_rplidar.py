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

# If bStartScanModeAtStartup to 0 in RPLIDAR0.txt...
#result = ResetRequestRPLIDAR(pRPLIDAR)
#print(result)
#pause(2)
#result = GetStartupMessageRPLIDAR(pRPLIDAR)
#print(result)
#result = StopRequestRPLIDAR(pRPLIDAR)
#print(result)
#result = GetInfoRequestRPLIDAR(pRPLIDAR)
#print(result)
# Not all the models support this function...
#result = GetTypicalScanModeRPLIDAR(pRPLIDAR)
#print(result)
#typicalscanmodeid = result[1]
#result = GetAllSupportedScanModesRPLIDAR(pRPLIDAR)
#print('Typical scan mode :',bytearray(result[5][typicalscanmodeid]).decode("utf-8"))
#result = SetMotorPWMRequestRPLIDAR(pRPLIDAR, 660)
#print(result)
#result = StartScanRequestRPLIDAR(pRPLIDAR)
##result = StartExpressScanRequestRPLIDAR(pRPLIDAR)
##result = StartOtherScanRequestRPLIDAR(pRPLIDAR, typicalscanmodeid)
#print(result)
#pause(2)

result = GetScanDataResponseRPLIDAR(pRPLIDAR)
distance = result[1]; angle = result[2]; bNewScan = result[3]; quality = result[4]
print('Distance at',angle*180.0/pi,'deg =',distance,'m \n')
#result = GetExpressScanDataResponseRPLIDAR(pRPLIDAR)
#distances = result[1]; angles = result[2]; bNewScan = result[3]
#result = GetOtherScanDataResponseRPLIDAR(pRPLIDAR)
#distances = result[1]; angles = result[2]; bNewScan = result[3]
#print('Distance at',angles[0]*180.0/pi,'deg =',distances[0],'m \n')

ion() # Turn the interactive mode on.

# Create a figure that will use the function on_key() when a key is
# pressed.
fig = figure('Test')
cid = fig.canvas.mpl_connect('key_press_event',on_key)
scale = 6

result = StartScanThreadRPLIDAR(pRPLIDAR)
#result = StartExpressScanThreadRPLIDAR(pRPLIDAR)
#result = StartOtherScanThreadRPLIDAR(pRPLIDAR)

# The matplotlib display functions might cause too many delays...
count = 0; alldistances = []; allangles = []
while (bExit == 0):
    #result = GetScanDataResponseRPLIDAR(pRPLIDAR); nbMeasurements = 1 # A2 Standard Scan mode
    #result = GetScanDataResponseFromThreadRPLIDAR(pRPLIDAR); nbMeasurements = 1
    #result = GetExpressScanDataResponseRPLIDAR(pRPLIDAR); nbMeasurements = 32 # A2 Legacy Express Scan mode
    #result = GetExpressScanDataResponseFromThreadRPLIDAR(pRPLIDAR); nbMeasurements = 32
    #result = GetOtherScanDataResponseRPLIDAR(pRPLIDAR); nbMeasurements = result[4] # S2 Dense Scan mode
    #result = GetOtherScanDataResponseFromThreadRPLIDAR(pRPLIDAR); nbMeasurements = result[4]
    result = GetLast360DataFromThreadRPLIDAR(pRPLIDAR); nbMeasurements = result[3]
    distances = result[1]; angles = result[2]; bNewScan = result[3];
    if nbMeasurements == 1:
        alldistances.append(distances); allangles.append(angles)
    else:
        for i in range(0, nbMeasurements): alldistances.append(distances[i]); allangles.append(angles[i])
    #if bNewScan:
    #if count > 360: # A2 Standard Scan mode
    #if count > 720/32: # A2 Legacy Express Scan mode
    #if count > 360/0.12/40: # S2 Dense Scan mode
    if True: # GetLast360DataFromThreadRPLIDAR()
        clf(); axis('square'); axis([-scale,scale,-scale,scale])
        plot(alldistances*cos(allangles), alldistances*sin(allangles), '.')
        pause(0.01)
        count = 0; alldistances = []; allangles = []
    count = count+1;

result = StopScanThreadRPLIDAR(pRPLIDAR)
#result = StopExpressScanThreadRPLIDAR(pRPLIDAR)
#result = StopOtherScanThreadRPLIDAR(pRPLIDAR)
result = DisconnectRPLIDAR(pRPLIDAR)
DestroyRPLIDAR(pRPLIDAR)
