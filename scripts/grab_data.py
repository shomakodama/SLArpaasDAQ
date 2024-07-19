import sys, os
sys.path.append('/path/to/this/directory')

import common.SLArpaas_test9_Functions as SLArpaasfunc
from ctypes import *
import time
import argparse

# each packet grabbed is 32 bits
board       = "172.0.0.10"
line_length = 32 # we like 32 bits
header_len  = 16 # 16 lines x 32 bits
sample_len  = 16 # 16 lines x 32 bits
nsamples    = 100
buff_size   = (nsamples*sample_len+header_len) * npacket # this assumes no truncated packets!
timeout_ms  = 1000
# nevt        = 10
# npacket     = nevt * 16 # 16 packets per event
threshold   = 8150





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

    max_packet     = max_evt * 16


    # Connect to board
    SLArpaasfunc.Init()
    [err, handle] = SLArpaasfunc.ConnectDevice(board)
    if (err == 0):
        print("Successful connection to board ", board)
    else:
        print("Connection Error")


    # Set trigger settings
    SLArpaasfunc.REG_NCH_SET(1, handle)
    SLArpaasfunc.REG_THRESH_0_SET(threshold, handle) # what is the difference
    SLArpaasfunc.REG_THRESH_1_SET(threshold, handle) # between 0 and 1?
    print("Threshold set to ", threshold, " counts")

    time.sleep(0.01)

    # Send reset
    SLArpaasfunc.REG_RESET_SET(1, handle) # what is the difference
    SLArpaasfunc.REG_RESET_SET(0, handle) # between 0 and 1?

    # Get inhibit time:
    err, data = SLArpaasfunc.REG_TRIG_COUNTS_GET(handle) # number of triggers
    print(">> N(triggers) at start", data)
    err, data_time = SLArpaasfunc.REG_INHIBIT_TIME_GET(handle) # when is 0?
    err, data_time_coarse = SLArpaasfunc.REG_INHIBIT_TIME_COARSE_GET(handle) # when is 0?
    data_time_s = int(data_time)*8*pow(10,-9)
    data_time_coarse_s = int(data_time_coarse)*pow(2,32)*8*pow(10,-9)
    data_time_total_s = data_time_coarse_s + data_time_s
    print(">> Inhibit time at start: %.2f s"%(data_time_total_s))

    # DAQ main part starts here
    # start receiving
    tcp_rec(handle, output_file_name, max_packet)
    # DAQ main part finishes here

    err, data = SLArpaasfunc.REG_TRIG_COUNTS_GET(handle) # number of triggers
    print(">> N(triggers) at end", data)
    err, data_time = SLArpaasfunc.REG_INHIBIT_TIME_GET(handle)
    err, data_time_coarse = SLArpaasfunc.REG_INHIBIT_TIME_COARSE_GET(handle)
    data_time_s = int(data_time)*8*pow(10,-9)
    data_time_coarse_s = int(data_time_coarse)*pow(2,32)*8*pow(10,-9)
    data_time_total_s = data_time_coarse_s + data_time_s
    print(">> Inhibit time at end: %.2f s"%(data_time_total_s))





def tcp_rec(handle, output_file_name, max_evt):

    output_file = open("data/%s.dat"%(output_file_name),"a")

    read_evt = 0

    try:
        if (SLArpaasfunc.CPACK_CP_0_RESET(handle) != 0):
            print("Reset Error!")
        if (SLArpaasfunc.CPACK_CP_0_START(handle) == True):
            [err, frame_status] = SLArpaasfunc.CPACK_CP_0_GET_STATUS(handle)
            if frame_status > 0:
                while read_evt < max_evt:
                    [err, Frame_Data, Frame_Read_Data, Frame_Valid_Data] = SLArpaasfunc.CPACK_CP_0_GET_DATA(buff_size, timeout_ms, handle)
                    n_valid = int(Frame_Valid_Data.value)
                    for i in range(n_valid):
                        output_file.write('%x\n'%(Frame_Data[i]))
                    read_evt += npacket
                    #time.sleep(sleep_time)
                    if read_evt % 1000 == 0:
                        # calculate inhibit time
                        err, data = SLArpaasfunc.REG_TRIG_COUNTS_GET(handle)
                        err, data_time = SLArpaasfunc.REG_INHIBIT_TIME_GET(handle)
                        err, data_time_coarse = SLArpaasfunc.REG_INHIBIT_TIME_COARSE_GET(handle)
                        data_time_s = int(data_time)*8*pow(10,-9)
                        data_time_coarse_s = int(data_time_coarse)*pow(2,32)*8*pow(10,-9)
                        data_time_total_s = data_time_coarse_s + data_time_s
                        print("Inhibit time at %d triggers: %.2f s"%(int(data), data_time_total_s))

            else:
                print("Status Error")
        else:
            print("Start Error")
    except KeyboardInterrupt:
        print "Stopped!"
        err, data = SLArpaasfunc.REG_TRIG_COUNTS_GET(handle)
        print(">> N(triggers) at end", data)
        err, data_time = SLArpaasfunc.REG_INHIBIT_TIME_GET(handle)
        err, data_time_coarse = SLArpaasfunc.REG_INHIBIT_TIME_COARSE_GET(handle)
        data_time_s = int(data_time)*8*pow(10,-9)
        data_time_coarse_s = int(data_time_coarse)*pow(2,32)*8*pow(10,-9)
        data_time_total_s = data_time_coarse_s + data_time_s
        print(">> Inhibit time at end: %.2f s"%(data_time_total_s))
        output_file.close()

    output_file.close()





if __name__=="__main__":
    main()








# comment 2024-07-01 by Shoma
# Using SciSDK Library, it is easy to set some parameters(?)
# https://nuclearinstruments.github.io/SCISDK/index.html
    

