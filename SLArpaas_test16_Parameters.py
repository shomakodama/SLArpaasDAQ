##################################################
##### SLArpaas_test16_Parameters.py
##### Written by Shoma 2024-07-25
##### Last modification 2024-08-15 (Shoma)
##################################################



# ip address
board = "127.0.0.10"

# timeout
Timeout_ms = 100000

# trigger
## manual trigger
### when OFF->ON, triggering once
manualtriggerOFF = 0
manualtriggerON = 10

## external trigger
externaltrigger = 0 # 0: disable, 1: enable

## periodic trigger
enableperiodictrigger = 0 # 0: disable, 1: enable
periodictriggerinterval = 125000 # in 8 ns

## self trigger
### ch0
threshold0 = 8150
polarity0 = 1 # 0: rising edge, 1: falling edge
enabletrigger0 = 1
### ch1
threshold1 = 8150
polarity1 = 1 # 0: rising edge, 1: falling edge
enabletrigger1 = 1
### ch2
threshold2 = 8150
polarity2 = 1 # 0: rising edge, 1: falling edge
enabletrigger2 = 1
### ch3
threshold3 = 8150
polarity3 = 1 # 0: rising edge, 1: falling edge
enabletrigger3 = 1
### ch4
threshold4 = 8150
polarity4 = 1 # 0: rising edge, 1: falling edge
enabletrigger4 = 1
### ch5
threshold5 = 8150
polarity5 = 1 # 0: rising edge, 1: falling edge
enabletrigger5 = 1
### ch6
threshold6 = 8150
polarity6 = 1 # 0: rising edge, 1: falling edge
enabletrigger6 = 1
### ch7
threshold7 = 8150
polarity7 = 1 # 0: rising edge, 1: falling edge
enabletrigger7 = 1
### ch8
threshold8 = 8150
polarity8 = 1 # 0: rising edge, 1: falling edge
enabletrigger8 = 1

### ch9
threshold9 = 0
polarity9 = 1 # 0: rising edge, 1: falling edge
enabletrigger9 = 0
### ch10
threshold10 = 0
polarity10 = 1 # 0: rising edge, 1: falling edge
enabletrigger10 = 0
### ch11
threshold11 = 0
polarity11 = 1 # 0: rising edge, 1: falling edge
enabletrigger11 = 0
### ch12
threshold12 = 0
polarity12 = 1 # 0: rising edge, 1: falling edge
enabletrigger12 = 0
### ch13
threshold13 = 0
polarity13 = 1 # 0: rising edge, 1: falling edge
enabletrigger13 = 0
### ch14
threshold14 = 0
polarity14 = 1 # 0: rising edge, 1: falling edge
enabletrigger14 = 0
### ch15
threshold15 = 0
polarity15 = 1 # 0: rising edge, 1: falling edge
enabletrigger15 = 0

# counter
enablecounter = 1 # 0: disable, 1: enable

# pre-scale factor
prescale = 1 # not used in test16_v2

# digitizer
## enable channel
### 1:  ch0
### 2:  ch0, ch1
### 4:  ch0, ch1, ch2, ch3
### 8:  ch0, ch1, ch2, ch3, ch4, ch5, ch6, ch7
### 16: ch0, ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10, ch11, ch12, ch13, ch14, ch15
channelsenabled = 1
## sample length
samplelength = 1248
## DAQ size
if(channelsenabled == 16):
    size = channelsenabled*samplelength + 16 + 16 # for channelsenabled == 16, I do not know why
else:
    size = channelsenabled*samplelength + 16