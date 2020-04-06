import sys
import SerialRead

from tkinter import * 				# used most often

from PIL import Image, ImageTk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


window = Tk()

# http://www.science.smith.edu/dftwiki/index.php/File:TkInterColorCharts.png
window.configure(background='gray25')			

window.title("Fuel Fighters cool interface")
window.geometry('1000x600')

# for serial reading
buffArray = []
baudrate = 9600
arrLen = 128
packCount = 0
#print(list_ports.comports())


#INITIALIZING SERIAL. 
# this is now imported from SerialRead.py to make it more readable
# change 'COM4' to 'dev..' whatever for linux
ser = SerialRead.SerialRead('COM4', baudrate, arrLen)
ser.readSerialToArray(ser, buffArray, arrLen, packCount)



window.mainloop()
