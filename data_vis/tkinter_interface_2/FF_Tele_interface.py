import sys

try:
	from Tkinter import * 				# used for puthon 2 ( i think )
except:
	from tkinter import *				# used for python 3

from PIL import Image, ImageTk		# requires pillow package
import serial
from serial.tools import list_ports

# https://matplotlib.org/2.1.2/gallery/user_interfaces/embedding_in_tk_sgskip.html
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from win32api import GetSystemMetrics

monitor_width = GetSystemMetrics(0) 						# requires pypiwin32 package
monitor_height = GetSystemMetrics(1)
window_scaling = 0.6										# needs to be between 0 and 1 



class SerialRead:
	ser = serial.Serial()
	portNames = list_ports.comports()
	portName = 'Undefined' 
	error = False				# set true if something is wrong

	baudratelist = [300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600, 115200]
	baudrate = 9600
	packCount = 0

	
	def __init__(self, port, baudrate, packLen):
		#initialize all variables
		self.portName = port
		self.baudrate = baudrate		
		self.packLen = packLen

		self.initSerialRead(self.portName, self.baudrate)

	#checks if portName is available on the PC
	def comportNotAvailable(self):
		ports = list_ports.comports()
		for i in range(len(ports)):
			if self.portName == ports[i].device:
				return False

		return True


	def initSerialRead(self, port, baudrate):
		#check if acceptable baud rate is set
		if(baudrate not in self.baudratelist):
			print("Baud rate not accepted")
		else:
			self.ser.baudrate = baudrate
		
		#check if USB port is found / accepted name
		if(self.portName == "Undefined"):
			print("Undefined port")
		elif(self.comportNotAvailable()):
			print("Port not availible/not located")
		else:
			self.ser.port = port
		
		
		self.ser.open()

		self.ser.flush()
		print(self.ser.is_open)
		# need to dump first reading! "why?" you may ask. ¯\_(ツ)_/¯ it just works ¯\_(ツ)_/¯
		dumpReading = self.ser.read()  
		
				
	def readSerialToArray(self, ser, arr, lenOfArr, packCount):
	    if len(arr) < lenOfArr:
	        arr.append(str(self.ser.read())[2])
	
	    if len(arr) == lenOfArr:
	        self.packCount += 1
	        print(arr, " - ", self.packCount, ' - ', len(arr))
	        self.ser.flush()
	        arr = []



class MenuBar:
	def __init__(self, master):
		self.menubar = Menu(master)
		self.filemenu = Menu(self.menubar, tearoff=0)
		self.filemenu.add_command(label="New", command=self.donothing)
		self.filemenu.add_command(label="Open", command=self.donothing)
		self.filemenu.add_command(label="Save", command=self.donothing)
		self.filemenu.add_command(label="Save as...", command=self.donothing)
		self.filemenu.add_command(label="Close", command=self.donothing)
		
		self.filemenu.add_separator()
		
		self.filemenu.add_command(label="Exit", command=master.quit)
		self.menubar.add_cascade(label="File", menu=self.filemenu)
		
		self.editmenu = Menu(self.menubar, tearoff=0)
		self.editmenu.add_command(label="Undo", command=self.donothing)
		
		self.editmenu.add_separator()
		
		self.editmenu.add_command(label="Cut", command=self.donothing)
		self.editmenu.add_command(label="Copy", command=self.donothing)
		self.editmenu.add_command(label="Paste", command=self.donothing)
		self.editmenu.add_command(label="Delete", command=self.donothing)
		self.editmenu.add_command(label="Select All", command=self.donothing)
		self.menubar.add_cascade(label="Edit", menu=self.editmenu)
		
		self.helpmenu = Menu(self.menubar, tearoff=0)
		self.helpmenu.add_command(label="Help Index", command=self.donothing)
		self.helpmenu.add_command(label="About...", command=self.donothing)
		self.menubar.add_cascade(label="Help", menu=self.helpmenu)
	


	def donothing():
		filewin = Toplevel(root)
		button = Button(filewin, text="Do nothing button")
		button.pack()


	






root = Tk()

menubar = MenuBar.MenuBar(root)


root.config(menu=menubar)






# for serial reading
# TODO : move this to SerialRead.py
buffArray = []
baudrate = 9600
arrLen = 128
packCount = 0

#INITIALIZING SERIAL. 
# this is now imported from SerialRead.py to make it more readable
# change 'COM4' to 'dev..' whatever for linux
#ser = SerialRead.SerialRead('COM4', baudrate, arrLen)
#ser.readSerialToArray(ser, buffArray, arrLen, packCount)



# http://www.science.smith.edu/dftwiki/index.php/File:TkInterColorCharts.png
root.configure(background='gray12')							# change this number to a lower one if you want darker background		

root.iconbitmap('Resources/logo.ico')						# sets the icon for the application
root.title("DNV GL Fuel Fighters Data Visualization")


#sets the opening size of the GUI to window_scaling * "your_monitor_resolution". need to slize string to remove ".0" after multiplication
root.geometry(str(window_scaling * monitor_width)[:-2] + 'x' + str(window_scaling * monitor_height)[:-2])
root.maxsize(monitor_width, monitor_height)					# now you cant have a bigger window than your monitor resolution

root.mainloop()

