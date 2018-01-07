Hardware-Python
==============
Windows : 
- Copy hardwarex.dll/.so from x86 folder if you use Python 32 bit or x64 folder if you use Python 64 bit (or download the ones from Hardware-MATLAB) and put it in this project folder (rename hardwarex.so to libhardwarex.so for Linux).
- Check e.g. test_razorahrs.py file for usage information.

Sample : http://www.ensta-bretagne.fr/lebars/Share/buggy_real_gps.zip for the buggy based on an Android smartphone described on http://www.ensta-bretagne.fr/lebars/buggy_android_full.pdf .

Change the device path and other parameters in the configuration files if necessary. Mind the line endings in the configuration files depending on the OS (use e.g. the command dos2unix *.txt to convert line endings for Linux)!

Tested on Windows 10 64 bit using Python 3.5 32 bit.

Hardware support : 
- Hokuyo : Hokuyo URG-04LX-UG01 laser telemeter.
- Maestro : Pololu Mini Maestro 6, 18, 24 servo controllers.
- NMEADevice : GPS, Furuno WS200 weather station.
- RazorAHRS : SparkFun 9DOF Razor IMU.
- RPLIDAR : RPLIDAR A2 laser telemeter.
- SSC-32 : Lynxmotion SSC-32, SSC-32u servo controllers.
- ublox : ublox GPS.

See also https://github.com/ENSTABretagneRobotics/Android, https://github.com/ENSTABretagneRobotics/Hardware-CPP, https://github.com/ENSTABretagneRobotics/Hardware-MATLAB, https://github.com/ENSTABretagneRobotics/Hardware-Java.
