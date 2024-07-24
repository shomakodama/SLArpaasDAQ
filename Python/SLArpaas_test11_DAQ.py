import SLArpaas_test11_Functions as SLArpaasFunc
from ctypes import *
import time
import argparse

# ip address
board = "127.0.0.10"

# timeout
Timeout_ms = 1000

# trigger
## external trigger
externaltrigger = 0 # 0: disable, 1: enable

## self trigger
threshold0 = 8150
polarity0 = 1 # 0: rising edge, 1: falling edge
enabletrigger0 = 1

# counter
enablecounter = 1 # 0: disable, 1: enable

# digitizer
## enable channel
channelsenabled = 1
## sample length
samplelength = 1250
## ??
size = (channelsenabled*samplelength + 10)





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
    [err, handle] = SLArpaasFunc.ConnectDevice(board)
    if (err == 0):
        print("Successful connection to board ", board)
    else:
        print("Connection Error")



    # Set trigger settings
    ## manual trigger
    SLArpaasFunc.REG_ManualTrigger_SET(0, handle) # disabled

    ## external trigger
    SLArpaasFunc.REG_EnExternalTrigger_SET(externaltrigger, handle)
    if(externaltrigger == 1):
        print("External trigger: enabled")
    else:
        print("External trigger: disabled")

    ## self trigger (ch0)
    SLArpaasFunc.REG_Threshold0_SET(threshold0, handle)
    SLArpaasFunc.REG_Polarity0_SET(polarity0, handle)
    SLArpaasFunc.REG_EnTrigger0_SET(enabletrigger0, handle)
    if(enabletrigger0 == 1):
        print("Threshold (ch0) set to ", threshold0, " ADC")
    else:
        print("Self trigger for ch0: disabled")

    time.sleep(0.01)

    # Send reset
    SLArpaasFunc.REG_TimingReset_SET(1, handle)
    SLArpaasFunc.REG_CounterReset_SET(1, handle)

    time.sleep(0.01)

    # Send set
    SLArpaasFunc.REG_TimingReset_SET(0, handle)
    SLArpaasFunc.REG_CounterReset_SET(0, handle)



    # Set digitizer sample length
    SLArpaasFunc.LISTMODULE_Digitizer_0_SetLen(samplelength, handle)



    err, data = SLArpaasFunc.REG_Counts_GET(handle) # number of triggers
    print(">> N(triggers) at start", data)

    # DAQ
    daq(handle, output_file_name, max_evt)

    err, data = SLArpaasFunc.REG_Counts_GET(handle) # number of triggers
    print(">> N(triggers) at end", data)





def daq(handle, output_file_name, max_evt):

    output_file = open("data/%s"%(output_file_name),"a")

    read_evt = 0
    TargetDataNumber = size * max_evt/2

    try:
        if (SLArpaasFunc.LISTMODULE_Digitizer_0_RESET(handle) != 0):
            print("Reset Error!")
        if (SLArpaasFunc.LISTMODULE_Digitizer_0_START(channelsenabled, handle) == True):
            [err, List_Status] = SLArpaasFunc.LISTMODULE_Digitizer_0_GET_STATUS(handle)
            if List_Status > 0:
                while TargetDataNumber > 0:
                    [err, List_Data, List_Read_Data, List_Valid_Data] = SLArpaasFunc.LISTMODULE_Digitizer_0_GET_DATA(size, Timeout_ms, handle)
                    n_valid = int(List_Valid_Data.value)
                    for i in range(n_valid):
                        output_file.write('%x\n'%(List_Data[i]))
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


