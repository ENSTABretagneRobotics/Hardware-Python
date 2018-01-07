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

publox = Createublox()
# Check and modify the configuration file if needed...
result = Connectublox(publox, 'ublox0.txt')

result = GetNMEASentenceublox(publox)
nmeadata = result[1]
print('(LAT,LON) = (',nmeadata.Latitude,',',nmeadata.Longitude,')\n')

ion() # Turn the interactive mode on.

# Create a figure that will use the function on_key() when a key is
# pressed.
fig = figure('Test')
cid = fig.canvas.mpl_connect('key_press_event',on_key)

# If GetNMEASentenceublox() takes too much time, use a thread to access data faster...
result = StartNMEAThreadublox(publox)

while (bExit == 0):
    clf()
    axis('square')
    axis([-200,200,-200,200])
    result = GetNMEASentenceFromThreadublox(publox);
    nmeadata = result[1]
    if ((abs(nmeadata.Latitude) > 0) & (abs(nmeadata.Longitude) > 0)): # Check if latitude and longitude are not 0, which means invalid.
        str='(LAT,LON) = (%.8f,%.8f)'%(nmeadata.Latitude,nmeadata.Longitude)
    text(-150,0,str)
    pause(0.01);

result = StopNMEAThreadublox(publox)
result = Disconnectublox(publox)
Destroyublox(publox)
