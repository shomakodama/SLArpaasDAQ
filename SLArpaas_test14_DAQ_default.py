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
                        default="caen_test.hex",
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
    # SLArpaasFunc.REG_ManualTrigger_SET(SLArpaas_test12_Parameters.manualtriggerOFF, handle)

    ## external trigger
    # SLArpaasFunc.REG_EnExternalTrigger_SET(SLArpaas_test12_Parameters.externaltrigger, handle)
    # if(SLArpaas_test12_Parameters.externaltrigger == 1):
    #     print("External trigger: enabled")
    # else:
    #     print("External trigger: disabled")

    ## self trigger (ch0)
    SLArpaasFunc.REG_Threshold0_SET(SLArpaas_test14_Parameters.threshold0, handle)
    SLArpaasFunc.REG_Polarity0_SET(SLArpaas_test14_Parameters.polarity0, handle)
    SLArpaasFunc.REG_EnTrigger0_SET(SLArpaas_test14_Parameters.enabletrigger0, handle)
    if(SLArpaas_test14_Parameters.enabletrigger0 == 1):
        print("Threshold (ch0) set to ", SLArpaas_test14_Parameters.threshold0)
    else:
        print("Self trigger for ch0: disabled")

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



    # Set digitizer sample length
    SLArpaasFunc.LISTMODULE_Digitizer_0_SetLen(handle, SLArpaas_test14_Parameters.samplelength)



    err, data = SLArpaasFunc.REG_Counts_GET(handle) # number of triggers
    print(">> N(triggers) at start", data)

    # DAQ
    daq(handle, output_file_name, max_evt)

    err, data = SLArpaasFunc.REG_Counts_GET(handle) # number of triggers
    print(">> N(triggers) at end", data)





def daq(handle, output_file_name, max_evt):

    output_file = open("data/%s"%(output_file_name),"wb")

    read_evt = 0
    TargetDataNumber = SLArpaas_test14_Parameters.size * max_evt/2

    try:
        if (SLArpaasFunc.LISTMODULE_Digitizer_0_RESET(handle) != 0):
            print("Reset Error!")
        if (SLArpaasFunc.LISTMODULE_Digitizer_0_START(handle, SLArpaas_test14_Parameters.channelsenabled) == True):
            [err, List_Status] = SLArpaasFunc.LISTMODULE_Digitizer_0_GET_STATUS(handle)
            if List_Status > 0:
                while TargetDataNumber > 0:
                    [err, List_Data, List_Read_Data, List_Valid_Data] = SLArpaasFunc.LISTMODULE_Digitizer_0_GET_DATA(SLArpaas_test14_Parameters.size, SLArpaas_test14_Parameters.Timeout_ms, handle)
                    n_valid = int(List_Valid_Data.value)
                    np_arr  = np.ctypeslib.as_array(List_Data)[:List_Valid_Data.value]
                    output_file.write(np_arr.tobytes())
                    TargetDataNumber -= n_valid
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


