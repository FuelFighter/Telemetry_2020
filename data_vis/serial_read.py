import serial
import numpy as np
from matplotlib import pyplot as plt

# ser = serial.Serial('/dev/ttyACM0', 9600) # linux/ubuntu alternative
ser = serial.Serial('COM11', 9600)
ser.flush()
buffArray = []
packLen = 128
packCount = 0
# start data collection

#def countFirstofArray():
dumpReading = ser.read()  # need to dump first reading!


def readSerialToArray(ser, arr, lenOfArr, packCount):

    if len(arr) < lenOfArr:
        arr.append(str(ser.read())[2])

    if len(arr) == lenOfArr:
        packCount += 1
        print(arr, " - ", packCount, ' - ', len(arr))
        ser.flush()
        arr = []


while True:
    readSerialToArray(ser, buffArray, packLen, packCount)
