import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.console
import numpy as np
import serial
import time



from pyqtgraph.dockarea import *


#Serial takes two parameters: serial device and baudrate
ser = serial.Serial('/dev/ttyACM0', 115200) #ttyACM0 is the port name it might change based on the device

#ser = serial.Serial('COM11', 9600)
ser.flushInput() #flush input buffer



app = QtGui.QApplication([])
win = QtGui.QMainWindow()
area = DockArea()
win.setCentralWidget(area)
win.resize(1000,500)
win.setWindowTitle('DNV GL FuelFighters: read data')

d1 = Dock("Dock1", size=(1, 1)) 
d2 = Dock("Dock2 - Data Table", size=(500,300), closable=True)
d3 = Dock("Dock3", size=(500,400))


area.addDock(d1, 'left')      ## place d1 at left edge of dock area
area.addDock(d2,'right')
area.addDock(d3,'top',d2)

w1 = pg.LayoutWidget()
w2 = pg.LayoutWidget()
w3 = pg.PlotWidget(title="reading")



label = QtGui.QLabel(""" -- DNV GL FuelFighters -- 
						Why you should join FF???
						because of our princess Magnus
						""")
label2 = QtGui.QLabel("test")
hour = [1,2,3,4,5,6,7,8,9,10]
temperature = [30,32,34,32,33,31,29,32,35,45]

pic = QtGui.QLabel()
pic.setPixmap(QtGui.QPixmap("/home/motaz/Pictures/images.png"))

qbtn2 = QtGui.QPushButton('plot')
qbtn2.resize(qbtn2.sizeHint())
qbtn2.move(0, 0)

qbtn1 = QtGui.QPushButton('start')
qbtn1.resize(qbtn1.sizeHint())
qbtn1.move(0, 0)

qbtn0 = QtGui.QPushButton('Quit')
qbtn0.resize(qbtn0.sizeHint())
qbtn0.move(0, 0)

table = QtGui.QTableWidget()
table.setShowGrid(True)
table.setColumnCount(2)
table.setHorizontalHeaderLabels(['time', 'data'])
#table.resize(100,200)




x_var = list()
y_var = list()
np.array(x_var).astype(np.float)
np.array(y_var).astype(np.float)
t0 = time.time()


def quit():
	QtGui.QApplication.instance().quit()



def start():
	print("START!!")
	d2.addWidget(w1)
	#d2.addWidget(table)
	
def multitimes ():
	for i in range(0,20):
	#while(1):
		plot()


def plot():
	#while(1):
		t = 5;
		#plot_window = 50
		#y_var = np.array(np.zeros([plot_window]))
		#x_var = np.array(np.zeros([plot_window]))
		#x_var.astype(str)
		#x_var.astype(str)
		if ser.inWaiting():
			print("here")
			data_serial = ser.readline()
			rowPosition = table.rowCount()
			table.insertRow(rowPosition)
			table.setItem(rowPosition , 0, QtGui.QTableWidgetItem("text1"))
			table.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(float(data_serial))))
			table.scrollToBottom()	
		
			y_var.append(float(data_serial)) #= np.insert(y_var,49,data_serial)
			x_var.append(time.time()-t0) #= np.insert(x_var,49,time.time()-t0) 
			y_var
			w3.plot(x_var, y_var)
		
qbtn0.clicked.connect(quit)
qbtn1.clicked.connect(start)
qbtn2.clicked.connect(multitimes)

w1.addWidget(label, row=0, col=0)
#w1.addWidget(label2, row=0, col=1)
w1.addWidget(table, row=0, col=2)
w2.addWidget(qbtn1, row=0, col=0)
w2.addWidget(qbtn2, row=1, col=0)
w2.addWidget(pic, row=2, col=0)
w2.addWidget(qbtn0, row=3, col=0)


d1.addWidget(w2)
#d2.addWidget(w1)
d3.addWidget(w3)

win.show()

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
