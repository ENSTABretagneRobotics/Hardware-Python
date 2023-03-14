from __future__ import print_function
import ctypes
from ctypes import util
import sys, os

# Load DLL into memory.
is_64bits = sys.maxsize > 2**32
if sys.platform.startswith('win'):
    try:
        if is_64bits:
            #hDll = ctypes.CDLL("x64/hardwarex.dll", winmode=True) # winmode=True necessary since Python 3.8 but not available in previous...
            if "add_dll_directory" in dir(os):
                os.add_dll_directory(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'x64'))
            else:
                os.environ['PATH'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'x64') + ';' + os.environ['PATH']
            # Should specify full path instead...? Less interesting if there are other necessary libraries in the folder...
            #hDll = ctypes.CDLL(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'x64/hardwarex.dll'))
        else:
            #hDll = ctypes.CDLL("x86/hardwarex.dll", winmode=True) # winmode=True necessary since Python 3.8 but not available in previous...
            if "add_dll_directory" in dir(os):
                os.add_dll_directory(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'x86'))
            else:
                os.environ['PATH'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'x86') + ';' + os.environ['PATH']
            # Should specify full path instead...? Less interesting if there are other necessary libraries in the folder...
            #hDll = ctypes.CDLL(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'x86/hardwarex.dll'))
        hDll = ctypes.CDLL("hardwarex.dll")
    except Exception:
        try:
            hDll = ctypes.CDLL(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.join('lib', 'hardwarex.dll')))
        except Exception:
            # Not sure what it does...
            sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
            hDll = ctypes.CDLL(ctypes.util.find_library("hardwarex"))
elif sys.platform.startswith('linux'):
    try:
        #os.environ['LD_LIBRARY_PATH'] = os.path.dirname(os.path.realpath(__file__)) + ':' + os.environ['LD_LIBRARY_PATH'] # Not taken into account by ctypes when set here (but OK if set before calling python in the terminal)...? See https://stackoverflow.com/questions/856116/changing-ld-library-path-at-runtime-for-ctypes. Setting rpath using patchelf in the library might help finding other necessary libraries if needed...
        hDll = ctypes.CDLL(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.join('linux_x64', 'hardwarex.so')))
    except Exception:
        try:
            hDll = ctypes.CDLL(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.join('lib', 'hardwarex.so')))
        except Exception:
            # Not sure what it does...
            sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
            hDll = ctypes.CDLL(ctypes.util.find_library("hardwarex"))
elif sys.platform.startswith('darwin'):
    try:
        #os.environ['DYLD_LIBRARY_PATH'] = os.path.dirname(os.path.realpath(__file__)) + ':' + os.environ['DYLD_LIBRARY_PATH'] # Not allowed to change here...?
        hDll = ctypes.CDLL(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.join('mac', 'hardwarex.dylib')))
    except Exception:
        try:
            hDll = ctypes.CDLL(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.join('lib', 'hardwarex.dylib')))
        except Exception:
            # Not sure what it does...
            sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
            hDll = ctypes.CDLL(ctypes.util.find_library("hardwarex"))
else:
    # Not sure what it does...
    sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
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
                ("heave_period", ctypes.c_double),
                ("surge", ctypes.c_double), ("sway", ctypes.c_double), ("heave", ctypes.c_double),
                ("surge_accel", ctypes.c_double), ("sway_accel", ctypes.c_double), ("heave_accel", ctypes.c_double),
                ("surge_vel", ctypes.c_double), ("sway_vel", ctypes.c_double), ("heave_vel", ctypes.c_double),
                ("odometerVelocity", ctypes.c_double),
                ("gpsRawData", ctypes.c_ubyte*4086),
                ("gpsRawDataSize", ctypes.c_uint),
                ("Status", ctypes.c_ubyte),
                ("TS", ctypes.c_uint),
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
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_void_p)
    hApiParams = None
    function_call = hApiProto(('CreateSBGx', hDll), hApiParams)
    return function_call()

def DestroySBG(pSBG):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
    hApiParams = (1, "pSBG", 0),
    function_call = hApiProto(('DestroySBGx', hDll), hApiParams)
    function_call(pSBG)

def GetLatestDataSBG(pSBG):
    global hDll

    pSBGData = (SBGDATA*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(SBGDATA))
    hApiParams = (1, "pSBG", 0),(1, "pSBGData", 0),
    function_call = hApiProto(('GetLatestDataSBGx', hDll), hApiParams)
    res = function_call(pSBG, pSBGData)
    return res, pSBGData[0]

def ConnectSBG(pSBG, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)
    hApiParams = (1, "pSBG", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectSBGx', hDll), hApiParams)
    return function_call(pSBG, cfgFilePath.encode('UTF-8'))

def DisconnectSBG(pSBG):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pSBG", 0),
    function_call = hApiProto(('DisconnectSBGx', hDll), hApiParams)
    return function_call(pSBG)

def GetLatestDataFromThreadSBG(pSBG):
    global hDll

    pSBGData = (SBGDATA*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(SBGDATA))
    hApiParams = (1, "pSBG", 0),(1, "pSBGData", 0),
    function_call = hApiProto(('GetLatestDataFromThreadSBGx', hDll), hApiParams)
    res = function_call(pSBG, pSBGData)
    return res, pSBGData[0]

def StartThreadSBG(pSBG):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pSBG", 0),
    function_call = hApiProto(('StartThreadSBGx', hDll), hApiParams)
    return function_call(pSBG)

def StopThreadSBG(pSBG):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
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
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_void_p)
    hApiParams = None
    function_call = hApiProto(('CreateMTx', hDll), hApiParams)
    return function_call()

def DestroyMT(pMT):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
    hApiParams = (1, "pMT", 0),
    function_call = hApiProto(('DestroyMTx', hDll), hApiParams)
    function_call(pMT)

def GetLatestDataMT(pMT):
    global hDll

    pMTData = (MTDATA*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(MTDATA))
    hApiParams = (1, "pMT", 0),(1, "pMTData", 0),
    function_call = hApiProto(('GetLatestDataMTx', hDll), hApiParams)
    res = function_call(pMT, pMTData)
    return res, pMTData[0]

def ConnectMT(pMT, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)
    hApiParams = (1, "pMT", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectMTx', hDll), hApiParams)
    return function_call(pMT, cfgFilePath.encode('UTF-8'))

def DisconnectMT(pMT):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pMT", 0),
    function_call = hApiProto(('DisconnectMTx', hDll), hApiParams)
    return function_call(pMT)

def GetLatestDataFromThreadMT(pMT):
    global hDll

    pMTData = (MTDATA*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(MTDATA))
    hApiParams = (1, "pMT", 0),(1, "pMTData", 0),
    function_call = hApiProto(('GetLatestDataFromThreadMTx', hDll), hApiParams)
    res = function_call(pMT, pMTData)
    return res, pMTData[0]

def StartThreadMT(pMT):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pMT", 0),
    function_call = hApiProto(('StartThreadMTx', hDll), hApiParams)
    return function_call(pMT)

def StopThreadMT(pMT):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
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
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_void_p)
    hApiParams = None
    function_call = hApiProto(('CreateRazorAHRSx', hDll), hApiParams)
    return function_call()

def DestroyRazorAHRS(pRazorAHRS):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
    hApiParams = (1, "pRazorAHRS", 0),
    function_call = hApiProto(('DestroyRazorAHRSx', hDll), hApiParams)
    function_call(pRazorAHRS)

def GetLatestDataRazorAHRS(pRazorAHRS):
    global hDll

    pRazorAHRSData = (RAZORAHRSDATA*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(RAZORAHRSDATA))
    hApiParams = (1, "pRazorAHRS", 0),(1, "pRazorAHRSData", 0),
    function_call = hApiProto(('GetLatestDataRazorAHRSx', hDll), hApiParams)
    res = function_call(pRazorAHRS, pRazorAHRSData)
    return res, pRazorAHRSData[0]

def ConnectRazorAHRS(pRazorAHRS, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)
    hApiParams = (1, "pRazorAHRS", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectRazorAHRSx', hDll), hApiParams)
    return function_call(pRazorAHRS, cfgFilePath.encode('UTF-8'))

def DisconnectRazorAHRS(pRazorAHRS):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRazorAHRS", 0),
    function_call = hApiProto(('DisconnectRazorAHRSx', hDll), hApiParams)
    return function_call(pRazorAHRS)

def GetLatestDataFromThreadRazorAHRS(pRazorAHRS):
    global hDll

    pRazorAHRSData = (RAZORAHRSDATA*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(RAZORAHRSDATA))
    hApiParams = (1, "pRazorAHRS", 0),(1, "pRazorAHRSData", 0),
    function_call = hApiProto(('GetLatestDataFromThreadRazorAHRSx', hDll), hApiParams)
    res = function_call(pRazorAHRS, pRazorAHRSData)
    return res, pRazorAHRSData[0]

def StartThreadRazorAHRS(pRazorAHRS):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRazorAHRS", 0),
    function_call = hApiProto(('StartThreadRazorAHRSx', hDll), hApiParams)
    return function_call(pRazorAHRS)

def StopThreadRazorAHRS(pRazorAHRS):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRazorAHRS", 0),
    function_call = hApiProto(('StopThreadRazorAHRSx', hDll), hApiParams)
    return function_call(pRazorAHRS)

def CreateMDM():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_void_p)
    hApiParams = None
    function_call = hApiProto(('CreateMDMx', hDll), hApiParams)
    return function_call()

def DestroyMDM(pMDM):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
    hApiParams = (1, "pMDM", 0),
    function_call = hApiProto(('DestroyMDMx', hDll), hApiParams)
    function_call(pMDM)

def SendDataMDM(pMDM, buf, buflen):
    global hDll
    
    pbuf = (ctypes.c_ubyte*(buflen))() # Memory leak here, rely on garbage collector?
    for k in range(buflen):
        pbuf[k] = ctypes.c_ubyte(int(buf[k]))
    pSentBytes = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int, ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pMDM", 0),(1, "pbuf", 0),(1, "buflen", 0),(1, "pSentBytes", 0),
    function_call = hApiProto(('SendDataMDMx', hDll), hApiParams)
    res = function_call(pMDM, pbuf, buflen, pSentBytes)
    return res, pSentBytes[0]

def RecvDataMDM(pMDM, buf, buflen):
    global hDll
    
    pbuf = (ctypes.c_ubyte*(buflen))() # Memory leak here, rely on garbage collector?
    for k in range(buflen):
        pbuf[k] = ctypes.c_ubyte(int(buf[k]))
    pReceivedBytes = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int, ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pMDM", 0),(1, "pbuf", 0),(1, "buflen", 0),(1, "pReceivedBytes", 0),
    function_call = hApiProto(('RecvDataMDMx', hDll), hApiParams)
    res = function_call(pMDM, pbuf, buflen, pReceivedBytes)
    for k in range(buflen):
        buf[k] = pbuf[k]
    return res, buf, pReceivedBytes[0]

def PurgeDataMDM(pMDM):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pMDM", 0),
    function_call = hApiProto(('PurgeDataMDMx', hDll), hApiParams)
    res = function_call(pMDM)
    return res

def ConnectMDM(pMDM, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)
    hApiParams = (1, "pMDM", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectMDMx', hDll), hApiParams)
    return function_call(pMDM, cfgFilePath.encode('UTF-8'))

def DisconnectMDM(pMDM):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pMDM", 0),
    function_call = hApiProto(('DisconnectMDMx', hDll), hApiParams)
    return function_call(pMDM)

def CreateP33x():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_void_p)
    hApiParams = None
    function_call = hApiProto(('CreateP33xx', hDll), hApiParams)
    return function_call()

def DestroyP33x(pP33x):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
    hApiParams = (1, "pP33x", 0),
    function_call = hApiProto(('DestroyP33xx', hDll), hApiParams)
    function_call(pP33x)

def GetPressureP33x(pP33x):
    global hDll
    
    pPressure = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double))
    hApiParams = (1, "pP33x", 0),(1, "pPressure", 0),
    function_call = hApiProto(('GetPressureP33xx', hDll), hApiParams)
    res = function_call(pP33x, pPressure)
    return res, pPressure[0]

def GetTemperatureP33x(pP33x):
    global hDll
    
    pTemperature = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double))
    hApiParams = (1, "pP33x", 0),(1, "pTemperature", 0),
    function_call = hApiProto(('GetTemperatureP33xx', hDll), hApiParams)
    res = function_call(pP33x, pTemperature)
    return res, pTemperature[0]

def ConnectP33x(pP33x, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)
    hApiParams = (1, "pP33x", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectP33xx', hDll), hApiParams)
    return function_call(pP33x, cfgFilePath.encode('UTF-8'))

def DisconnectP33x(pP33x):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pP33x", 0),
    function_call = hApiProto(('DisconnectP33xx', hDll), hApiParams)
    return function_call(pP33x)

def GetPressureFromThreadP33x(pP33x):
    global hDll
    
    pPressure = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double))
    hApiParams = (1, "pP33x", 0),(1, "pPressure", 0),
    function_call = hApiProto(('GetPressureFromThreadP33xx', hDll), hApiParams)
    res = function_call(pP33x, pPressure)
    return res, pPressure[0]

def GetTemperatureFromThreadP33x(pP33x):
    global hDll
    
    pTemperature = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double))
    hApiParams = (1, "pP33x", 0),(1, "pTemperature", 0),
    function_call = hApiProto(('GetTemperatureFromThreadP33xx', hDll), hApiParams)
    res = function_call(pP33x, pTemperature)
    return res, pTemperature[0]

def StartThreadP33x(pP33x):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pP33x", 0),
    function_call = hApiProto(('StartThreadP33xx', hDll), hApiParams)
    return function_call(pP33x)

def StopThreadP33x(pP33x):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pP33x", 0),
    function_call = hApiProto(('StopThreadP33xx', hDll), hApiParams)
    return function_call(pP33x)

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
                ("d_east", ctypes.c_double), ("d_north", ctypes.c_double), ("d_up", ctypes.c_double), ("rangetobottom", ctypes.c_double),
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
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_void_p)
    hApiParams = None
    function_call = hApiProto(('CreateNMEADevicex', hDll), hApiParams)
    return function_call()

def DestroyNMEADevice(pNMEADevice):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
    hApiParams = (1, "pNMEADevice", 0),
    function_call = hApiProto(('DestroyNMEADevicex', hDll), hApiParams)
    function_call(pNMEADevice)

def GetLatestDataNMEADevice(pNMEADevice):
    global hDll

    pNMEAData = (NMEADATA*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(NMEADATA))
    hApiParams = (1, "pNMEADevice", 0),(1, "pNMEAData", 0),
    function_call = hApiProto(('GetLatestDataNMEADevicex', hDll), hApiParams)
    res = function_call(pNMEADevice, pNMEAData)
    return res, pNMEAData[0]

def ConnectNMEADevice(pNMEADevice, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)
    hApiParams = (1, "pNMEADevice", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectNMEADevicex', hDll), hApiParams)
    return function_call(pNMEADevice, cfgFilePath.encode('UTF-8'))

def DisconnectNMEADevice(pNMEADevice):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pNMEADevice", 0),
    function_call = hApiProto(('DisconnectNMEADevicex', hDll), hApiParams)
    return function_call(pNMEADevice)

def GetLatestDataFromThreadNMEADevice(pNMEADevice):
    global hDll

    pNMEAData = (NMEADATA*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(NMEADATA))
    hApiParams = (1, "pNMEADevice", 0),(1, "pNMEAData", 0),
    function_call = hApiProto(('GetLatestDataFromThreadNMEADevicex', hDll), hApiParams)
    res = function_call(pNMEADevice, pNMEAData)
    return res, pNMEAData[0]

def StartThreadNMEADevice(pNMEADevice):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pNMEADevice", 0),
    function_call = hApiProto(('StartThreadNMEADevicex', hDll), hApiParams)
    return function_call(pNMEADevice)

def StopThreadNMEADevice(pNMEADevice):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pNMEADevice", 0),
    function_call = hApiProto(('StopThreadNMEADevicex', hDll), hApiParams)
    return function_call(pNMEADevice)

#class UBXDATA(ctypes.Structure):
#    _pack_ = 1
#    _fields_ = ...

def Createublox():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_void_p)
    hApiParams = None
    function_call = hApiProto(('Createubloxx', hDll), hApiParams)
    return function_call()

def Destroyublox(publox):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
    hApiParams = (1, "publox", 0),
    function_call = hApiProto(('Destroyubloxx', hDll), hApiParams)
    function_call(publox)

def GetNMEASentenceublox(publox):
    global hDll

    pNMEAData = (NMEADATA*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(NMEADATA))
    hApiParams = (1, "publox", 0),(1, "pNMEAData", 0),
    function_call = hApiProto(('GetNMEASentenceubloxx', hDll), hApiParams)
    res = function_call(publox, pNMEAData)
    return res, pNMEAData[0]

def Connectublox(publox, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)
    hApiParams = (1, "publox", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('Connectubloxx', hDll), hApiParams)
    return function_call(publox, cfgFilePath.encode('UTF-8'))

def Disconnectublox(publox):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "publox", 0),
    function_call = hApiProto(('Disconnectubloxx', hDll), hApiParams)
    return function_call(publox)

def GetNMEASentenceFromThreadublox(publox):
    global hDll

    pNMEAData = (NMEADATA*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(NMEADATA))
    hApiParams = (1, "publox", 0),(1, "pNMEAData", 0),
    function_call = hApiProto(('GetNMEASentenceFromThreadubloxx', hDll), hApiParams)
    res = function_call(publox, pNMEAData)
    return res, pNMEAData[0]

def StartNMEAThreadublox(publox):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "publox", 0),
    function_call = hApiProto(('StartNMEAThreadubloxx', hDll), hApiParams)
    return function_call(publox)

def StopNMEAThreadublox(publox):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "publox", 0),
    function_call = hApiProto(('StopNMEAThreadubloxx', hDll), hApiParams)
    return function_call(publox)

def CreateIM483I():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_void_p)
    hApiParams = None
    function_call = hApiProto(('CreateIM483Ix', hDll), hApiParams)
    return function_call()

def DestroyIM483I(pIM483I):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
    hApiParams = (1, "pIM483I", 0),
    function_call = hApiProto(('DestroyIM483Ix', hDll), hApiParams)
    function_call(pIM483I)

def SetMotorTorqueIM483I(pIM483I, holdpercent, runpercent):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)
    hApiParams = (1, "pIM483I", 0),(1, "holdpercent", 0),(1, "runpercent", 0),
    function_call = hApiProto(('SetMotorTorqueIM483Ix', hDll), hApiParams)
    return function_call(pIM483I, holdpercent, runpercent)

def SetMotorSpeedIM483I(pIM483I, val):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)
    hApiParams = (1, "pIM483I", 0),(1, "val", 0),
    function_call = hApiProto(('SetMotorSpeedIM483Ix', hDll), hApiParams)
    return function_call(pIM483I, val)

def SetMotorRelativeIM483I(pIM483I, val, bForce):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)
    hApiParams = (1, "pIM483I", 0),(1, "val", 0),(1, "bForce", 0),
    function_call = hApiProto(('SetMotorSpeedIM483Ix', hDll), hApiParams)
    return function_call(pIM483I, val, bForce)

def SetMotorOriginIM483I(pIM483I):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pIM483I", 0),
    function_call = hApiProto(('SetMotorOriginIM483Ix', hDll), hApiParams)
    return function_call(pIM483I)

def SetMaxAngleIM483I(pIM483I, angle):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_double)
    hApiParams = (1, "pIM483I", 0),(1, "angle", 0),
    function_call = hApiProto(('SetMaxAngleIM483Ix', hDll), hApiParams)
    return function_call(pIM483I, angle)

def CalibrateIM483I(pIM483I):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pIM483I", 0),
    function_call = hApiProto(('CalibrateIM483Ix', hDll), hApiParams)
    return function_call(pIM483I)

def ConnectIM483I(pIM483I, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)
    hApiParams = (1, "pIM483I", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectIM483Ix', hDll), hApiParams)
    return function_call(pIM483I, cfgFilePath.encode('UTF-8'))

def DisconnectIM483I(pIM483I):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pIM483I", 0),
    function_call = hApiProto(('DisconnectIM483Ix', hDll), hApiParams)
    return function_call(pIM483I)

def SetMaxAngleFromThreadIM483I(pIM483I, angle):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_double)
    hApiParams = (1, "pIM483I", 0),(1, "angle", 0),
    function_call = hApiProto(('SetMaxAngleFromThreadIM483Ix', hDll), hApiParams)
    return function_call(pIM483I, angle)

def StartThreadIM483I(pIM483I):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pIM483I", 0),
    function_call = hApiProto(('StartThreadIM483Ix', hDll), hApiParams)
    return function_call(pIM483I)

def StopThreadIM483I(pIM483I):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pIM483I", 0),
    function_call = hApiProto(('StopThreadIM483Ix', hDll), hApiParams)
    return function_call(pIM483I)

def CreateSSC32():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_void_p)
    hApiParams = None
    function_call = hApiProto(('CreateSSC32x', hDll), hApiParams)
    return function_call()

def DestroySSC32(pSSC32):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
    hApiParams = (1, "pSSC32", 0),
    function_call = hApiProto(('DestroySSC32x', hDll), hApiParams)
    function_call(pSSC32)

def GetVoltageSSC32(pSSC32, channel):
    global hDll

    pvoltage = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_double))
    hApiParams = (1, "pSSC32", 0),(1, "channel", 0),(1, "pvoltage", 0),
    function_call = hApiProto(('GetVoltageSSC32x', hDll), hApiParams)
    res = function_call(pSSC32, channel, pvoltage)
    return res, pvoltage[0]

def GetDigitalInputSSC32(pSSC32, channel):
    global hDll

    pValue = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pSSC32", 0),(1, "channel", 0),(1, "pValue", 0),
    function_call = hApiProto(('GetDigitalInputSSC32x', hDll), hApiParams)
    res = function_call(pSSC32, channel, pValue)
    return res, pValue[0]

def GetPWMSSC32(pSSC32, channel):
    global hDll

    ppw = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pSSC32", 0),(1, "channel", 0),(1, "ppw", 0),
    function_call = hApiProto(('GetPWMSSC32x', hDll), hApiParams)
    res = function_call(pSSC32, channel, ppw)
    return res, ppw[0]

def SetPWMSSC32(pSSC32, channel, pw):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)
    hApiParams = (1, "pSSC32", 0),(1, "channel", 0),(1, "pw", 0),
    function_call = hApiProto(('SetPWMSSC32x', hDll), hApiParams)
    return function_call(pSSC32, channel, pw)

def SetAllPWMsSSC32(pSSC32, selectedchannels, pws):
    global hDll

    nbchannels = 32
    pselectedchannels = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        pselectedchannels[k] = ctypes.c_int(int(selectedchannels[k]))
    ppws = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        ppws[k] = ctypes.c_int(pws[k])

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pSSC32", 0),(1, "pselectedchannels", 0),(1, "ppws", 0),
    function_call = hApiProto(('SetAllPWMsSSC32x', hDll), hApiParams)
    return function_call(pSSC32, pselectedchannels, ppws)

def SetDigitalOutputSSC32(pSSC32, channel, value):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)
    hApiParams = (1, "pSSC32", 0),(1, "channel", 0),(1, "value", 0),
    function_call = hApiProto(('SetDigitalOutputSSC32x', hDll), hApiParams)
    return function_call(pSSC32, channel, value)

def ConnectSSC32(pSSC32, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)
    hApiParams = (1, "pSSC32", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectSSC32x', hDll), hApiParams)
    return function_call(pSSC32, cfgFilePath.encode('UTF-8'))

def DisconnectSSC32(pSSC32):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pSSC32", 0),
    function_call = hApiProto(('DisconnectSSC32x', hDll), hApiParams)
    return function_call(pSSC32)

def SetAllPWMsFromThreadSSC32(pSSC32, selectedchannels, pws):
    global hDll

    nbchannels = 32
    pselectedchannels = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        pselectedchannels[k] = ctypes.c_int(int(selectedchannels[k]))
    ppws = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        ppws[k] = ctypes.c_int(pws[k])

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pSSC32", 0),(1, "pselectedchannels", 0),(1, "ppws", 0),
    function_call = hApiProto(('SetAllPWMsFromThreadSSC32x', hDll), hApiParams)
    return function_call(pSSC32, pselectedchannels, ppws)

def StartThreadSSC32(pSSC32):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pSSC32", 0),
    function_call = hApiProto(('StartThreadSSC32x', hDll), hApiParams)
    return function_call(pSSC32)

def StopThreadSSC32(pSSC32):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pSSC32", 0),
    function_call = hApiProto(('StopThreadSSC32x', hDll), hApiParams)
    return function_call(pSSC32)

def CreatePololu():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_void_p)
    hApiParams = None
    function_call = hApiProto(('CreatePololux', hDll), hApiParams)
    return function_call()

def DestroyPololu(pPololu):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
    hApiParams = (1, "pPololu", 0),
    function_call = hApiProto(('DestroyPololux', hDll), hApiParams)
    function_call(pPololu)

def GetValuePololu(pPololu, channel):
    global hDll

    pValue = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pPololu", 0),(1, "channel", 0),(1, "pValue", 0),
    function_call = hApiProto(('GetValuePololux', hDll), hApiParams)
    res = function_call(pPololu, channel, pValue)
    return res, pValue[0]

def GetAllValuesPololu(pPololu, selectedchannels, ais):
    global hDll

    nbchannels = 24
    pselectedchannels = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        pselectedchannels[k] = ctypes.c_int(int(selectedchannels[k]))
    pais = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        pais[k] = ctypes.c_int(ais[k])

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pPololu", 0),(1, "pselectedchannels", 0),(1, "pais", 0),
    function_call = hApiProto(('GetAllValuesPololux', hDll), hApiParams)
    return function_call(pPololu, pselectedchannels, pais)

def SetPWMPololu(pPololu, channel, pw):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)
    hApiParams = (1, "pPololu", 0),(1, "channel", 0),(1, "pw", 0),
    function_call = hApiProto(('SetPWMPololux', hDll), hApiParams)
    return function_call(pPololu, channel, pw)

def SetAllPWMsPololu(pPololu, selectedchannels, pws):
    global hDll

    nbchannels = 24
    pselectedchannels = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        pselectedchannels[k] = ctypes.c_int(int(selectedchannels[k]))
    ppws = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        ppws[k] = ctypes.c_int(pws[k])

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pPololu", 0),(1, "pselectedchannels", 0),(1, "ppws", 0),
    function_call = hApiProto(('SetAllPWMsPololux', hDll), hApiParams)
    return function_call(pPololu, pselectedchannels, ppws)

def SetPWMJrkPololu(pPololu, pw):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)
    hApiParams = (1, "pPololu", 0),(1, "pw", 0),
    function_call = hApiProto(('SetPWMJrkPololux', hDll), hApiParams)
    return function_call(pPololu, pw)

def ConnectPololu(pPololu, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)
    hApiParams = (1, "pPololu", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectPololux', hDll), hApiParams)
    return function_call(pPololu, cfgFilePath.encode('UTF-8'))

def DisconnectPololu(pPololu):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pPololu", 0),
    function_call = hApiProto(('DisconnectPololux', hDll), hApiParams)
    return function_call(pPololu)

def GetValueFromThreadPololu(pPololu, channel):
    global hDll

    pValue = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pPololu", 0),(1, "channel", 0),(1, "pValue", 0),
    function_call = hApiProto(('GetValueFromThreadPololux', hDll), hApiParams)
    res = function_call(pPololu, channel, pValue)
    return res, pValue[0]

def SetAllPWMsFromThreadPololu(pPololu, selectedchannels, pws):
    global hDll

    nbchannels = 24
    pselectedchannels = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        pselectedchannels[k] = ctypes.c_int(int(selectedchannels[k]))
    ppws = (ctypes.c_int*(nbchannels))() # Memory leak here, rely on garbage collector?
    for k in range(nbchannels):
        ppws[k] = ctypes.c_int(pws[k])

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pPololu", 0),(1, "pselectedchannels", 0),(1, "ppws", 0),
    function_call = hApiProto(('SetAllPWMsFromThreadPololux', hDll), hApiParams)
    return function_call(pPololu, pselectedchannels, ppws)

def StartThreadPololu(pPololu):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pPololu", 0),
    function_call = hApiProto(('StartThreadPololux', hDll), hApiParams)
    return function_call(pPololu)

def StopThreadPololu(pPololu):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pPololu", 0),
    function_call = hApiProto(('StopThreadPololux', hDll), hApiParams)
    return function_call(pPololu)

def CreateHokuyo():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_void_p)
    hApiParams = None
    function_call = hApiProto(('CreateHokuyox', hDll), hApiParams)
    return function_call()

def DestroyHokuyo(pHokuyo):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
    hApiParams = (1, "pHokuyo", 0),
    function_call = hApiProto(('DestroyHokuyox', hDll), hApiParams)
    function_call(pHokuyo)

def k2angleHokuyo(pHokuyo, k):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_void_p, ctypes.c_int)
    hApiParams = (1, "pHokuyo", 0),(1, "k", 0),
    function_call = hApiProto(('k2angleHokuyox', hDll), hApiParams)
    return function_call(pHokuyo, k)

def angle2kHokuyo(pHokuyo, angle):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_double)
    hApiParams = (1, "pHokuyo", 0),(1, "angle", 0),
    function_call = hApiProto(('angle2kHokuyox', hDll), hApiParams)
    return function_call(pHokuyo, angle)

def GetLatestDataHokuyo(pHokuyo):
    global hDll

    n = 2048
    pdistances = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pangles = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))
    hApiParams = (1, "pHokuyo", 0),(1, "pdistances", 0),(1, "pangles", 0),
    function_call = hApiProto(('GetLatestDataHokuyox', hDll), hApiParams)
    res = function_call(pHokuyo, pdistances, pangles)
    return res, pdistances, pangles

def ConnectHokuyo(pHokuyo, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)
    hApiParams = (1, "pHokuyo", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectHokuyox', hDll), hApiParams)
    return function_call(pHokuyo, cfgFilePath.encode('UTF-8'))

def DisconnectHokuyo(pHokuyo):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pHokuyo", 0),
    function_call = hApiProto(('DisconnectHokuyox', hDll), hApiParams)
    return function_call(pHokuyo)

def GetLatestDataFromThreadHokuyo(pHokuyo):
    global hDll

    n = 2048
    pdistances = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pangles = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))
    hApiParams = (1, "pHokuyo", 0),(1, "pdistances", 0),(1, "pangles", 0),
    function_call = hApiProto(('GetLatestDataFromThreadHokuyox', hDll), hApiParams)
    res = function_call(pHokuyo, pdistances, pangles)
    return res, pdistances, pangles

def StartThreadHokuyo(pHokuyo):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pHokuyo", 0),
    function_call = hApiProto(('StartThreadHokuyox', hDll), hApiParams)
    return function_call(pHokuyo)

def StopThreadHokuyo(pHokuyo):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pHokuyo", 0),
    function_call = hApiProto(('StopThreadHokuyox', hDll), hApiParams)
    return function_call(pHokuyo)

def CreateRPLIDAR():
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_void_p)
    hApiParams = None
    function_call = hApiProto(('CreateRPLIDARx', hDll), hApiParams)
    return function_call()

def DestroyRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('DestroyRPLIDARx', hDll), hApiParams)
    function_call(pRPLIDAR)

def StopRequestRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StopRequestRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def ResetRequestRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('ResetRequestRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def GetStartupMessageRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('GetStartupMessageRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def ClearCacheRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('ClearCacheRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def GetHealthRequestRPLIDAR(pRPLIDAR):
    global hDll

    pbProtectionStop = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pRPLIDAR", 0),(1, "pbProtectionStop", 0),
    function_call = hApiProto(('GetHealthRequestRPLIDARx', hDll), hApiParams)
    res = function_call(pRPLIDAR, pbProtectionStop)
    return res, pbProtectionStop[0]

def GetInfoRequestRPLIDAR(pRPLIDAR):
    global hDll

    pModelID = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?
    pHardwareVersion = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?
    pFirmwareMajor = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?
    pFirmwareMinor = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?
    #SerialNumber = (ctypes.c_byte*(33))() # Memory leak here, rely on garbage collector?
    #for k in range(33):
    #    SerialNumber[k] = ctypes.c_byte(int(0))
    SerialNumber = ctypes.create_string_buffer(33)

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_char_p)
    hApiParams = (1, "pRPLIDAR", 0),(1, "pModelID", 0),(1, "pHardwareVersion", 0),(1, "pFirmwareMajor", 0),(1, "pFirmwareMinor", 0),(1, "SerialNumber", 0),
    function_call = hApiProto(('GetInfoRequestRPLIDARx', hDll), hApiParams)
    res = function_call(pRPLIDAR, pModelID, pHardwareVersion, pFirmwareMajor, pFirmwareMinor, SerialNumber)
    return res, pModelID[0], pHardwareVersion[0], pFirmwareMajor[0], pFirmwareMinor[0], SerialNumber.value

def GetTypicalScanModeRPLIDAR(pRPLIDAR):
    global hDll

    pScanModeID = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pRPLIDAR", 0),(1, "pScanModeID", 0),
    function_call = hApiProto(('GetTypicalScanModeRPLIDARx', hDll), hApiParams)
    res = function_call(pRPLIDAR, pScanModeID)
    return res, pScanModeID[0]

def GetAllSupportedScanModesRPLIDAR(pRPLIDAR):
    global hDll

    pScanModeIDs = (ctypes.c_int*(16))() # Memory leak here, rely on garbage collector?
    pScanModeusPerSamples = (ctypes.c_double*(16))() # Memory leak here, rely on garbage collector?
    pScanModeMaxDistances = (ctypes.c_double*(16))() # Memory leak here, rely on garbage collector?
    pScanModeAnsTypes = (ctypes.c_int*(16))() # Memory leak here, rely on garbage collector?
    #pScanModeNames = ((ctypes.c_char * 64) * 16)() # Memory leak here, rely on garbage collector?
    string_buffers = [ctypes.create_string_buffer(64) for i in range(16)]
    pScanModeNames = (ctypes.c_char_p*16)(*map(ctypes.addressof, string_buffers))

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_char_p))
    hApiParams = (1, "pRPLIDAR", 0),(1, "pScanModeIDs", 0),(1, "pScanModeusPerSamples", 0),(1, "pScanModeMaxDistances", 0),(1, "pScanModeAnsTypes", 0),(1, "pScanModeNames", 0),
    function_call = hApiProto(('GetAllSupportedScanModesRPLIDARx', hDll), hApiParams)
    res = function_call(pRPLIDAR, pScanModeIDs, pScanModeusPerSamples, pScanModeMaxDistances, pScanModeAnsTypes, pScanModeNames)
    return res, pScanModeIDs, pScanModeusPerSamples, pScanModeMaxDistances, pScanModeAnsTypes, pScanModeNames

def SetMotorPWMRequestRPLIDAR(pRPLIDAR, pwm):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)
    hApiParams = (1, "pRPLIDAR", 0),(1, "pwm", 0),
    function_call = hApiProto(('SetMotorPWMRequestRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR, pwm)

def SetLidarSpinSpeedRequestRPLIDAR(pRPLIDAR, rpm):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)
    hApiParams = (1, "pRPLIDAR", 0),(1, "rpm", 0),
    function_call = hApiProto(('SetLidarSpinSpeedRequestRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR, rpm)

def StartMotorRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StartMotorRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def StopMotorRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StopMotorRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def StartScanRequestRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StartScanRequestRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def StartForceScanRequestRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StartForceScanRequestRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def GetScanDataResponseRPLIDAR(pRPLIDAR):
    global hDll

    pdistance = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?
    pangle = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?
    pbNewScan = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?
    pQuality = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pRPLIDAR", 0),(1, "pdistance", 0),(1, "pangle", 0),(1, "pbNewScan", 0),(1, "pQuality", 0),
    function_call = hApiProto(('GetScanDataResponseRPLIDARx', hDll), hApiParams)
    res = function_call(pRPLIDAR, pdistance, pangle, pbNewScan, pQuality)
    return res, pdistance[0], pangle[0], pbNewScan[0], pQuality[0]

def StartExpressScanRequestRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StartExpressScanRequestRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def GetExpressScanDataResponseRPLIDAR(pRPLIDAR):
    global hDll

    n = 32
    pdistances = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pangles = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pbNewScan = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pRPLIDAR", 0),(1, "pdistances", 0),(1, "pangles", 0),(1, "pbNewScan", 0),
    function_call = hApiProto(('GetExpressScanDataResponseRPLIDARx', hDll), hApiParams)
    res = function_call(pRPLIDAR, pdistances, pangles, pbNewScan)
    return res, pdistances, pangles, pbNewScan[0]

def StartOtherScanRequestRPLIDAR(pRPLIDAR, scanmodeid):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)
    hApiParams = (1, "pRPLIDAR", 0),(1, "scanmodeid", 0),
    function_call = hApiProto(('StartOtherScanRequestRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR, scanmodeid)

def GetOtherScanDataResponseRPLIDAR(pRPLIDAR):
    global hDll

    n = 32
    pdistances = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pangles = (ctypes.c_double*(n))() # Memory leak here, rely on garbage collector?
    pbNewScan = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pRPLIDAR", 0),(1, "pdistances", 0),(1, "pangles", 0),(1, "pbNewScan", 0),
    function_call = hApiProto(('GetOtherScanDataResponseRPLIDARx', hDll), hApiParams)
    res = function_call(pRPLIDAR, pdistances, pangles, pbNewScan)
    return res, pdistances, pangles, pbNewScan[0]

def ConnectRPLIDAR(pRPLIDAR, cfgFilePath):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)
    hApiParams = (1, "pRPLIDAR", 0),(1, "cfgFilePath", 0),
    function_call = hApiProto(('ConnectRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR, cfgFilePath.encode('UTF-8'))

def DisconnectRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('DisconnectRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def GetScanDataResponseFromThreadRPLIDAR(pRPLIDAR):
    global hDll

    pdistance = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?
    pangle = (ctypes.c_double*(1))() # Memory leak here, rely on garbage collector?
    pbNewScan = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?
    pQuality = (ctypes.c_int*(1))() # Memory leak here, rely on garbage collector?

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
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

    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int))
    hApiParams = (1, "pRPLIDAR", 0),(1, "pdistances", 0),(1, "pangles", 0),(1, "pbNewScan", 0),
    function_call = hApiProto(('GetExpressScanDataResponseFromThreadRPLIDARx', hDll), hApiParams)
    res = function_call(pRPLIDAR, pdistances, pangles, pbNewScan)
    return res, pdistances, pangles, pbNewScan[0]

def StartScanThreadRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StartScanThreadRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def StopScanThreadRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StopScanThreadRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def StartExpressScanThreadRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StartExpressScanThreadRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def StopExpressScanThreadRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StopExpressScanThreadRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def StartOtherScanThreadRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StartOtherScanThreadRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)

def StopOtherScanThreadRPLIDAR(pRPLIDAR):
    global hDll
    hApiProto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    hApiParams = (1, "pRPLIDAR", 0),
    function_call = hApiProto(('StopOtherScanThreadRPLIDARx', hDll), hApiParams)
    return function_call(pRPLIDAR)
