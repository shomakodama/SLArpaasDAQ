




import SLArpaas_test12_RegisterFile
from ctypes import *
import array
import numpy as np

import os
mydll = cdll.LoadLibrary(os.path.dirname(__file__) +'/R5560_SDKLib.dll')

def Init():
    return 0

def ConnectDevice(board):
    c_s = c_char_p(board.encode('ascii'))
    da= mydll.R5560_HandleAllocator()
    handle = c_void_p(da)
    err = mydll.R5560_ConnectTCP(c_s, 8888, handle)
    return err, handle

def CloseConnect(handle):
    err = mydll.NI_CloseConnection((handle))
    return err    
    
def ListDevices():
    str_devices=""
    dev_count =-1
    return str_devices, dev_count 

def __abstracted_reg_write(data, address, handle):
    err = mydll.NI_WriteReg(data, address, (handle))
    return err

def __abstracted_reg_read(address, handle):
    data = c_uint(0)
    err = mydll.NI_ReadReg(byref(data), address, (handle))
    return err, data.value

def __abstracted_mem_write(data, count, address, timeout_ms, handle):
    written_data = c_uint(0)
    err = mydll.NI_WriteData(data, count, address, (handle), byref(written_data))
    return err, written_data.value

def __abstracted_mem_read(count, address, timeout_ms, handle):
    data = (c_uint * (2* count))()
    read_data = c_uint(0)
    valid_data = c_uint(0)
    err = mydll.NI_ReadData(byref(data), count, address, (handle), byref(read_data))
    valid_data=read_data
    return err, data, read_data.value, valid_data.value

def __abstracted_fifo_write(data, count, address, address_status, timeout_ms, handle):
    return -1

def __abstracted_fifo_read(count, address, address_status, blocking, timeout_ms, handle):
    data = (c_uint * (2 * count))()
    read_data = c_uint(0)
    valid_data = c_uint(0)
    err = mydll.NI_ReadFifo(byref(data), count, address, address_status, (1 if blocking else 2), timeout_ms, (handle), byref(read_data))
    valid_data=read_data
    return err, data, read_data, valid_data     
    
def __abstracted_DMA_read(dma_channel, handle):
    count = 2*1024*1024;
    data = (c_ulonglong * (count))()
    read_data = c_uint(0)
    err = mydll.NI_DMA_Read(dma_channel, byref(data), count, byref(read_data), (handle))
    vd = (read_data.value / 8);
    return err, data, vd     
    
def __abstracted_DMA_CONFIG(dma_channel, blocking, timeout, buffer_length, handle):
    err = mydll.NI_DMA_SetOptions(dma_channel, blocking, timeout, buffer_length, (handle))
    return err
    
    
def gray_to_bin(num, nbit):
    temp = num ^ (num >> 8)
    temp ^= (temp >> 4)
    temp ^= (temp >> 2)
    temp ^= (temp >> 1)
    return temp    

def REG_Threshold0_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test12_RegisterFile.SCI_REG_Threshold0, handle)
    return err, data

def REG_Threshold0_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test12_RegisterFile.SCI_REG_Threshold0, handle)
    return err

def REG_EnTrigger0_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test12_RegisterFile.SCI_REG_EnTrigger0, handle)
    return err, data

def REG_EnTrigger0_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test12_RegisterFile.SCI_REG_EnTrigger0, handle)
    return err

def REG_TimingReset_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test12_RegisterFile.SCI_REG_TimingReset, handle)
    return err, data

def REG_TimingReset_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test12_RegisterFile.SCI_REG_TimingReset, handle)
    return err

def REG_CounterEnable_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test12_RegisterFile.SCI_REG_CounterEnable, handle)
    return err, data

def REG_CounterEnable_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test12_RegisterFile.SCI_REG_CounterEnable, handle)
    return err

def REG_CounterReset_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test12_RegisterFile.SCI_REG_CounterReset, handle)
    return err, data

def REG_CounterReset_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test12_RegisterFile.SCI_REG_CounterReset, handle)
    return err

def REG_Counts_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test12_RegisterFile.SCI_REG_Counts, handle)
    return err, data

def REG_Counts_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test12_RegisterFile.SCI_REG_Counts, handle)
    return err

def REG_Polarity0_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test12_RegisterFile.SCI_REG_Polarity0, handle)
    return err, data

def REG_Polarity0_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test12_RegisterFile.SCI_REG_Polarity0, handle)
    return err



def LISTMODULE_Digitizer_0_RESET(handle):
    err = __abstracted_reg_write(2, SLArpaas_test12_RegisterFile.SCI_REG_Digitizer_0_CONFIG, handle)
    return err

def LISTMODULE_Digitizer_0_START(handle, channels):
    err = __abstracted_reg_write(2 + (channels<<8), SLArpaas_test12_RegisterFile.SCI_REG_Digitizer_0_CONFIG, handle)
    if (err != 0):
       return False
    err = __abstracted_reg_write(0 + (channels<<8), SLArpaas_test12_RegisterFile.SCI_REG_Digitizer_0_CONFIG, handle)
    if (err != 0):
       return False
    err = __abstracted_reg_write(1 + (channels<<8), SLArpaas_test12_RegisterFile.SCI_REG_Digitizer_0_CONFIG, handle)
    if (err != 0):
       return False
    return True

def LISTMODULE_Digitizer_0_SetLen(handle, length):
    err = __abstracted_reg_write(length, SLArpaas_test12_RegisterFile.SCI_REG_Digitizer_0_ACQ_LEN, handle)
    if (err != 0):
       return False
    return True

def LISTMODULE_Digitizer_0_GET_STATUS(handle):
    [err, status] = __abstracted_reg_read(SLArpaas_test12_RegisterFile.SCI_REG_Digitizer_0_STATUS, handle)
    status = status & 0xf
    return err, status

def LISTMODULE_Digitizer_0_GET_DATA(Data_Number, timeout_ms, handle):
    [err, data, read_data, valid_data] = __abstracted_fifo_read(Data_Number, SLArpaas_test12_RegisterFile.SCI_REG_Digitizer_0_FIFOADDRESS, SLArpaas_test12_RegisterFile.SCI_REG_Digitizer_0_STATUS,1, timeout_ms, handle)
    return err, data, read_data, valid_data



def OSCILLOSCOPE_Oscilloscope_0_START(handle):
    err = __abstracted_reg_write(0, SLArpaas_test12_RegisterFile.SCI_REG_Oscilloscope_0_CONFIG_ARM, handle)
    if (err != 0):
       return False
    err = __abstracted_reg_write(1, SLArpaas_test12_RegisterFile.SCI_REG_Oscilloscope_0_CONFIG_ARM, handle)
    if (err != 0):
       return False
    return True

def OSCILLOSCOPE_Oscilloscope_0_SET_DECIMATOR(OscilloscopeDecimator, handle):
    err = __abstracted_reg_write(OscilloscopeDecimator, SLArpaas_test12_RegisterFile.SCI_REG_Oscilloscope_0_CONFIG_DECIMATOR, handle)
    return err

def OSCILLOSCOPE_Oscilloscope_0_SET_PRETRIGGER(OscilloscopePreTrigger, handle):
    err = __abstracted_reg_write(OscilloscopePreTrigger, SLArpaas_test12_RegisterFile.SCI_REG_Oscilloscope_0_CONFIG_PRETRIGGER, handle)
    return err

def OSCILLOSCOPE_Oscilloscope_0_SET_TRIGGER_LEVEL(OscilloscopeTriggerLevel, handle):
    err = __abstracted_reg_write(OscilloscopeTriggerLevel, SLArpaas_test12_RegisterFile.SCI_REG_Oscilloscope_0_CONFIG_TRIGGER_LEVEL, handle)
    return err

def OSCILLOSCOPE_Oscilloscope_0_SET_TRIGGER_MODE(OscilloscopeTriggerMode, OscilloscopeTriggerChannel, OscilloscopeTriggerEdge, handle):
    AnalogTrigger = 0
    Digital0Trigger = 0
    Digital1Trigger = 0
    Digital2Trigger = 0
    Digital3Trigger = 0
    SoftwareTrigger = 0
    if (OscilloscopeTriggerMode == "Analog"):
        AnalogTrigger = 1
    if (OscilloscopeTriggerMode == "Digital0"):
        Digital0Trigger = 1
    if (OscilloscopeTriggerMode == "Digital1"):
        Digital1Trigger = 1
    if (OscilloscopeTriggerMode == "Digital2"):
        Digital2Trigger = 1
    if (OscilloscopeTriggerMode == "Digital3"):
        Digital3Trigger = 1
    if (OscilloscopeTriggerMode == "Free"):
        SoftwareTrigger = 1
    if (OscilloscopeTriggerEdge == "Rising"):
        Edge = 0
    else:
        Edge = 1
    triggermode = c_int(0)
    triggermode = (OscilloscopeTriggerChannel << 8)  + (SoftwareTrigger << 7 ) + (Edge << 3) + (SoftwareTrigger << 1) + AnalogTrigger +(Digital0Trigger << 2) + (Digital1Trigger << 2) + Digital1Trigger + (Digital2Trigger << 2) + (Digital2Trigger << 1) + (Digital3Trigger << 2) + (Digital3Trigger << 1) + Digital3Trigger
    err = __abstracted_reg_write(triggermode, SLArpaas_test12_RegisterFile.SCI_REG_Oscilloscope_0_CONFIG_TRIGGER_MODE, handle)
    return err

def OSCILLOSCOPE_Oscilloscope_0_GET_STATUS(handle):
    [err, status] = __abstracted_reg_read(SLArpaas_test12_RegisterFile.SCI_REG_Oscilloscope_0_READ_STATUS, handle)
    return err, status

def OSCILLOSCOPE_Oscilloscope_0_GET_POSITION(handle):
    [err, position] = __abstracted_reg_read(SLArpaas_test12_RegisterFile.SCI_REG_Oscilloscope_0_READ_POSITION, handle)
    return err, position

def OSCILLOSCOPE_Oscilloscope_0_GET_DATA(timeout_ms, handle):
    [err, data, read_data, valid_data] = __abstracted_mem_read(2048, SLArpaas_test12_RegisterFile.SCI_REG_Oscilloscope_0_FIFOADDRESS, timeout_ms, handle)
    return err, data, read_data, valid_data

def OSCILLOSCOPE_Oscilloscope_0_RECONSTRUCT_DATA(OscilloscopeData, OscilloscopePosition, OscilloscopePreTrigger):
    OscilloscopeChannels = 1
    OscilloscopeSamples = 2048
    Analog = list(range(OscilloscopeSamples*OscilloscopeChannels))
    Digital0 = list(range(OscilloscopeSamples*OscilloscopeChannels))
    Digital1 = list(range(OscilloscopeSamples*OscilloscopeChannels))
    Digital2 = list(range(OscilloscopeSamples*OscilloscopeChannels))
    Digital3 = list(range(OscilloscopeSamples*OscilloscopeChannels))
    for n in range(OscilloscopeChannels):
        current = OscilloscopePosition - OscilloscopePreTrigger
        if ((current) > 0):
            k = 0
            for i in range(current, OscilloscopeSamples-1):
                Analog[k+ OscilloscopeSamples * n] = OscilloscopeData[i+ OscilloscopeSamples * n] & 65535
                k = k + 1
            for i in range(0, current-1):
                Analog[k+ OscilloscopeSamples * n] = OscilloscopeData[i+ OscilloscopeSamples * n] & 65535
                k = k + 1
        else:
            k = 0
            for i in range(OscilloscopeSamples+current, OscilloscopeSamples-1):
                Analog[k+ OscilloscopeSamples * n] = OscilloscopeData[i+ OscilloscopeSamples * n] & 65535
                k = k + 1
            for i in range(0, OscilloscopeSamples+current-1):
                Analog[k+ OscilloscopeSamples * n] = OscilloscopeData[i+ OscilloscopeSamples * n] & 65535
                k = k + 1
    return Analog, Digital0, Digital1,Digital2, Digital3

