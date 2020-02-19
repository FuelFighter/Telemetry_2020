import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.console
import numpy as np
import serial
import time


from pyqtgraph.dockarea import *


#Serial takes two parameters: serial device and baudrate
ser = serial.Serial('/dev/ttyACM0', 9600) #ttyACM0 is the port name it might change based on the device
# ser = serial.Serial('COMXX', 9600) #WINDOWS ALTERNATIVE
ser.flushInput() #flush input buffer



app = QtGui.QApplication([])
win = QtGui.QMainWindow()
area = DockArea()
win.setCentralWidget(area)
win.resize(1000,500)
win.setWindowTitle('DNV GL FuelFighters: read data')

d1 = Dock("Dock1", size=(1, 1)) 
d2 = Dock("Dock2 - Console", size=(500,300), closable=True)
d3 = Dock("Dock3", size=(500,400))


area.addDock(d1, 'left')      ## place d1 at left edge of dock area
area.addDock(d2,'right')
area.addDock(d3,'top',d2)

w1 = pg.LayoutWidget()
w2 = pg.LayoutWidget()
w3 = pg.PlotWidget(title="Plot inside dock with no title bar")




label = QtGui.QLabel(""" -- DNV GL FuelFighters -- 
Why you should join FF???
because of our princess Magnus
""")
hour = [1,2,3,4,5,6,7,8,9,10]
temperature = [30,32,34,32,33,31,29,32,35,45]

pic = QtGui.QLabel()
pic.setPixmap(QtGui.QPixmap("/home/motaz/Pictures/images.png"))

qbtn1 = QtGui.QPushButton('start')
qbtn1.resize(qbtn1.sizeHint())
qbtn1.move(0, 0)

qbtn0 = QtGui.QPushButton('Quit')
qbtn0.resize(qbtn0.sizeHint())
qbtn0.move(0, 0)


def quit():
	QtGui.QApplication.instance().quit()

def plotValues():
    plt.title('Serial value from Arduino')
    plt.grid(True)
    plt.ylabel('Values')
    plt.plot(values, 'rx-', label='values')
    plt.legend(loc='upper right')

def start():
	print("START!!")
	d2.addWidget(w1)
	plot_window = 50
	y_var = np.array(np.zeros([plot_window]))
	x_var = np.array(np.zeros([plot_window]))
	x_var.astype(str)
	x_var.astype(str)
	itt = 1
	t0 = time.time()
	# read data from serial port
	if ser.inWaiting()>0 :

		data_serial = ser.readline()	

		y_var = np.insert(y_var,0,data_serial)
		x_var = np.insert(x_var,0,time.time()-t0) 


		w3.plot(x_var, y_var)

qbtn0.clicked.connect(quit)
qbtn1.clicked.connect(start)

w1.addWidget(label, row=0, col=0)
w2.addWidget(qbtn1, row=0, col=0)
w2.addWidget(pic, row=1, col=0)
w2.addWidget(qbtn0, row=2, col=0)

d1.addWidget(w2)
#d2.addWidget(w1)
d3.addWidget(w3)

win.show()

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
