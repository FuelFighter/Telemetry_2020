import sys

try:
	import Tkinter as tk				# used for puthon 2 ( i think )
except:
	import tkinter as tk				# used for python 3

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
	#self.port_names = list_ports.comports()
	

	#checks if portName is available on the PC
	def comport_not_available(self):
		ports = list_ports.comports()
		for i in range(len(ports)):
			if self.port_name == ports[i].device: 
				return False
		return True
	
	
	def __init__(self, port="Undefined", baudrate=9600, pack_len=0):
		#check if acceptable baud rate is set
		self.ser = serial.Serial()
		self.port_name = port
		self.baudrate_list = [300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600, 115200]
		if(baudrate in self.baudrate_list):
			self.ser.baudrate = baudrate
		else:
			print("Baud rate not accepted")
			error = True

		#check if USB port is found / accepted name
		if(self.comport_not_available() and port =='Undefined'):
			print("Port not availible/not located, or undefined")
			self.error = True
		else:
			self.ser.port = port

		#self.error = False				# set true if something is wrong
		self.com_open = False			# set true if reading COM ports
		self.pack_count = 0
		self.pack_len = pack_len


	def init_serial_read(self):
		self.com_open = True
		if not self.error:
			self.ser.open()
			self.ser.flush()
			print(self.ser.is_open)
			# need to dump first reading! "why?" you may ask. ¯\_(ツ)_/¯ it just works ¯\_(ツ)_/¯
			dumpReading = self.ser.read()  
		
	def end_serial_read(self):
		self.ser.close()
		self.com_open = False
				
	def read_serial_to_array(self, ser, arr, len_of_arr, pack_count):
	    if len(arr) < len_of_arr:
	        arr.append(str(self.ser.read())[2])
	
	    if len(arr) == len_of_arr:
	        self.pack_count += 1
	        print(arr, " - ", self.pack_count, ' - ', len(arr))
	        self.ser.flush()
	        arr = []


class MenuBar:
	def __init__(self, master):
		self.master = master
		self.menubar = tk.Menu(self.master)
		self.filemenu = tk.Menu(self.menubar, tearoff=0)
		self.filemenu.add_command(label="New", command=self.donothing)
		self.filemenu.add_command(label="Open", command=self.donothing)
		self.filemenu.add_command(label="Save", command=self.donothing)
		self.filemenu.add_command(label="Save as...", command=self.donothing)
		self.filemenu.add_command(label="Close", command=self.donothing)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Exit", command=self.master.quit)
		self.menubar.add_cascade(label="File", menu=self.filemenu)		
		
		self.serialmenu = tk.Menu(self.menubar, tearoff=0)
		self.serialmenu.add_command(label='Start serial communication', command=self.start_serial_com)
		self.serialmenu.add_command(label='End serial com.', command=self.end_serial_com)
		self.menubar.add_cascade(label="Serial com.", menu=self.serialmenu)
		self.master.config(menu=self.menubar) 			# needed to actually show the menubar

	def donothing(self):								
		filewin = tk.Toplevel(self.master)

	def start_serial_com(self):
		com_win = tk.Toplevel(self.master, bg='gray12')
		ser.init_serial_read()

	def end_serial_com(self):
		ser.end_serial_read()
		print(1)


class Table:
	def __init__(self, master):
		self.frame = tk.Frame(master)


class MainApp():
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(master)
		self.frame.configure(background='gray12')
		self.frame.pack(expand=True, fill='both')

		self.menubar = MenuBar(self.master)

# for serial reading

#buffArray = []
baudrate = 9600
arrLen = 128
packCount = 0

#INITIALIZING SERIAL. 
# this is now imported from SerialRead.py to make it more readable
# change 'COM4' to 'dev..' whatever for linux
ser = SerialRead('COM4', baudrate, arrLen) # this needs to be global ( i know this is bad practice, but i didnt know of any other way to do this)



if __name__ == '__main__':
	root = tk.Tk()
	

	# http://www.science.smith.edu/dftwiki/index.php/File:TkInterColorCharts.png
	#root.configure(background='gray12')							# change this number to a lower one if you want darker background		
	
	root.iconbitmap('Resources/logo.ico')						# sets the icon for the application
	root.title("DNV GL Fuel Fighters Data Visualization")
	
	
	#sets the opening size of the GUI to window_scaling * "your_monitor_resolution". need to slize string to remove ".0" after multiplication
	root.geometry(str(window_scaling * monitor_width)[:-2] + 'x' + str(window_scaling * monitor_height)[:-2]) # this is now decided with mainApp frame size
	root.maxsize(monitor_width, monitor_height)					# now you cant have a bigger window than your monitor resolution
	main_app = MainApp(root)
	root.mainloop()

