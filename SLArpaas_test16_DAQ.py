##################################################
##### SLArpaas_test16_DAQ.py
##### Written by Shoma 2024-07-31
##### Last modification 2024-08-15 (Shoma)
##################################################



import SLArpaas_test16_Functions as SLArpaasFunc
import SLArpaas_test16_Parameters
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
    [err, handle] = SLArpaasFunc.ConnectDevice(SLArpaas_test16_Parameters.board)
    if (err == 0):
        print("Successful connection to board ", SLArpaas_test16_Parameters.board)
    else:
        print("Connection Error")



    # Set trigger settings
    ## manual trigger
    SLArpaasFunc.REG_ManualTrigger_SET(SLArpaas_test16_Parameters.manualtriggerOFF, handle)

    ## external trigger
    SLArpaasFunc.REG_EnExternalTrigger_SET(SLArpaas_test16_Parameters.externaltrigger, handle)
    if(SLArpaas_test16_Parameters.externaltrigger == 1):
        print("External trigger: enabled")
    else:
        print("External trigger: disabled")

    ## self trigger (ch0)
    SLArpaasFunc.REG_Threshold0_SET(SLArpaas_test16_Parameters.threshold0, handle)
    SLArpaasFunc.REG_Polarity0_SET(SLArpaas_test16_Parameters.polarity0, handle)
    SLArpaasFunc.REG_EnTrigger0_SET(SLArpaas_test16_Parameters.enabletrigger0, handle)
    if(SLArpaas_test16_Parameters.enabletrigger0 == 1):
        print("Threshold (ch0) set to ", SLArpaas_test16_Parameters.threshold0)
    else:
        print("Self trigger for ch0: disabled")

    ## self trigger (ch1)
    SLArpaasFunc.REG_Threshold1_SET(SLArpaas_test16_Parameters.threshold1, handle)
    SLArpaasFunc.REG_Polarity1_SET(SLArpaas_test16_Parameters.polarity1, handle)
    SLArpaasFunc.REG_EnTrigger1_SET(SLArpaas_test16_Parameters.enabletrigger1, handle)
    if(SLArpaas_test16_Parameters.enabletrigger1 == 1):
        print("Threshold (ch1) set to ", SLArpaas_test16_Parameters.threshold1)
    else:
        print("Self trigger for ch1: disabled")

    ## self trigger (ch2)
    SLArpaasFunc.REG_Threshold2_SET(SLArpaas_test16_Parameters.threshold2, handle)
    SLArpaasFunc.REG_Polarity2_SET(SLArpaas_test16_Parameters.polarity2, handle)
    SLArpaasFunc.REG_EnTrigger2_SET(SLArpaas_test16_Parameters.enabletrigger2, handle)
    if(SLArpaas_test16_Parameters.enabletrigger2 == 1):
        print("Threshold (ch2) set to ", SLArpaas_test16_Parameters.threshold2)
    else:
        print("Self trigger for ch2: disabled")

    ## self trigger (ch3)
    SLArpaasFunc.REG_Threshold3_SET(SLArpaas_test16_Parameters.threshold3, handle)
    SLArpaasFunc.REG_Polarity3_SET(SLArpaas_test16_Parameters.polarity3, handle)
    SLArpaasFunc.REG_EnTrigger3_SET(SLArpaas_test16_Parameters.enabletrigger3, handle)
    if(SLArpaas_test16_Parameters.enabletrigger3 == 1):
        print("Threshold (ch3) set to ", SLArpaas_test16_Parameters.threshold3)
    else:
        print("Self trigger for ch3: disabled")

    ## self trigger (ch4)
    SLArpaasFunc.REG_Threshold4_SET(SLArpaas_test16_Parameters.threshold4, handle)
    SLArpaasFunc.REG_Polarity4_SET(SLArpaas_test16_Parameters.polarity4, handle)
    SLArpaasFunc.REG_EnTrigger4_SET(SLArpaas_test16_Parameters.enabletrigger4, handle)
    if(SLArpaas_test16_Parameters.enabletrigger4 == 1):
        print("Threshold (ch4) set to ", SLArpaas_test16_Parameters.threshold4)
    else:
        print("Self trigger for ch4: disabled")

    ## self trigger (ch5)
    SLArpaasFunc.REG_Threshold5_SET(SLArpaas_test16_Parameters.threshold5, handle)
    SLArpaasFunc.REG_Polarity5_SET(SLArpaas_test16_Parameters.polarity5, handle)
    SLArpaasFunc.REG_EnTrigger5_SET(SLArpaas_test16_Parameters.enabletrigger5, handle)
    if(SLArpaas_test16_Parameters.enabletrigger5 == 1):
        print("Threshold (ch5) set to ", SLArpaas_test16_Parameters.threshold5)
    else:
        print("Self trigger for ch5: disabled")

    time.sleep(0.01)

    ## self trigger (ch6)
    SLArpaasFunc.REG_Threshold6_SET(SLArpaas_test16_Parameters.threshold6, handle)
    SLArpaasFunc.REG_Polarity6_SET(SLArpaas_test16_Parameters.polarity6, handle)
    SLArpaasFunc.REG_EnTrigger6_SET(SLArpaas_test16_Parameters.enabletrigger6, handle)
    if(SLArpaas_test16_Parameters.enabletrigger6 == 1):
        print("Threshold (ch6) set to ", SLArpaas_test16_Parameters.threshold6)
    else:
        print("Self trigger for ch6: disabled")

    time.sleep(0.01)

    ## self trigger (ch7)
    SLArpaasFunc.REG_Threshold7_SET(SLArpaas_test16_Parameters.threshold7, handle)
    SLArpaasFunc.REG_Polarity7_SET(SLArpaas_test16_Parameters.polarity7, handle)
    SLArpaasFunc.REG_EnTrigger7_SET(SLArpaas_test16_Parameters.enabletrigger7, handle)
    if(SLArpaas_test16_Parameters.enabletrigger7 == 1):
        print("Threshold (ch7) set to ", SLArpaas_test16_Parameters.threshold7)
    else:
        print("Self trigger for ch7: disabled")

    time.sleep(0.01)

    ## self trigger (ch8)
    SLArpaasFunc.REG_Threshold8_SET(SLArpaas_test16_Parameters.threshold8, handle)
    SLArpaasFunc.REG_Polarity8_SET(SLArpaas_test16_Parameters.polarity8, handle)
    SLArpaasFunc.REG_EnTrigger8_SET(SLArpaas_test16_Parameters.enabletrigger8, handle)
    if(SLArpaas_test16_Parameters.enabletrigger8 == 1):
        print("Threshold (ch8) set to ", SLArpaas_test16_Parameters.threshold8)
    else:
        print("Self trigger for ch8: disabled")

    time.sleep(0.01)

    ## self trigger (ch9)
    SLArpaasFunc.REG_Threshold9_SET(SLArpaas_test16_Parameters.threshold9, handle)
    SLArpaasFunc.REG_Polarity9_SET(SLArpaas_test16_Parameters.polarity9, handle)
    SLArpaasFunc.REG_EnTrigger9_SET(SLArpaas_test16_Parameters.enabletrigger9, handle)
    if(SLArpaas_test16_Parameters.enabletrigger9 == 1):
        print("Threshold (ch9) set to ", SLArpaas_test16_Parameters.threshold9)
    else:
        print("Self trigger for ch9: disabled")

    time.sleep(0.01)

    ## self trigger (ch10)
    SLArpaasFunc.REG_Threshold10_SET(SLArpaas_test16_Parameters.threshold10, handle)
    SLArpaasFunc.REG_Polarity10_SET(SLArpaas_test16_Parameters.polarity10, handle)
    SLArpaasFunc.REG_EnTrigger10_SET(SLArpaas_test16_Parameters.enabletrigger10, handle)
    if(SLArpaas_test16_Parameters.enabletrigger10 == 1):
        print("Threshold (ch10) set to ", SLArpaas_test16_Parameters.threshold10)
    else:
        print("Self trigger for ch10: disabled")

    time.sleep(0.01)

    ## self trigger (ch11)
    SLArpaasFunc.REG_Threshold11_SET(SLArpaas_test16_Parameters.threshold11, handle)
    SLArpaasFunc.REG_Polarity11_SET(SLArpaas_test16_Parameters.polarity11, handle)
    SLArpaasFunc.REG_EnTrigger11_SET(SLArpaas_test16_Parameters.enabletrigger11, handle)
    if(SLArpaas_test16_Parameters.enabletrigger11 == 1):
        print("Threshold (ch11) set to ", SLArpaas_test16_Parameters.threshold11)
    else:
        print("Self trigger for ch11: disabled")

    time.sleep(0.01)

    ## self trigger (ch12)
    SLArpaasFunc.REG_Threshold12_SET(SLArpaas_test16_Parameters.threshold12, handle)
    SLArpaasFunc.REG_Polarity12_SET(SLArpaas_test16_Parameters.polarity12, handle)
    SLArpaasFunc.REG_EnTrigger12_SET(SLArpaas_test16_Parameters.enabletrigger12, handle)
    if(SLArpaas_test16_Parameters.enabletrigger12 == 1):
        print("Threshold (ch12) set to ", SLArpaas_test16_Parameters.threshold12)
    else:
        print("Self trigger for ch12: disabled")

    time.sleep(0.01)

    ## self trigger (ch13)
    SLArpaasFunc.REG_Threshold13_SET(SLArpaas_test16_Parameters.threshold13, handle)
    SLArpaasFunc.REG_Polarity13_SET(SLArpaas_test16_Parameters.polarity13, handle)
    SLArpaasFunc.REG_EnTrigger13_SET(SLArpaas_test16_Parameters.enabletrigger13, handle)
    if(SLArpaas_test16_Parameters.enabletrigger13 == 1):
        print("Threshold (ch13) set to ", SLArpaas_test16_Parameters.threshold13)
    else:
        print("Self trigger for ch13: disabled")

    time.sleep(0.01)

    ## self trigger (ch14)
    SLArpaasFunc.REG_Threshold14_SET(SLArpaas_test16_Parameters.threshold14, handle)
    SLArpaasFunc.REG_Polarity14_SET(SLArpaas_test16_Parameters.polarity14, handle)
    SLArpaasFunc.REG_EnTrigger14_SET(SLArpaas_test16_Parameters.enabletrigger14, handle)
    if(SLArpaas_test16_Parameters.enabletrigger14 == 1):
        print("Threshold (ch14) set to ", SLArpaas_test16_Parameters.threshold14)
    else:
        print("Self trigger for ch14: disabled")

    time.sleep(0.01)

    ## self trigger (ch15)
    SLArpaasFunc.REG_Threshold15_SET(SLArpaas_test16_Parameters.threshold15, handle)
    SLArpaasFunc.REG_Polarity15_SET(SLArpaas_test16_Parameters.polarity15, handle)
    SLArpaasFunc.REG_EnTrigger15_SET(SLArpaas_test16_Parameters.enabletrigger15, handle)
    if(SLArpaas_test16_Parameters.enabletrigger15 == 1):
        print("Threshold (ch15) set to ", SLArpaas_test16_Parameters.threshold15)
    else:
        print("Self trigger for ch15: disabled")

    time.sleep(0.01)



    # Send reset
    SLArpaasFunc.REG_TimingReset_SET(1, handle)
    SLArpaasFunc.REG_CounterReset_SET(1, handle)

    time.sleep(0.01)

    SLArpaasFunc.REG_CounterEnable_SET(SLArpaas_test16_Parameters.enablecounter, handle)

    time.sleep(0.01)

    # Send set
    SLArpaasFunc.REG_TimingReset_SET(0, handle)
    SLArpaasFunc.REG_CounterReset_SET(0, handle)

    # pre-scale
    # SLArpaasFunc.REG_PreScaleFactor_SET(SLArpaas_test14_Parameters.prescale, handle)



    # Set digitizer sample length
    SLArpaasFunc.LISTMODULE_Digitizer_0_SetLen(handle, SLArpaas_test16_Parameters.samplelength)



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
        if (SLArpaasFunc.LISTMODULE_Digitizer_0_START(handle, SLArpaas_test16_Parameters.channelsenabled) == True):
            # while TargetDataNumber > 0:
            while read_evt < max_evt:
                start_time = time.time()
                [err, List_Data, List_Read_Data, List_Valid_Data] = SLArpaasFunc.LISTMODULE_Digitizer_0_GET_DATA(SLArpaas_test16_Parameters.size/2, SLArpaas_test16_Parameters.Timeout_ms, handle)
                n_valid = int(List_Valid_Data.value)
                err, data = SLArpaasFunc.REG_Counts_GET(handle) # number of triggers
                print(">> N(triggers) = ", data, "n_valid = ", n_valid, "elapse = ", time.time()-start_time, "s")
                for i in range(n_valid):
                    output_file.write('%x\n'%(List_Data[i]))
                output_file.write('\n')
                # np_arr  = np.ctypeslib.as_array(List_Data)[:List_Valid_Data.value]
                # output_file.write(np_arr.tobytes())
                # TargetDataNumber -= n_valid
                read_evt += 1
        else:
            print("Start Error")
    except KeyboardInterrupt:
        print ("Stopped!")
        output_file.close()

    output_file.close()





if __name__=="__main__":
    main()


