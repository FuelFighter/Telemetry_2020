import serial
import numpy as np
from matplotlib import pyplot as plt
# ser = serial.Serial('/dev/ttyACM0', 9600)
ser = serial.Serial('COM4', 9600)
ser.flush()
buffArray = []
print(len('###111111111111111111111111111111111111111111111111111111111112X'))
# start data collection
while True:
    # if str(ser.read())[2:3] == 'X':
    #     print('Tis be the sameth')
    if str(ser.read())[2:3] != 'X' and str(ser.read())[2:4] != "\\" and len(buffArray) < 65:
        buffArray.append(str(ser.read())[2:3])
        ser.flush()
        if len(buffArray) == 64:
            print(buffArray[3:])
            buffArray = []

    # d = str(ser.read())
    # print(d)
    # ser.flush()
    # d = ""
