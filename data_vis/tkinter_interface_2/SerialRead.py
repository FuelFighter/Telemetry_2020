import serial
from serial.tools import list_ports

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
		# need to dump first reading! why you may ask? ¯\_(ツ)_/¯ it just works ¯\_(ツ)_/¯
		dumpReading = self.ser.read()  
		
				
	def readSerialToArray(self, ser, arr, lenOfArr, packCount):
	    if len(arr) < lenOfArr:
	        arr.append(str(self.ser.read())[2])
	
	    if len(arr) == lenOfArr:
	        self.packCount += 1
	        print(arr, " - ", self.packCount, ' - ', len(arr))
	        self.ser.flush()
	        arr = []

