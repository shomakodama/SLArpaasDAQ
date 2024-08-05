


import SLArpaas_test15_RegisterFile
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
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Threshold0, handle)
    return err, data

def REG_Threshold0_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Threshold0, handle)
    return err

def REG_EnTrigger0_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger0, handle)
    return err, data

def REG_EnTrigger0_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger0, handle)
    return err

def REG_TimingReset_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_TimingReset, handle)
    return err, data

def REG_TimingReset_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_TimingReset, handle)
    return err

def REG_CounterEnable_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_CounterEnable, handle)
    return err, data

def REG_CounterEnable_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_CounterEnable, handle)
    return err

def REG_CounterReset_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_CounterReset, handle)
    return err, data

def REG_CounterReset_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_CounterReset, handle)
    return err

def REG_Counts_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Counts, handle)
    return err, data

def REG_Counts_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Counts, handle)
    return err

def REG_Polarity0_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Polarity0, handle)
    return err, data

def REG_Polarity0_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Polarity0, handle)
    return err

def REG_ManualTrigger_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_ManualTrigger, handle)
    return err, data

def REG_ManualTrigger_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_ManualTrigger, handle)
    return err

def REG_EnExternalTrigger_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_EnExternalTrigger, handle)
    return err, data

def REG_EnExternalTrigger_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_EnExternalTrigger, handle)
    return err

def REG_Threshold1_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Threshold1, handle)
    return err, data

def REG_Threshold1_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Threshold1, handle)
    return err

def REG_Polarity1_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Polarity1, handle)
    return err, data

def REG_Polarity1_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Polarity1, handle)
    return err

def REG_EnTrigger1_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger1, handle)
    return err, data

def REG_EnTrigger1_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger1, handle)
    return err

def REG_Threshold2_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Threshold2, handle)
    return err, data

def REG_Threshold2_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Threshold2, handle)
    return err

def REG_Polarity2_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Polarity2, handle)
    return err, data

def REG_Polarity2_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Polarity2, handle)
    return err

def REG_EnTrigger2_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger2, handle)
    return err, data

def REG_EnTrigger2_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger2, handle)
    return err

def REG_Threshold3_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Threshold3, handle)
    return err, data

def REG_Threshold3_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Threshold3, handle)
    return err

def REG_Polarity3_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Polarity3, handle)
    return err, data

def REG_Polarity3_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Polarity3, handle)
    return err

def REG_EnTrigger3_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger3, handle)
    return err, data

def REG_EnTrigger3_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger3, handle)
    return err

def REG_Threshold4_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Threshold4, handle)
    return err, data

def REG_Threshold4_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Threshold4, handle)
    return err

def REG_Polarity4_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Polarity4, handle)
    return err, data

def REG_Polarity4_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Polarity4, handle)
    return err

def REG_EnTrigger4_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger4, handle)
    return err, data

def REG_EnTrigger4_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger4, handle)
    return err

def REG_Threshold5_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Threshold5, handle)
    return err, data

def REG_Threshold5_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Threshold5, handle)
    return err

def REG_Polarity5_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Polarity5, handle)
    return err, data

def REG_Polarity5_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Polarity5, handle)
    return err

def REG_EnTrigger5_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger5, handle)
    return err, data

def REG_EnTrigger5_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger5, handle)
    return err

def REG_Threshold6_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Threshold6, handle)
    return err, data

def REG_Threshold6_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Threshold6, handle)
    return err

def REG_Polarity6_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Polarity6, handle)
    return err, data

def REG_Polarity6_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Polarity6, handle)
    return err

def REG_EnTrigger6_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger6, handle)
    return err, data

def REG_EnTrigger6_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger6, handle)
    return err

def REG_Threshold7_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Threshold7, handle)
    return err, data

def REG_Threshold7_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Threshold7, handle)
    return err

def REG_Polarity7_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Polarity7, handle)
    return err, data

def REG_Polarity7_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Polarity7, handle)
    return err

def REG_EnTrigger7_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger7, handle)
    return err, data

def REG_EnTrigger7_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger7, handle)
    return err

def REG_Threshold8_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Threshold8, handle)
    return err, data

def REG_Threshold8_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Threshold8, handle)
    return err

def REG_Polarity8_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Polarity8, handle)
    return err, data

def REG_Polarity8_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_Polarity8, handle)
    return err

def REG_EnTrigger8_GET(handle):
    [err, data] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger8, handle)
    return err, data

def REG_EnTrigger8_SET(data, handle):
    err = __abstracted_reg_write(data, SLArpaas_test15_RegisterFile.SCI_REG_EnTrigger8, handle)
    return err



def LISTMODULE_Digitizer_0_RESET(handle):
    err = __abstracted_reg_write(2, SLArpaas_test15_RegisterFile.SCI_REG_Digitizer_0_CONFIG, handle)
    return err

def LISTMODULE_Digitizer_0_START(handle, channels):
    err = __abstracted_reg_write(2 + (channels<<8), SLArpaas_test15_RegisterFile.SCI_REG_Digitizer_0_CONFIG, handle)
    if (err != 0):
       return False
    err = __abstracted_reg_write(0 + (channels<<8), SLArpaas_test15_RegisterFile.SCI_REG_Digitizer_0_CONFIG, handle)
    if (err != 0):
       return False
    err = __abstracted_reg_write(1 + (channels<<8), SLArpaas_test15_RegisterFile.SCI_REG_Digitizer_0_CONFIG, handle)
    if (err != 0):
       return False
    return True

def LISTMODULE_Digitizer_0_SetLen(handle, length):
    err = __abstracted_reg_write(length, SLArpaas_test15_RegisterFile.SCI_REG_Digitizer_0_ACQ_LEN, handle)
    if (err != 0):
       return False
    return True

def LISTMODULE_Digitizer_0_GET_STATUS(handle):
    [err, status] = __abstracted_reg_read(SLArpaas_test15_RegisterFile.SCI_REG_Digitizer_0_STATUS, handle)
    status = status & 0xf
    return err, status

def LISTMODULE_Digitizer_0_GET_DATA(Data_Number, timeout_ms, handle):
    [err, data, read_data, valid_data] = __abstracted_fifo_read(Data_Number, SLArpaas_test15_RegisterFile.SCI_REG_Digitizer_0_FIFOADDRESS, SLArpaas_test15_RegisterFile.SCI_REG_Digitizer_0_STATUS,1, timeout_ms, handle)
    return err, data, read_data, valid_data

