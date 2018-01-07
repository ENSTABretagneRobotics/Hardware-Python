from __future__ import print_function
import ctypes

class RAZORAHRSDATA(ctypes.Structure):
    _fields_ = [("yaw", ctypes.c_double), ("pitch", ctypes.c_double), ("roll", ctypes.c_double),
                ("accx", ctypes.c_double), ("accy", ctypes.c_double), ("accz", ctypes.c_double),
                ("gyrx", ctypes.c_double), ("gyry", ctypes.c_double), ("gyrz", ctypes.c_double),
                ("Roll", ctypes.c_double), ("Pitch", ctypes.c_double), ("Yaw", ctypes.c_double)]

def CreateRazorAHRSData():
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(RAZORAHRSDATA))
    hApiParams = None
    function_call = hApiProto(('CreateRazorAHRSDatax', hDll), hApiParams)
    return function_call()

def DestroyRazorAHRSData(pRazorAHRSData):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(RAZORAHRSDATA))
    hApiParams = (1, "pRazorAHRSData", 0),
    function_call = hApiProto(('DestroyRazorAHRSDatax', hDll), hApiParams)
    function_call(pRazorAHRSData)

def CreateRazorAHRS():
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('CreateRazorAHRSx', hDll), hApiParams)
    return function_call()

def DestroyRazorAHRS(pRazorAHRS):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRazorAHRS", 0),
    function_call = hApiProto(('DestroyRazorAHRSx', hDll), hApiParams)
    function_call(pRazorAHRS)

def GetLatestDataRazorAHRS(pRazorAHRS):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    pRazorAHRSData = CreateRazorAHRSData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(RAZORAHRSDATA))
    hApiParams = (1, "pRazorAHRS", 0),(1, "pRazorAHRSData", 0),
    function_call = hApiProto(('GetLatestDataRazorAHRSx', hDll), hApiParams)
    res = function_call(pRazorAHRS, pRazorAHRSData)
    
    razorahrsdata = pRazorAHRSData[0]

    DestroyRazorAHRSData(pRazorAHRSData)

    return res, razorahrsdata

def ConnectRazorAHRS(pRazorAHRS, cfgFilePath):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "pRazorAHRS", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectRazorAHRSx', hDll), hApiParams)
    return function_call(pRazorAHRS, cfgFilePath.encode('UTF-8'))

def DisconnectRazorAHRS(pRazorAHRS):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRazorAHRS", 0),
    function_call = hApiProto(('DisconnectRazorAHRSx', hDll), hApiParams)
    return function_call(pRazorAHRS)

def GetLatestDataFromThreadRazorAHRS(pRazorAHRS):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    pRazorAHRSData = CreateRazorAHRSData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(RAZORAHRSDATA))
    hApiParams = (1, "pRazorAHRS", 0),(1, "pRazorAHRSData", 0),
    function_call = hApiProto(('GetLatestDataFromThreadRazorAHRSx', hDll), hApiParams)
    res = function_call(pRazorAHRS, pRazorAHRSData)
    
    razorahrsdata = pRazorAHRSData[0]

    DestroyRazorAHRSData(pRazorAHRSData)

    return res, razorahrsdata

def StartThreadRazorAHRS(pRazorAHRS):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRazorAHRS", 0),
    function_call = hApiProto(('StartThreadRazorAHRSx', hDll), hApiParams)
    return function_call(pRazorAHRS)

def StopThreadRazorAHRS(pRazorAHRS):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

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
                ("WindDir", ctypes.c_double), 
                ("WindSpeed", ctypes.c_double),
                ("ApparentWindDir", ctypes.c_double), 
                ("ApparentWindSpeed", ctypes.c_double),
                ("AIS_Latitude", ctypes.c_double), 
                ("AIS_Longitude", ctypes.c_double),
                ("AIS_SOG", ctypes.c_double), 
                ("AIS_COG", ctypes.c_double)]

def CreateNMEAData():
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(NMEADATA))
    hApiParams = None
    function_call = hApiProto(('CreateNMEADatax', hDll), hApiParams)
    return function_call()

def DestroyNMEAData(pNMEAData):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(NMEADATA))
    hApiParams = (1, "pNMEAData", 0),
    function_call = hApiProto(('DestroyNMEADatax', hDll), hApiParams)
    function_call(pNMEAData)
    
def CreateNMEADevice():
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('CreateNMEADevicex', hDll), hApiParams)
    return function_call()

def DestroyNMEADevice(pNMEADevice):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pNMEADevice", 0),
    function_call = hApiProto(('DestroyNMEADevicex', hDll), hApiParams)
    function_call(pNMEADevice)

def GetLatestDataNMEADevice(pNMEADevice):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    pNMEAData = CreateNMEAData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(NMEADATA))
    hApiParams = (1, "pNMEADevice", 0),(1, "pNMEAData", 0),
    function_call = hApiProto(('GetLatestDataNMEADevicex', hDll), hApiParams)
    res = function_call(pNMEADevice, pNMEAData)

    nmeadata = pNMEAData[0]

    DestroyNMEAData(pNMEAData)

    return res, nmeadata

def ConnectNMEADevice(pNMEADevice, cfgFilePath):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "pNMEADevice", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectNMEADevicex', hDll), hApiParams)
    return function_call(pNMEADevice, cfgFilePath.encode('UTF-8'))

def DisconnectNMEADevice(pNMEADevice):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pNMEADevice", 0),
    function_call = hApiProto(('DisconnectNMEADevicex', hDll), hApiParams)
    return function_call(pNMEADevice)

def GetLatestDataFromThreadNMEADevice(pNMEADevice):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    pNMEAData = CreateNMEAData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(NMEADATA))
    hApiParams = (1, "pNMEADevice", 0),(1, "pNMEAData", 0),
    function_call = hApiProto(('GetLatestDataFromThreadNMEADevicex', hDll), hApiParams)
    res = function_call(pNMEADevice, pNMEAData)

    nmeadata = pNMEAData[0]

    DestroyNMEAData(pNMEAData)

    return res, nmeadata

def StartThreadNMEADevice(pNMEADevice):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pNMEADevice", 0),
    function_call = hApiProto(('StartThreadNMEADevicex', hDll), hApiParams)
    return function_call(pNMEADevice)

def StopThreadNMEADevice(pNMEADevice):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pNMEADevice", 0),
    function_call = hApiProto(('StopThreadNMEADevicex', hDll), hApiParams)
    return function_call(pNMEADevice)

def Createublox():
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('Createubloxx', hDll), hApiParams)
    return function_call()

def Destroyublox(publox):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "publox", 0),
    function_call = hApiProto(('Destroyubloxx', hDll), hApiParams)
    function_call(publox)

def GetNMEASentenceublox(publox):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    pNMEAData = CreateNMEAData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(NMEADATA))
    hApiParams = (1, "publox", 0),(1, "pNMEAData", 0),
    function_call = hApiProto(('GetNMEASentenceubloxx', hDll), hApiParams)
    res = function_call(publox, pNMEAData)

    nmeadata = pNMEAData[0]

    DestroyNMEAData(pNMEAData)

    return res, nmeadata

def Connectublox(publox, cfgFilePath):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "publox", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('Connectubloxx', hDll), hApiParams)
    return function_call(publox, cfgFilePath.encode('UTF-8'))

def Disconnectublox(publox):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "publox", 0),
    function_call = hApiProto(('Disconnectubloxx', hDll), hApiParams)
    return function_call(publox)

def GetNMEASentenceFromThreadublox(publox):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    pNMEAData = CreateNMEAData()

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(NMEADATA))
    hApiParams = (1, "publox", 0),(1, "pNMEAData", 0),
    function_call = hApiProto(('GetNMEASentenceFromThreadubloxx', hDll), hApiParams)
    res = function_call(publox, pNMEAData)

    nmeadata = pNMEAData[0]

    DestroyNMEAData(pNMEAData)

    return res, nmeadata

def StartNMEAThreadublox(publox):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "publox", 0),
    function_call = hApiProto(('StartNMEAThreadubloxx', hDll), hApiParams)
    return function_call(publox)

def StopNMEAThreadublox(publox):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "publox", 0),
    function_call = hApiProto(('StopNMEAThreadubloxx', hDll), hApiParams)
    return function_call(publox)

def CreateSSC32():
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('CreateSSC32x', hDll), hApiParams)
    return function_call()

def DestroySSC32(pSSC32):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pSSC32", 0),
    function_call = hApiProto(('DestroySSC32x', hDll), hApiParams)
    function_call(pSSC32)

def SetPWMSSC32(pSSC32, channel, pw):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_int)
    hApiParams = (1, "pSSC32", 0),(1, "channel", 0),(1, "pw", 0),
    function_call = hApiProto(('SetPWMSSC32x', hDll), hApiParams)
    return function_call(pSSC32, channel, pw)

def SetAllPWMsSSC32(pSSC32, selectedchannels, pws):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    nbchannels = 5
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

def ConnectSSC32(pSSC32, cfgFilePath):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "pSSC32", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectSSC32x', hDll), hApiParams)
    return function_call(pSSC32, cfgFilePath.encode('UTF-8'))

def DisconnectSSC32(pSSC32):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pSSC32", 0),
    function_call = hApiProto(('DisconnectSSC32x', hDll), hApiParams)
    return function_call(pSSC32)

def SetAllPWMsFromThreadSSC32(pSSC32, selectedchannels, pws):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    nbchannels = 5
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
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pSSC32", 0),
    function_call = hApiProto(('StartThreadSSC32x', hDll), hApiParams)
    return function_call(pSSC32)

def StopThreadSSC32(pSSC32):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pSSC32", 0),
    function_call = hApiProto(('StopThreadSSC32x', hDll), hApiParams)
    return function_call(pSSC32)

def CreateMaestro():
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('CreateMaestrox', hDll), hApiParams)
    return function_call()

def DestroyMaestro(pMaestro):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pMaestro", 0),
    function_call = hApiProto(('DestroyMaestrox', hDll), hApiParams)
    function_call(pMaestro)

def GetValueMaestro(pMaestro, channel):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    pvalue = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pMaestro", 0),(1, "channel", 0),(1, "pvalue", 0),
    function_call = hApiProto(('GetValueMaestrox', hDll), hApiParams)
    res = function_call(pMaestro, channel, pvalue)
    return res, pvalue[0]

def SetPWMMaestro(pMaestro, channel, pw):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_int)
    hApiParams = (1, "pMaestro", 0),(1, "channel", 0),(1, "pw", 0),
    function_call = hApiProto(('SetPWMMaestrox', hDll), hApiParams)
    return function_call(pMaestro, channel, pw)

def SetAllPWMsMaestro(pMaestro, selectedchannels, pws):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    nbchannels = 5
    pselectedchannels = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        pselectedchannels[k] = selectedchannels[k]
    ppws = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        ppws[k] = pws[k]

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pMaestro", 0),(1, "pselectedchannels", 0),(1, "ppws", 0),
    function_call = hApiProto(('SetAllPWMsMaestrox', hDll), hApiParams)
    return function_call(pMaestro, pselectedchannels, ppws)

def ConnectMaestro(pMaestro, cfgFilePath):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "pMaestro", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectMaestrox', hDll), hApiParams)
    return function_call(pMaestro, cfgFilePath.encode('UTF-8'))

def DisconnectMaestro(pMaestro):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pMaestro", 0),
    function_call = hApiProto(('DisconnectMaestrox', hDll), hApiParams)
    return function_call(pMaestro)

def GetValueFromThreadMaestro(pMaestro, channel):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    pvalue = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pMaestro", 0),(1, "channel", 0),(1, "pvalue", 0),
    function_call = hApiProto(('GetValueFromThreadMaestrox', hDll), hApiParams)
    res = function_call(pMaestro, channel, pvalue)
    return res, pvalue[0]

def SetAllPWMsFromThreadMaestro(pMaestro, selectedchannels, pws):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    nbchannels = 5
    pselectedchannels = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        pselectedchannels[k] = selectedchannels[k]
    ppws = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        ppws[k] = pws[k]

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pMaestro", 0),(1, "pselectedchannels", 0),(1, "ppws", 0),
    function_call = hApiProto(('SetAllPWMsFromThreadMaestrox', hDll), hApiParams)
    return function_call(pMaestro, pselectedchannels, ppws)

def StartThreadMaestro(pMaestro):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pMaestro", 0),
    function_call = hApiProto(('StartThreadMaestrox', hDll), hApiParams)
    return function_call(pMaestro)

def StopThreadMaestro(pMaestro):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pMaestro", 0),
    function_call = hApiProto(('StopThreadMaestrox', hDll), hApiParams)
    return function_call(pMaestro)

def CreateHokuyo():
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('CreateHokuyox', hDll), hApiParams)
    return function_call()

def DestroyHokuyo(pHokuyo):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pHokuyo", 0),
    function_call = hApiProto(('DestroyHokuyox', hDll), hApiParams)
    function_call(pHokuyo)

def k2angleHokuyo(pHokuyo, k):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int)
    hApiParams = (1, "pHokuyo", 0),(1, "k", 0),
    function_call = hApiProto(('k2angleHokuyox', hDll), hApiParams)
    return function_call(pHokuyo, k)

def angle2kHokuyo(pHokuyo, angle):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_double)
    hApiParams = (1, "pHokuyo", 0),(1, "angle", 0),
    function_call = hApiProto(('angle2kHokuyox', hDll), hApiParams)
    return function_call(pHokuyo, angle)

def GetLatestDataHokuyo(pHokuyo):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    n = 2048
    pdistances = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pangles = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))
    hApiParams = (1, "pHokuyo", 0),(1, "pdistances", 0),(1, "pangles", 0),
    function_call = hApiProto(('GetLatestDataHokuyox', hDll), hApiParams)
    res = function_call(pHokuyo, pdistances, pangles)
    return res, pdistances, pangles

def ConnectHokuyo(pHokuyo, cfgFilePath):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "pHokuyo", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectHokuyox', hDll), hApiParams)
    return function_call(pHokuyo, cfgFilePath.encode('UTF-8'))

def DisconnectHokuyo(pHokuyo):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pHokuyo", 0),
    function_call = hApiProto(('DisconnectHokuyox', hDll), hApiParams)
    return function_call(pHokuyo)

def GetLatestDataFromThreadHokuyo(pHokuyo):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    n = 2048
    pdistances = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pangles = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))
    hApiParams = (1, "pHokuyo", 0),(1, "pdistances", 0),(1, "pangles", 0),
    function_call = hApiProto(('GetLatestDataFromThreadHokuyox', hDll), hApiParams)
    res = function_call(pHokuyo, pdistances, pangles)
    return res, pdistances, pangles

def StartThreadHokuyo(pHokuyo):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pHokuyo", 0),
    function_call = hApiProto(('StartThreadHokuyox', hDll), hApiParams)
    return function_call(pHokuyo)

def StopThreadHokuyo(pHokuyo):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pHokuyo", 0),
    function_call = hApiProto(('StopThreadHokuyox', hDll), hApiParams)
    return function_call(pHokuyo)

def CreateRPLIDAR():
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_void_p))
    hApiParams = None
    function_call = hApiProto(('CreateRPLIDARx', hDll), hApiParams)
    return function_call()

def DestroyRPLIDAR(pRPLIDAR):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('DestroyRPLIDARx', hDll), hApiParams)
    function_call(pRPLIDAR)

def GetExpressScanDataResponseRPLIDAR(pRPLIDAR):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    n = 32
    pdistances = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pangles = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pbNewScan = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pRPLIDAR", 0),(1, "pdistances", 0),(1, "pangles", 0),(1, "pbNewScan", 0),
    function_call = hApiProto(('GetExpressScanDataResponseRPLIDARx', hDll), hApiParams)
    res = function_call(pRPLIDAR, pdistances, pangles, pbNewScan)
    return res, pdistances, pangles, pbNewScan[0]

def ConnectRPLIDAR(pRPLIDAR, cfgFilePath):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p)
    hApiParams = (1, "pRPLIDAR", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR, cfgFilePath.encode('UTF-8'))

def DisconnectRPLIDAR(pRPLIDAR):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('DisconnectRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def GetExpressScanDataResponseFromThreadRPLIDAR(pRPLIDAR):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    n = 32
    pdistances = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pangles = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pbNewScan = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pRPLIDAR", 0),(1, "pdistances", 0),(1, "pangles", 0),(1, "pbNewScan", 0),
    function_call = hApiProto(('GetExpressScanDataResponseFromThreadRPLIDARx', hDll), hApiParams)
    res = function_call(pRPLIDAR, pdistances, pangles, pbNewScan)
    return res, pdistances, pangles, pbNewScan[0]

def StartThreadRPLIDAR(pRPLIDAR):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StartThreadRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def StopThreadRPLIDAR(pRPLIDAR):
 
    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("hardwarex.dll")

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StopThreadRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)
