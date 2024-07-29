import SLArpaas_test9_Functions as SLArpaasfunc
from ctypes import *
import time
import argparse

board       = "127.0.0.10"
#sleep_time  = 0.000002 #1

# external trigger
enext0 = 0 # 0:disable, 1:enable
# self trigger
enself0 = 1 # 0:disable, 1:enable
threshold0   = 8150
polarity0 = 1 # 0:rising edge, 1:falling edge

N_Packet = 100
Timeout_ms = 10000
# N_Total_Events = 10000





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

    max_evt = -1
    if ops.n:
        max_evt = int(ops.n)

    N_Total_Events = max_evt * 100


    # Connect to board
    SLArpaasfunc.Init()
    [err, handle] = SLArpaasfunc.ConnectDevice(board)
    if (err == 0):
        print("Successful connection to board ", board)
    else:
        print("Connection Error")


    # Set trigger settings
    SLArpaasfunc.REG_ManualTrigger_SET(0, handle) # not set
    SLArpaasfunc.REG_EnExternalTrigger_SET(enext0, handle)

    SLArpaasfunc.REG_Threshold0_SET(threshold0, handle)
    SLArpaasfunc.REG_Polarity0_SET(polarity0, handle)
    SLArpaasfunc.REG_EnTrigger0_SET(enself0, handle)

    print("Threshold set to ", threshold0)

    time.sleep(0.01)

    # Counter
    SLArpaasfunc.REG_CounterEnable_SET(1, handle) # Counter enable

    # Reset
    SLArpaasfunc.REG_FIFOReset_SET(1, handle) # Reset FIFO
    SLArpaasfunc.REG_TimingReset_SET(1, handle) # Reset Timing
    SLArpaasfunc.REG_CounterEnable_SET(1, handle) # Reset Counter

    # Restart
    SLArpaasfunc.REG_FIFOReset_SET(0, handle) # Restart FIFO
    SLArpaasfunc.REG_TimingReset_SET(0, handle) # Restart Timing
    SLArpaasfunc.REG_CounterEnable_SET(0, handle) # Restart Counter

    # DAQ main part
    tcp_rec(handle, output_file_name, N_Total_Events)






def tcp_rec(handle, output_file_name, N_Total_Events):

    output_file = open("data/%s.dat"%(output_file_name),"a")

    ReadDataNumber = 0

    try:
        if (SLArpaasfunc.CPACK_CP_0_RESET(handle) != 0):
            print("Reset Error!")
        if (SLArpaasfunc.CPACK_CP_0_START(handle) == True):
            [err, frame_status] = SLArpaasfunc.CPACK_CP_0_GET_STATUS(handle)
            if frame_status > 0:
                while ReadDataNumber < N_Total_Events:
                    [err, Frame_Data, Frame_Read_Data, Frame_Valid_Data] = SLArpaasfunc.CPACK_CP_0_GET_DATA(N_Packet, Timeout_ms, handle)
                    n_valid = int(Frame_Valid_Data.value)
                    for i in range(n_valid):
                        output_file.write('%x'%(Frame_Data[i]))
                    ReadDataNumber += N_Packet
                    #time.sleep(sleep_time)

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







    

