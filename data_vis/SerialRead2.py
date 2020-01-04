import serial
import numpy as np

ser = serial.Serial('COM11', 9600)


# start data collection
while True:

    d = str(ser.read(20))
    print(d)

    if d[2:4] == "Yo":
        print(d[2:-2])

    else:
        ser.close()
        print("This be the shit: ", d[2:4])
        ser = serial.Serial('COM11', 9600)

    #d = ""
    print('\n')

