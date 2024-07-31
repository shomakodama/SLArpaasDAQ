##################################################
##### SLArpaas_test11_Parameters.py
##### Written by Shoma 2024-07-25
##### Last modification 2024-07-25 (Shoma)
##################################################



# ip address
board = "127.0.0.10"

# timeout
Timeout_ms = 1000

# trigger
## manual trigger
### when OFF->ON, triggering once
manualtriggerOFF = 0
manualtriggerON = 10

## external trigger
externaltrigger = 0 # 0: disable, 1: enable

## self trigger
### ch0
threshold0 = 8150
polarity0 = 1 # 0: rising edge, 1: falling edge
enabletrigger0 = 1
### ch1
threshold1 = 8150
polarity1 = 1 # 0: rising edge, 1: falling edge
enabletrigger1 = 0
### ch2
threshold2 = 8150
polarity2 = 1 # 0: rising edge, 1: falling edge
enabletrigger2 = 0
### ch3
threshold3 = 8150
polarity3 = 1 # 0: rising edge, 1: falling edge
enabletrigger3 = 0
### ch4
threshold4 = 8150
polarity4 = 1 # 0: rising edge, 1: falling edge
enabletrigger4 = 0
### ch5
threshold5 = 8150
polarity5 = 1 # 0: rising edge, 1: falling edge
enabletrigger5 = 0

# counter
enablecounter = 1 # 0: disable, 1: enable

# digitizer
## enable channel
### 1: ch0
### 2: ch0, ch1
### 3: ch0, ch1, ch2
### 4: ch0, ch1, ch2, ch3
### 5: ch0, ch1, ch2, ch3, ch4
### 6: ch0, ch1, ch2, ch3, ch4, ch5
### 2-6: cannot be chosen for test11_v2
channelsenabled = 1
## sample length
samplelength = 1250
## DAQ size
size = (channelsenabled*samplelength + 16)