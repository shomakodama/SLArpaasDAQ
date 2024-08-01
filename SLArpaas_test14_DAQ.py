##################################################
##### SLArpaas_test12_DAQ.py
##### Written by Shoma 2024-07-31
##### Last modification 2024-07-31 (Shoma)
##################################################



import SLArpaas_test14_Functions as SLArpaasFunc
import SLArpaas_test14_Parameters
from ctypes import *
import time
import argparse
import numpy as np



def options():

    parser = argparse.ArgumentParser(usage=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-o",
                        default="caen_test.dat",
                        help="Output file name")
    parser.add_argument("-n",
                        default=10,
                        help="Max events")
    return parser.parse_args()





def main():

    ops = options()

    output_file_name = ops.o
    max_evt = int(ops.n)



    SLArpaasFunc.Init()
    [err, handle] = SLArpaasFunc.ConnectDevice(SLArpaas_test14_Parameters.board)
    if (err == 0):
        print("Successful connection to board ", SLArpaas_test14_Parameters.board)
    else:
        print("Connection Error")



    # Set trigger settings
    ## manual trigger
    SLArpaasFunc.REG_ManualTrigger_SET(SLArpaas_test14_Parameters.manualtriggerOFF, handle)

    ## external trigger
    SLArpaasFunc.REG_EnExternalTrigger_SET(SLArpaas_test14_Parameters.externaltrigger, handle)
    if(SLArpaas_test14_Parameters.externaltrigger == 1):
        print("External trigger: enabled")
    else:
        print("External trigger: disabled")

    ## self trigger (ch0)
    SLArpaasFunc.REG_Threshold0_SET(SLArpaas_test14_Parameters.threshold0, handle)
    SLArpaasFunc.REG_Polarity0_SET(SLArpaas_test14_Parameters.polarity0, handle)
    SLArpaasFunc.REG_EnTrigger0_SET(SLArpaas_test14_Parameters.enabletrigger0, handle)
    if(SLArpaas_test14_Parameters.enabletrigger0 == 1):
        print("Threshold (ch0) set to ", SLArpaas_test14_Parameters.threshold0)
    else:
        print("Self trigger for ch0: disabled")

    ## self trigger (ch1)
    SLArpaasFunc.REG_Threshold1_SET(SLArpaas_test14_Parameters.threshold1, handle)
    SLArpaasFunc.REG_Polarity1_SET(SLArpaas_test14_Parameters.polarity1, handle)
    SLArpaasFunc.REG_EnTrigger1_SET(SLArpaas_test14_Parameters.enabletrigger1, handle)
    if(SLArpaas_test14_Parameters.enabletrigger1 == 1):
        print("Threshold (ch1) set to ", SLArpaas_test14_Parameters.threshold1)
    else:
        print("Self trigger for ch1: disabled")

    ## self trigger (ch2)
    SLArpaasFunc.REG_Threshold2_SET(SLArpaas_test14_Parameters.threshold2, handle)
    SLArpaasFunc.REG_Polarity2_SET(SLArpaas_test14_Parameters.polarity2, handle)
    SLArpaasFunc.REG_EnTrigger2_SET(SLArpaas_test14_Parameters.enabletrigger2, handle)
    if(SLArpaas_test14_Parameters.enabletrigger2 == 1):
        print("Threshold (ch2) set to ", SLArpaas_test14_Parameters.threshold2)
    else:
        print("Self trigger for ch2: disabled")

    ## self trigger (ch3)
    SLArpaasFunc.REG_Threshold3_SET(SLArpaas_test14_Parameters.threshold3, handle)
    SLArpaasFunc.REG_Polarity3_SET(SLArpaas_test14_Parameters.polarity3, handle)
    SLArpaasFunc.REG_EnTrigger3_SET(SLArpaas_test14_Parameters.enabletrigger3, handle)
    if(SLArpaas_test14_Parameters.enabletrigger3 == 1):
        print("Threshold (ch3) set to ", SLArpaas_test14_Parameters.threshold3)
    else:
        print("Self trigger for ch3: disabled")

    ## self trigger (ch4)
    SLArpaasFunc.REG_Threshold4_SET(SLArpaas_test14_Parameters.threshold4, handle)
    SLArpaasFunc.REG_Polarity4_SET(SLArpaas_test14_Parameters.polarity4, handle)
    SLArpaasFunc.REG_EnTrigger4_SET(SLArpaas_test14_Parameters.enabletrigger4, handle)
    if(SLArpaas_test14_Parameters.enabletrigger4 == 1):
        print("Threshold (ch4) set to ", SLArpaas_test14_Parameters.threshold4)
    else:
        print("Self trigger for ch4: disabled")

    ## self trigger (ch5)
    SLArpaasFunc.REG_Threshold5_SET(SLArpaas_test14_Parameters.threshold5, handle)
    SLArpaasFunc.REG_Polarity5_SET(SLArpaas_test14_Parameters.polarity5, handle)
    SLArpaasFunc.REG_EnTrigger5_SET(SLArpaas_test14_Parameters.enabletrigger5, handle)
    if(SLArpaas_test14_Parameters.enabletrigger5 == 1):
        print("Threshold (ch5) set to ", SLArpaas_test14_Parameters.threshold5)
    else:
        print("Self trigger for ch5: disabled")

    time.sleep(0.01)



    # Send reset
    SLArpaasFunc.REG_TimingReset_SET(1, handle)
    SLArpaasFunc.REG_CounterReset_SET(1, handle)

    time.sleep(0.01)

    SLArpaasFunc.REG_CounterEnable_SET(SLArpaas_test14_Parameters.enablecounter, handle)

    time.sleep(0.01)

    # Send set
    SLArpaasFunc.REG_TimingReset_SET(0, handle)
    SLArpaasFunc.REG_CounterReset_SET(0, handle)

    # pre-scale
    SLArpaasFunc.REG_PreScaleFactor_SET(SLArpaas_test14_Parameters.prescale, handle)



    # Set digitizer sample length
    SLArpaasFunc.LISTMODULE_Digitizer_0_SetLen(handle, SLArpaas_test14_Parameters.samplelength)



    err, data = SLArpaasFunc.REG_Counts_GET(handle) # number of triggers
    print(">> N(triggers) at start", data)

    # DAQ
    daq(handle, output_file_name, max_evt)

    err, data = SLArpaasFunc.REG_Counts_GET(handle) # number of triggers
    print(">> N(triggers) at end", data)





def daq(handle, output_file_name, max_evt):

    output_file = open("data/%s"%(output_file_name),"a")
    # output_file = open("data/%s"%(output_file_name),"wb")

    read_evt = 0
    #  TargetDataNumber = SLArpaas_test14_Parameters.size * max_evt/2

    try:
        if (SLArpaasFunc.LISTMODULE_Digitizer_0_RESET(handle) != 0):
            print("Reset Error!")
        if (SLArpaasFunc.LISTMODULE_Digitizer_0_START(handle, SLArpaas_test14_Parameters.channelsenabled) == True):
            [err, List_Status] = SLArpaasFunc.LISTMODULE_Digitizer_0_GET_STATUS(handle)
            if List_Status > 0:
                # while TargetDataNumber > 0:
                while read_evt < max_evt:
                    [err, List_Data, List_Read_Data, List_Valid_Data] = SLArpaasFunc.LISTMODULE_Digitizer_0_GET_DATA(SLArpaas_test14_Parameters.size, SLArpaas_test14_Parameters.Timeout_ms, handle)
                    n_valid = int(List_Valid_Data.value)
                    err, data = SLArpaasFunc.REG_Counts_GET(handle) # number of triggers
                    print(">> N(triggers) = ", data)
                    for i in range(n_valid):
                        output_file.write('%x\n'%(List_Data[i]))
                    # np_arr  = np.ctypeslib.as_array(List_Data)[:List_Valid_Data.value]
                    # output_file.write(np_arr.tobytes())
                    # TargetDataNumber -= n_valid
                    read_evt += 1
            else:
                print("Status Error")
        else:
            print("Start Error")
    except KeyboardInterrupt:
        print ("Stopped!")
        output_file.close()

    output_file.close()





if __name__=="__main__":
    main()


