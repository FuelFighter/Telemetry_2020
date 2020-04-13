import sys

from win32api import GetSystemMetrics

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import (QAction, QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit,
							   QMainWindow, QPushButton, QTableWidget, QTableWidgetItem,
							   QVBoxLayout, QWidget)
#from PyQt5.QtCharts import QtCharts

import pyqtgraph as pg


monitor_width = GetSystemMetrics(0)                         # requires pypiwin32 package
monitor_height = GetSystemMetrics(1)
window_scaling = 0.6                                        # needs to be between 0 and 1


class SerialRead:
	#self.port_names = list_ports.comports()
	# checks if portName is available on the PC
	def comport_not_available(self):
		ports = list_ports.comports()
		for i in range(len(ports)):
			if self.port_name == ports[i].device:
				return False
		return True


	def __init__(self, port="Undefined", baudrate=9600, pack_len=0):
		# check if acceptable baud rate is set
		self.ser = serial.Serial()
		self.port_name = port
		self.baudrate_list = [300, 600, 1200, 2400, 4800,
							  9600, 14400, 19200, 28800, 38400, 57600, 115200]
		if(baudrate in self.baudrate_list):
			self.ser.baudrate = baudrate
		else:
			print("Baud rate not accepted")
			error = True

		# check if USB port is found / accepted name
		if(self.comport_not_available() and port == 'Undefined'):
			print("Port not availible/not located, or undefined")
			self.error = True
		else:
			self.ser.port = port

		self.error = False				# set true if something is wrong
		self.com_open = False			# set true if reading COM ports
		self.pack_count = 0
		self.pack_len = pack_len


	def init_serial_read(self):
		if not self.error:
			try:
				self.ser.open()
				self.ser.flush()
				self.com_open = True

				print("Serial reading initialized.")
				# need to dump first reading! "why?" you may ask. ¯\_(ツ)_/¯ it just works ¯\_(ツ)_/¯
				dumpReading = self.ser.read()
			# this error occurs if one serial parametere is wrong
			except(serial.serialutil.SerialException):
				print("Serial port error. Have you chosen a valid COM-port?")


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


class Widget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		#set background color
		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), Qt.darkGray)
		self.setPalette(p)

		# data table for raw data
		self.table = QTableWidget()
		self.table.setColumnCount(3)
		self.table.setHorizontalHeaderLabels(['Data', 'Value', 'Unit'])
		self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

		# plotting data
		self.plot_widget = pg.PlotWidget(name="Plot 1")



		# this was intended for some fancy steering graphics. Does not scale as it should after resizing the window
		#self.draw_label = QLabel()
		#self.draw_label.setScaledContents(True)
		#self.draw_label.sizeHint()
		#self.steering_canvas = QtGui.QPixmap(100, 500)
		#self.scaled = self.steering_canvas.scaled(100,100, Qt.KeepAspectRatio, Qt.FastTransformation)
		#self.label_w = self.draw_label.width()
		#self.label_h = self.draw_label.height()
		#print(self.label_w, self.label_h)

		#self.draw_label.setPixmap(self.steering_canvas.scaled(350, 350, Qt.KeepAspectRatio, Qt.SmoothTransformation)) 
		#self.draw_label.setPixmap(self.scaled)
		#self.draw_label.setPixmap(QtGui.QPixmap('logo.png'))
		#self.draw_something()

		# can translation. 
		self.can_table = QTableWidget()
		self.can_table.setColumnCount(4)
		self.can_table.setHorizontalHeaderLabels(['CAN ID', 'Len', 'Data', 'Translated data'])
		self.can_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

		
		self.grid_layout = QtWidgets.QGridLayout()
		self.grid_layout.setHorizontalSpacing(20)
		self.grid_layout.setVerticalSpacing(20)
		
		self.grid_layout.setColumnStretch(0, 3)
		self.grid_layout.setColumnStretch(1, 7)
		
		self.grid_layout.setRowStretch(0, 3)		# only functional in full screen
		self.grid_layout.setRowStretch(1, 2)

		self.grid_layout.addWidget(self.table, 0, 0, 1, 1)  # row, column, rowspan, colspan
		self.grid_layout.addWidget(self.plot_widget, 0, 1, 1, 1)
		#self.grid_layout.addWidget(self.draw_label, 1, 1, 1, 1)
		self.grid_layout.addWidget(self.can_table, 1, 0, 1, 2)
		self.setLayout(self.grid_layout)
		'''
		self.hbox_layout_top = QHBoxLayout()
		self.hbox_layout_top.addWidget(self.table)
		self.hbox_layout_top.addWidget(self.plot_widget)
		#self.hbox_layout_top.addItem(self.steering_canvas)

		self.hbox_layout_bot = QHBoxLayout()
		self.hbox_layout_bot.addWidget(self.draw_label)
		self.hbox_layout_bot.addWidget(self.can_table)

		self.vbox_layout = QVBoxLayout()
		self.vbox_layout.addLayout(self.hbox_layout_top)
		self.vbox_layout.addLayout(self.hbox_layout_bot)
		
		self.setLayout(self.vbox_layout)
		'''

	def draw_something(self):
		painter = QtGui.QPainter(self.draw_label.pixmap())
		painter.drawLine(10, 10, 300, 200)
		painter.end()




class MainWindow(QMainWindow):
	def __init__(self, widget):
		QMainWindow.__init__(self)
		self.setWindowTitle("DNV GL Fuel Fighter Data Vis")

		self.menu = self.menuBar()
		self.file_menu = self.menu.addMenu("File")

		self.setCentralWidget(widget)




if __name__ == "__main__":
	# Qt Application
	app = QApplication(sys.argv)
	#Qwidget
	widget = Widget()
	#QMainwindow using Qwidget as central widget
	window = MainWindow(widget)
	
	win_width = int(window_scaling * monitor_width)
	win_height = int(window_scaling * monitor_height)

	window.resize(win_width, win_height)
	window.show()
	# set icon of window
	app.setWindowIcon(QtGui.QIcon('logo.png'))	


	sys.exit(app.exec_())
