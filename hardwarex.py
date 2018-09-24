from __future__ import print_function
import ctypes
from ctypes import util
import sys

# Load DLL into memory.
if sys.platform.startswith('win'):
    is_64bits = sys.maxsize > 2**32
    if is_64bits:
        hDll = ctypes.CDLL("x64/hardwarex.dll")
    else:
        hDll = ctypes.CDLL("x86/hardwarex.dll")
elif sys.platform.startswith('linux'):
    hDll = ctypes.CDLL("libhardwarex.so")
elif sys.platform.startswith('darwin'):
    hDll = ctypes.CDLL("libhardwarex.dylib")
else:
    hDll = ctypes.CDLL(ctypes.util.find_library("hardwarex"))

class UTC_Time_SBG(ctypes.Structure):
    _fields_ = [("Nanoseconds", ctypes.c_uint),
	            ("Year", ctypes.c_ushort),
	            ("Month", ctypes.c_ubyte),
	            ("Day", ctypes.c_ubyte),
	            ("Hour", ctypes.c_ubyte),
	            ("Minute", ctypes.c_ubyte),
	            ("Seconds", ctypes.c_ubyte),
	            ("Valid", ctypes.c_ubyte)]

class SBGDATA(ctypes.Structure):
    _fields_ = [("temp", ctypes.c_double), 
                ("accx", ctypes.c_double), ("accy", ctypes.c_double), ("accz", ctypes.c_double),
                ("gyrx", ctypes.c_double), ("gyry", ctypes.c_double), ("gyrz", ctypes.c_double),
                ("magx", ctypes.c_double), ("magy", ctypes.c_double), ("magz", ctypes.c_double),
                ("q0", ctypes.c_double), ("q1", ctypes.c_double), ("q2", ctypes.c_double), ("q3", ctypes.c_double),
                ("roll", ctypes.c_double), ("pitch", ctypes.c_double), ("yaw", ctypes.c_double),
                ("a", ctypes.c_double), ("b", ctypes.c_double), ("c", ctypes.c_double),
                ("d", ctypes.c_double), ("e", ctypes.c_double), ("f", ctypes.c_double),
                ("g", ctypes.c_double), ("h", ctypes.c_double), ("i", ctypes.c_double),
                ("Ain_1", ctypes.c_ushort), ("Ain_2", ctypes.c_ushort),
                ("Lat", ctypes.c_double), ("Long", ctypes.c_double), ("Alt", ctypes.c_double),
                ("Vel_X", ctypes.c_double), ("Vel_Y", ctypes.c_double), ("Vel_Z", ctypes.c_double),
                ("eulerStdDev", ctypes.c_float*3),
                ("positionStdDev", ctypes.c_float*3),
                ("velocityStdDev", ctypes.c_float*3),
                ("odometerVelocity", ctypes.c_double),
                ("gpsRawData", ctypes.c_ubyte*4086),
                ("gpsRawDataSize", ctypes.c_uint),
                ("Status", ctypes.c_ubyte),
                ("TS", ctypes.c_ushort),
                ("UTCTime", UTC_Time_SBG),
                ("Roll", ctypes.c_double), ("Pitch", ctypes.c_double), ("Yaw", ctypes.c_double)]

def CreateSBGData():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(SBGDATA))
    hApiParams = None
    function_call = hApiProto(('CreateSBGDatax', hDll), hApiParams)
    return function_call()

def DestroySBGData(pSBGData):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(SBGDATA))
    hApiParams = (1, "pSBGData", 0),
    function_call = hApiProto(('DestroySBGDatax', hDll), hApiParams)
    function_call(pSBGData)

def CreateSBG():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('CreateSBGx', hDll), hApiParams)
    return function_call()

def DestroySBG(pSBG):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pSBG", 0),
    function_call = hApiProto(('DestroySBGx', hDll), hApiParams)
    function_call(pSBG)

def GetLatestDataSBG(pSBG):
    global hDll

    pSBGData = CreateSBGData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(SBGDATA))
    hApiParams = (1, "pSBG", 0),(1, "pSBGData", 0),
    function_call = hApiProto(('GetLatestDataSBGx', hDll), hApiParams)
    res = function_call(pSBG, pSBGData)
    
    sbgdata = pSBGData[0]

    DestroySBGData(pSBGData)

    return res, sbgdata

def ConnectSBG(pSBG, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "pSBG", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectSBGx', hDll), hApiParams)
    return function_call(pSBG, cfgFilePath.encode('UTF-8'))

def DisconnectSBG(pSBG):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pSBG", 0),
    function_call = hApiProto(('DisconnectSBGx', hDll), hApiParams)
    return function_call(pSBG)

def GetLatestDataFromThreadSBG(pSBG):
    global hDll

    pSBGData = CreateSBGData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(SBGDATA))
    hApiParams = (1, "pSBG", 0),(1, "pSBGData", 0),
    function_call = hApiProto(('GetLatestDataFromThreadSBGx', hDll), hApiParams)
    res = function_call(pSBG, pSBGData)
    
    sbgdata = pSBGData[0]

    DestroySBGData(pSBGData)

    return res, sbgdata

def StartThreadSBG(pSBG):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pSBG", 0),
    function_call = hApiProto(('StartThreadSBGx', hDll), hApiParams)
    return function_call(pSBG)

def StopThreadSBG(pSBG):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pSBG", 0),
    function_call = hApiProto(('StopThreadSBGx', hDll), hApiParams)
    return function_call(pSBG)

class UTC_Time_MT(ctypes.Structure):
    _fields_ = [("Nanoseconds", ctypes.c_uint),
	            ("Year", ctypes.c_ushort),
	            ("Month", ctypes.c_ubyte),
	            ("Day", ctypes.c_ubyte),
	            ("Hour", ctypes.c_ubyte),
	            ("Minute", ctypes.c_ubyte),
	            ("Seconds", ctypes.c_ubyte),
	            ("Valid", ctypes.c_ubyte)]

class MTDATA(ctypes.Structure):
    _fields_ = [("temp", ctypes.c_double), 
                ("accx", ctypes.c_double), ("accy", ctypes.c_double), ("accz", ctypes.c_double),
                ("gyrx", ctypes.c_double), ("gyry", ctypes.c_double), ("gyrz", ctypes.c_double),
                ("magx", ctypes.c_double), ("magy", ctypes.c_double), ("magz", ctypes.c_double),
                ("q0", ctypes.c_double), ("q1", ctypes.c_double), ("q2", ctypes.c_double), ("q3", ctypes.c_double),
                ("roll", ctypes.c_double), ("pitch", ctypes.c_double), ("yaw", ctypes.c_double),
                ("a", ctypes.c_double), ("b", ctypes.c_double), ("c", ctypes.c_double),
                ("d", ctypes.c_double), ("e", ctypes.c_double), ("f", ctypes.c_double),
                ("g", ctypes.c_double), ("h", ctypes.c_double), ("i", ctypes.c_double),
                ("Ain_1", ctypes.c_ushort), ("Ain_2", ctypes.c_ushort),
                ("Lat", ctypes.c_double), ("Long", ctypes.c_double), ("Alt", ctypes.c_double),
                ("Vel_X", ctypes.c_double), ("Vel_Y", ctypes.c_double), ("Vel_Z", ctypes.c_double),
                ("Status", ctypes.c_ubyte),
                ("TS", ctypes.c_ushort),
                ("UTCTime", UTC_Time_MT),
                ("Roll", ctypes.c_double), ("Pitch", ctypes.c_double), ("Yaw", ctypes.c_double)]

def CreateMTData():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(MTDATA))
    hApiParams = None
    function_call = hApiProto(('CreateMTDatax', hDll), hApiParams)
    return function_call()

def DestroyMTData(pMTData):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(MTDATA))
    hApiParams = (1, "pMTData", 0),
    function_call = hApiProto(('DestroyMTDatax', hDll), hApiParams)
    function_call(pMTData)

def CreateMT():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('CreateMTx', hDll), hApiParams)
    return function_call()

def DestroyMT(pMT):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pMT", 0),
    function_call = hApiProto(('DestroyMTx', hDll), hApiParams)
    function_call(pMT)

def GetLatestDataMT(pMT):
    global hDll

    pMTData = CreateMTData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(MTDATA))
    hApiParams = (1, "pMT", 0),(1, "pMTData", 0),
    function_call = hApiProto(('GetLatestDataMTx', hDll), hApiParams)
    res = function_call(pMT, pMTData)
    
    mtdata = pMTData[0]

    DestroyMTData(pMTData)

    return res, mtdata

def ConnectMT(pMT, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "pMT", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectMTx', hDll), hApiParams)
    return function_call(pMT, cfgFilePath.encode('UTF-8'))

def DisconnectMT(pMT):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pMT", 0),
    function_call = hApiProto(('DisconnectMTx', hDll), hApiParams)
    return function_call(pMT)

def GetLatestDataFromThreadMT(pMT):
    global hDll

    pMTData = CreateMTData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(MTDATA))
    hApiParams = (1, "pMT", 0),(1, "pMTData", 0),
    function_call = hApiProto(('GetLatestDataFromThreadMTx', hDll), hApiParams)
    res = function_call(pMT, pMTData)
    
    mtdata = pMTData[0]

    DestroyMTData(pMTData)

    return res, mtdata

def StartThreadMT(pMT):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pMT", 0),
    function_call = hApiProto(('StartThreadMTx', hDll), hApiParams)
    return function_call(pMT)

def StopThreadMT(pMT):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pMT", 0),
    function_call = hApiProto(('StopThreadMTx', hDll), hApiParams)
    return function_call(pMT)

class RAZORAHRSDATA(ctypes.Structure):
    _fields_ = [("yaw", ctypes.c_double), ("pitch", ctypes.c_double), ("roll", ctypes.c_double),
                ("accx", ctypes.c_double), ("accy", ctypes.c_double), ("accz", ctypes.c_double),
                ("gyrx", ctypes.c_double), ("gyry", ctypes.c_double), ("gyrz", ctypes.c_double),
                ("Roll", ctypes.c_double), ("Pitch", ctypes.c_double), ("Yaw", ctypes.c_double)]

def CreateRazorAHRSData():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(RAZORAHRSDATA))
    hApiParams = None
    function_call = hApiProto(('CreateRazorAHRSDatax', hDll), hApiParams)
    return function_call()

def DestroyRazorAHRSData(pRazorAHRSData):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(RAZORAHRSDATA))
    hApiParams = (1, "pRazorAHRSData", 0),
    function_call = hApiProto(('DestroyRazorAHRSDatax', hDll), hApiParams)
    function_call(pRazorAHRSData)

def CreateRazorAHRS():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('CreateRazorAHRSx', hDll), hApiParams)
    return function_call()

def DestroyRazorAHRS(pRazorAHRS):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRazorAHRS", 0),
    function_call = hApiProto(('DestroyRazorAHRSx', hDll), hApiParams)
    function_call(pRazorAHRS)

def GetLatestDataRazorAHRS(pRazorAHRS):
    global hDll

    pRazorAHRSData = CreateRazorAHRSData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(RAZORAHRSDATA))
    hApiParams = (1, "pRazorAHRS", 0),(1, "pRazorAHRSData", 0),
    function_call = hApiProto(('GetLatestDataRazorAHRSx', hDll), hApiParams)
    res = function_call(pRazorAHRS, pRazorAHRSData)
    
    razorahrsdata = pRazorAHRSData[0]

    DestroyRazorAHRSData(pRazorAHRSData)

    return res, razorahrsdata

def ConnectRazorAHRS(pRazorAHRS, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "pRazorAHRS", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectRazorAHRSx', hDll), hApiParams)
    return function_call(pRazorAHRS, cfgFilePath.encode('UTF-8'))

def DisconnectRazorAHRS(pRazorAHRS):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRazorAHRS", 0),
    function_call = hApiProto(('DisconnectRazorAHRSx', hDll), hApiParams)
    return function_call(pRazorAHRS)

def GetLatestDataFromThreadRazorAHRS(pRazorAHRS):
    global hDll

    pRazorAHRSData = CreateRazorAHRSData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(RAZORAHRSDATA))
    hApiParams = (1, "pRazorAHRS", 0),(1, "pRazorAHRSData", 0),
    function_call = hApiProto(('GetLatestDataFromThreadRazorAHRSx', hDll), hApiParams)
    res = function_call(pRazorAHRS, pRazorAHRSData)
    
    razorahrsdata = pRazorAHRSData[0]

    DestroyRazorAHRSData(pRazorAHRSData)

    return res, razorahrsdata

def StartThreadRazorAHRS(pRazorAHRS):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRazorAHRS", 0),
    function_call = hApiProto(('StartThreadRazorAHRSx', hDll), hApiParams)
    return function_call(pRazorAHRS)

def StopThreadRazorAHRS(pRazorAHRS):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRazorAHRS", 0),
    function_call = hApiProto(('StopThreadRazorAHRSx', hDll), hApiParams)
    return function_call(pRazorAHRS)

class NMEADATA(ctypes.Structure):
    _fields_ = [("utc", ctypes.c_double), ("date", ctypes.c_double),
                ("pressure", ctypes.c_double), ("temperature", ctypes.c_double),
                ("cpressure", ctypes.c_char), ("ctemperature", ctypes.c_char),
                ("winddir", ctypes.c_double), ("windspeed", ctypes.c_double),
                ("cwinddir", ctypes.c_char), ("cwindspeed", ctypes.c_char),
                ("awinddir", ctypes.c_double), ("awindspeed", ctypes.c_double),
                ("cawinddir", ctypes.c_char), ("cawindspeed", ctypes.c_char),
                ("latdeg", ctypes.c_int), ("longdeg", ctypes.c_int),
                ("latmin", ctypes.c_double), ("longmin", ctypes.c_double),
                ("szlatdeg", ctypes.c_char*3), ("szlongdeg", ctypes.c_char*4),
                ("north", ctypes.c_char), ("east", ctypes.c_char),
                ("GPS_quality_indicator", ctypes.c_int),
                ("nbsat", ctypes.c_int),
                ("hdop", ctypes.c_double),
                ("height_geoid", ctypes.c_double),
                ("status", ctypes.c_char),
                ("posMode", ctypes.c_char),
                ("sog", ctypes.c_double), ("kph", ctypes.c_double), ("cog", ctypes.c_double), ("mag_cog", ctypes.c_double),
                ("heading", ctypes.c_double), ("deviation", ctypes.c_double), ("variation", ctypes.c_double),
                ("dev_east", ctypes.c_char), ("var_east", ctypes.c_char),
                ("rateofturn", ctypes.c_double),
                ("wplatdeg", ctypes.c_int), ("wplongdeg", ctypes.c_int),
                ("wplatmin", ctypes.c_double), ("wplongmin", ctypes.c_double),
                ("szwplatdeg", ctypes.c_char*3), ("szwplongdeg", ctypes.c_char*4),
                ("wpnorth", ctypes.c_char), ("wpeast", ctypes.c_char),
                ("szwpname", ctypes.c_char*64),
                ("totalrtemsg", ctypes.c_int), ("rtemsgnb", ctypes.c_int),
                ("rtemsgmode", ctypes.c_char),
                ("szrtewp1name", ctypes.c_char*64),
                ("szrtewp2name", ctypes.c_char*64),
                ("szrtewp3name", ctypes.c_char*64),
                ("szrtewp4name", ctypes.c_char*64),
                ("nbsentences", ctypes.c_int),
                ("sentence_number", ctypes.c_int),
                ("seqmsgid", ctypes.c_int),
                ("AIS_channel", ctypes.c_char),
                ("nbfillbits", ctypes.c_int),
                ("roll", ctypes.c_double), ("pitch", ctypes.c_double),
                ("salinity", ctypes.c_double),
                ("depth", ctypes.c_double),
                ("speedofsound", ctypes.c_double),
                ("vx_dvl", ctypes.c_double), ("vy_dvl", ctypes.c_double), ("vz_dvl", ctypes.c_double), ("verr_dvl", ctypes.c_double), ("vt_ship", ctypes.c_double), ("vl_ship", ctypes.c_double), ("vn_ship", ctypes.c_double), ("v_east", ctypes.c_double), ("v_north", ctypes.c_double), ("v_up", ctypes.c_double), 
                ("vstatus_dvl", ctypes.c_char), ("vstatus_ship", ctypes.c_char), ("vstatus_earth", ctypes.c_char),
                ("d_east", ctypes.c_double), ("d_north", ctypes.c_double),
                ("d_up", ctypes.c_double), ("rangetobottom", ctypes.c_double),
                ("timesincelastgood", ctypes.c_double),
                ("Latitude", ctypes.c_double),
                ("Longitude", ctypes.c_double),
                ("Altitude", ctypes.c_double),
                ("Altitude_AGL", ctypes.c_double),
                ("SOG", ctypes.c_double),
                ("COG", ctypes.c_double),
                ("year", ctypes.c_int), ("month", ctypes.c_int), ("day", ctypes.c_int), ("hour", ctypes.c_int), ("minute", ctypes.c_int),
                ("second", ctypes.c_double),
                ("Roll", ctypes.c_double),
                ("Pitch", ctypes.c_double),
                ("Heading", ctypes.c_double),
                ("RateOfTurn", ctypes.c_double),
                ("WindDir", ctypes.c_double),
                ("WindSpeed", ctypes.c_double),
                ("ApparentWindDir", ctypes.c_double),
                ("ApparentWindSpeed", ctypes.c_double),
                ("wpLatitude", ctypes.c_double),
                ("wpLongitude", ctypes.c_double),
                ("AIS_Latitude", ctypes.c_double),
                ("AIS_Longitude", ctypes.c_double),
                ("AIS_SOG", ctypes.c_double),
                ("AIS_COG", ctypes.c_double)]

def CreateNMEAData():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(NMEADATA))
    hApiParams = None
    function_call = hApiProto(('CreateNMEADatax', hDll), hApiParams)
    return function_call()

def DestroyNMEAData(pNMEAData):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(NMEADATA))
    hApiParams = (1, "pNMEAData", 0),
    function_call = hApiProto(('DestroyNMEADatax', hDll), hApiParams)
    function_call(pNMEAData)
    
def CreateNMEADevice():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('CreateNMEADevicex', hDll), hApiParams)
    return function_call()

def DestroyNMEADevice(pNMEADevice):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pNMEADevice", 0),
    function_call = hApiProto(('DestroyNMEADevicex', hDll), hApiParams)
    function_call(pNMEADevice)

def GetLatestDataNMEADevice(pNMEADevice):
    global hDll

    pNMEAData = CreateNMEAData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(NMEADATA))
    hApiParams = (1, "pNMEADevice", 0),(1, "pNMEAData", 0),
    function_call = hApiProto(('GetLatestDataNMEADevicex', hDll), hApiParams)
    res = function_call(pNMEADevice, pNMEAData)

    nmeadata = pNMEAData[0]

    DestroyNMEAData(pNMEAData)

    return res, nmeadata

def ConnectNMEADevice(pNMEADevice, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "pNMEADevice", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectNMEADevicex', hDll), hApiParams)
    return function_call(pNMEADevice, cfgFilePath.encode('UTF-8'))

def DisconnectNMEADevice(pNMEADevice):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pNMEADevice", 0),
    function_call = hApiProto(('DisconnectNMEADevicex', hDll), hApiParams)
    return function_call(pNMEADevice)

def GetLatestDataFromThreadNMEADevice(pNMEADevice):
    global hDll

    pNMEAData = CreateNMEAData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(NMEADATA))
    hApiParams = (1, "pNMEADevice", 0),(1, "pNMEAData", 0),
    function_call = hApiProto(('GetLatestDataFromThreadNMEADevicex', hDll), hApiParams)
    res = function_call(pNMEADevice, pNMEAData)

    nmeadata = pNMEAData[0]

    DestroyNMEAData(pNMEAData)

    return res, nmeadata

def StartThreadNMEADevice(pNMEADevice):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pNMEADevice", 0),
    function_call = hApiProto(('StartThreadNMEADevicex', hDll), hApiParams)
    return function_call(pNMEADevice)

def StopThreadNMEADevice(pNMEADevice):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pNMEADevice", 0),
    function_call = hApiProto(('StopThreadNMEADevicex', hDll), hApiParams)
    return function_call(pNMEADevice)

def Createublox():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('Createubloxx', hDll), hApiParams)
    return function_call()

def Destroyublox(publox):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "publox", 0),
    function_call = hApiProto(('Destroyubloxx', hDll), hApiParams)
    function_call(publox)

def GetNMEASentenceublox(publox):
    global hDll

    pNMEAData = CreateNMEAData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(NMEADATA))
    hApiParams = (1, "publox", 0),(1, "pNMEAData", 0),
    function_call = hApiProto(('GetNMEASentenceubloxx', hDll), hApiParams)
    res = function_call(publox, pNMEAData)

    nmeadata = pNMEAData[0]

    DestroyNMEAData(pNMEAData)

    return res, nmeadata

def Connectublox(publox, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "publox", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('Connectubloxx', hDll), hApiParams)
    return function_call(publox, cfgFilePath.encode('UTF-8'))

def Disconnectublox(publox):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "publox", 0),
    function_call = hApiProto(('Disconnectubloxx', hDll), hApiParams)
    return function_call(publox)

def GetNMEASentenceFromThreadublox(publox):
    global hDll

    pNMEAData = CreateNMEAData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(NMEADATA))
    hApiParams = (1, "publox", 0),(1, "pNMEAData", 0),
    function_call = hApiProto(('GetNMEASentenceFromThreadubloxx', hDll), hApiParams)
    res = function_call(publox, pNMEAData)

    nmeadata = pNMEAData[0]

    DestroyNMEAData(pNMEAData)

    return res, nmeadata

def StartNMEAThreadublox(publox):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "publox", 0),
    function_call = hApiProto(('StartNMEAThreadubloxx', hDll), hApiParams)
    return function_call(publox)

def StopNMEAThreadublox(publox):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "publox", 0),
    function_call = hApiProto(('StopNMEAThreadubloxx', hDll), hApiParams)
    return function_call(publox)

def CreateSSC32():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('CreateSSC32x', hDll), hApiParams)
    return function_call()

def DestroySSC32(pSSC32):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pSSC32", 0),
    function_call = hApiProto(('DestroySSC32x', hDll), hApiParams)
    function_call(pSSC32)

def GetVoltageSSC32(pSSC32, channel):
    global hDll

    pvoltage = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.POINTER(ctypes.c_double))
    hApiParams = (1, "pSSC32", 0),(1, "channel", 0),(1, "pvoltage", 0),
    function_call = hApiProto(('GetVoltageSSC32x', hDll), hApiParams)
    res = function_call(pSSC32, channel, pvoltage)
    return res, pvalue[0]

def GetDigitalInputSSC32(pSSC32, channel):
    global hDll

    pvalue = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pSSC32", 0),(1, "channel", 0),(1, "pvalue", 0),
    function_call = hApiProto(('GetDigitalInputSSC32x', hDll), hApiParams)
    res = function_call(pSSC32, channel, pvalue)
    return res, pvalue[0]

def GetPWMSSC32(pSSC32, channel):
    global hDll

    ppw = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pSSC32", 0),(1, "channel", 0),(1, "ppw", 0),
    function_call = hApiProto(('GetPWMSSC32x', hDll), hApiParams)
    res = function_call(pSSC32, channel, ppw)
    return res, ppw[0]

def SetPWMSSC32(pSSC32, channel, pw):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_int)
    hApiParams = (1, "pSSC32", 0),(1, "channel", 0),(1, "pw", 0),
    function_call = hApiProto(('SetPWMSSC32x', hDll), hApiParams)
    return function_call(pSSC32, channel, pw)

def SetAllPWMsSSC32(pSSC32, selectedchannels, pws):
    global hDll

    nbchannels = 32
    pselectedchannels = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        pselectedchannels[k] = selectedchannels[k]
    ppws = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        ppws[k] = pws[k]

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pSSC32", 0),(1, "pselectedchannels", 0),(1, "ppws", 0),
    function_call = hApiProto(('SetAllPWMsSSC32x', hDll), hApiParams)
    return function_call(pSSC32, pselectedchannels, ppws)

def SetDigitalOutputSSC32(pSSC32, channel, value):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_int)
    hApiParams = (1, "pSSC32", 0),(1, "channel", 0),(1, "value", 0),
    function_call = hApiProto(('SetDigitalOutputSSC32x', hDll), hApiParams)
    return function_call(pSSC32, channel, value)

def ConnectSSC32(pSSC32, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "pSSC32", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectSSC32x', hDll), hApiParams)
    return function_call(pSSC32, cfgFilePath.encode('UTF-8'))

def DisconnectSSC32(pSSC32):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pSSC32", 0),
    function_call = hApiProto(('DisconnectSSC32x', hDll), hApiParams)
    return function_call(pSSC32)

def SetAllPWMsFromThreadSSC32(pSSC32, selectedchannels, pws):
    global hDll

    nbchannels = 32
    pselectedchannels = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        pselectedchannels[k] = selectedchannels[k]
    ppws = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        ppws[k] = pws[k]

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pSSC32", 0),(1, "pselectedchannels", 0),(1, "ppws", 0),
    function_call = hApiProto(('SetAllPWMsFromThreadSSC32x', hDll), hApiParams)
    return function_call(pSSC32, pselectedchannels, ppws)

def StartThreadSSC32(pSSC32):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pSSC32", 0),
    function_call = hApiProto(('StartThreadSSC32x', hDll), hApiParams)
    return function_call(pSSC32)

def StopThreadSSC32(pSSC32):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pSSC32", 0),
    function_call = hApiProto(('StopThreadSSC32x', hDll), hApiParams)
    return function_call(pSSC32)

def CreatePololu():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('CreatePololux', hDll), hApiParams)
    return function_call()

def DestroyPololu(pPololu):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pPololu", 0),
    function_call = hApiProto(('DestroyPololux', hDll), hApiParams)
    function_call(pPololu)

def GetValuePololu(pPololu, channel):
    global hDll

    pvalue = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pPololu", 0),(1, "channel", 0),(1, "pvalue", 0),
    function_call = hApiProto(('GetValuePololux', hDll), hApiParams)
    res = function_call(pPololu, channel, pvalue)
    return res, pvalue[0]

def SetPWMPololu(pPololu, channel, pw):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_int)
    hApiParams = (1, "pPololu", 0),(1, "channel", 0),(1, "pw", 0),
    function_call = hApiProto(('SetPWMPololux', hDll), hApiParams)
    return function_call(pPololu, channel, pw)

def SetAllPWMsPololu(pPololu, selectedchannels, pws):
    global hDll

    nbchannels = 24
    pselectedchannels = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        pselectedchannels[k] = selectedchannels[k]
    ppws = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        ppws[k] = pws[k]

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pPololu", 0),(1, "pselectedchannels", 0),(1, "ppws", 0),
    function_call = hApiProto(('SetAllPWMsPololux', hDll), hApiParams)
    return function_call(pPololu, pselectedchannels, ppws)

def SetPWMJrkPololu(pPololu, pw):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int)
    hApiParams = (1, "pPololu", 0),(1, "pw", 0),
    function_call = hApiProto(('SetPWMJrkPololux', hDll), hApiParams)
    return function_call(pPololu, pw)

def ConnectPololu(pPololu, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "pPololu", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectPololux', hDll), hApiParams)
    return function_call(pPololu, cfgFilePath.encode('UTF-8'))

def DisconnectPololu(pPololu):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pPololu", 0),
    function_call = hApiProto(('DisconnectPololux', hDll), hApiParams)
    return function_call(pPololu)

def GetValueFromThreadPololu(pPololu, channel):
    global hDll

    pvalue = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pPololu", 0),(1, "channel", 0),(1, "pvalue", 0),
    function_call = hApiProto(('GetValueFromThreadPololux', hDll), hApiParams)
    res = function_call(pPololu, channel, pvalue)
    return res, pvalue[0]

def SetAllPWMsFromThreadPololu(pPololu, selectedchannels, pws):
    global hDll

    nbchannels = 24
    pselectedchannels = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        pselectedchannels[k] = selectedchannels[k]
    ppws = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        ppws[k] = pws[k]

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pPololu", 0),(1, "pselectedchannels", 0),(1, "ppws", 0),
    function_call = hApiProto(('SetAllPWMsFromThreadPololux', hDll), hApiParams)
    return function_call(pPololu, pselectedchannels, ppws)

def StartThreadPololu(pPololu):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pPololu", 0),
    function_call = hApiProto(('StartThreadPololux', hDll), hApiParams)
    return function_call(pPololu)

def StopThreadPololu(pPololu):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pPololu", 0),
    function_call = hApiProto(('StopThreadPololux', hDll), hApiParams)
    return function_call(pPololu)

def CreateHokuyo():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('CreateHokuyox', hDll), hApiParams)
    return function_call()

def DestroyHokuyo(pHokuyo):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pHokuyo", 0),
    function_call = hApiProto(('DestroyHokuyox', hDll), hApiParams)
    function_call(pHokuyo)

def k2angleHokuyo(pHokuyo, k):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int)
    hApiParams = (1, "pHokuyo", 0),(1, "k", 0),
    function_call = hApiProto(('k2angleHokuyox', hDll), hApiParams)
    return function_call(pHokuyo, k)

def angle2kHokuyo(pHokuyo, angle):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_double)
    hApiParams = (1, "pHokuyo", 0),(1, "angle", 0),
    function_call = hApiProto(('angle2kHokuyox', hDll), hApiParams)
    return function_call(pHokuyo, angle)

def GetLatestDataHokuyo(pHokuyo):
    global hDll

    n = 2048
    pdistances = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pangles = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))
    hApiParams = (1, "pHokuyo", 0),(1, "pdistances", 0),(1, "pangles", 0),
    function_call = hApiProto(('GetLatestDataHokuyox', hDll), hApiParams)
    res = function_call(pHokuyo, pdistances, pangles)
    return res, pdistances, pangles

def ConnectHokuyo(pHokuyo, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "pHokuyo", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectHokuyox', hDll), hApiParams)
    return function_call(pHokuyo, cfgFilePath.encode('UTF-8'))

def DisconnectHokuyo(pHokuyo):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pHokuyo", 0),
    function_call = hApiProto(('DisconnectHokuyox', hDll), hApiParams)
    return function_call(pHokuyo)

def GetLatestDataFromThreadHokuyo(pHokuyo):
    global hDll

    n = 2048
    pdistances = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pangles = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))
    hApiParams = (1, "pHokuyo", 0),(1, "pdistances", 0),(1, "pangles", 0),
    function_call = hApiProto(('GetLatestDataFromThreadHokuyox', hDll), hApiParams)
    res = function_call(pHokuyo, pdistances, pangles)
    return res, pdistances, pangles

def StartThreadHokuyo(pHokuyo):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pHokuyo", 0),
    function_call = hApiProto(('StartThreadHokuyox', hDll), hApiParams)
    return function_call(pHokuyo)

def StopThreadHokuyo(pHokuyo):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pHokuyo", 0),
    function_call = hApiProto(('StopThreadHokuyox', hDll), hApiParams)
    return function_call(pHokuyo)

def CreateRPLIDAR():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('CreateRPLIDARx', hDll), hApiParams)
    return function_call()

def DestroyRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('DestroyRPLIDARx', hDll), hApiParams)
    function_call(pRPLIDAR)

def GetScanDataResponseRPLIDAR(pRPLIDAR):
    global hDll

    pdistance = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?
    pangle = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?
    pbNewScan = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?
    pQuality = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pRPLIDAR", 0),(1, "pdistance", 0),(1, "pangle", 0),(1, "pbNewScan", 0),(1, "pQuality", 0),
    function_call = hApiProto(('GetScanDataResponseRPLIDARx', hDll), hApiParams)
    res = function_call(pRPLIDAR, pdistance, pangle, pbNewScan, pQuality)
    return res, pdistance[0], pangle[0], pbNewScan[0], pQuality[0]

def GetExpressScanDataResponseRPLIDAR(pRPLIDAR):
    global hDll

    n = 32
    pdistances = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pangles = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pbNewScan = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pRPLIDAR", 0),(1, "pdistances", 0),(1, "pangles", 0),(1, "pbNewScan", 0),
    function_call = hApiProto(('GetExpressScanDataResponseRPLIDARx', hDll), hApiParams)
    res = function_call(pRPLIDAR, pdistances, pangles, pbNewScan)
    return res, pdistances, pangles, pbNewScan[0]

def ConnectRPLIDAR(pRPLIDAR, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "pRPLIDAR", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR, cfgFilePath.encode('UTF-8'))

def DisconnectRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('DisconnectRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def GetScanDataResponseFromThreadRPLIDAR(pRPLIDAR):
    global hDll

    pdistance = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?
    pangle = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?
    pbNewScan = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?
    pQuality = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pRPLIDAR", 0),(1, "pdistance", 0),(1, "pangle", 0),(1, "pbNewScan", 0),(1, "pQuality", 0),
    function_call = hApiProto(('GetScanDataResponseFromThreadRPLIDARx', hDll), hApiParams)
    res = function_call(pRPLIDAR, pdistance, pangle, pbNewScan, pQuality)
    return res, pdistance[0], pangle[0], pbNewScan[0], pQuality[0]

def GetExpressScanDataResponseFromThreadRPLIDAR(pRPLIDAR):
    global hDll

    n = 32
    pdistances = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pangles = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pbNewScan = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pRPLIDAR", 0),(1, "pdistances", 0),(1, "pangles", 0),(1, "pbNewScan", 0),
    function_call = hApiProto(('GetExpressScanDataResponseFromThreadRPLIDARx', hDll), hApiParams)
    res = function_call(pRPLIDAR, pdistances, pangles, pbNewScan)
    return res, pdistances, pangles, pbNewScan[0]

def StartScanThreadRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StartScanThreadRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def StopScanThreadRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StopScanThreadRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def StartExpressScanThreadRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StartExpressScanThreadRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def StopExpressScanThreadRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StopExpressScanThreadRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)
