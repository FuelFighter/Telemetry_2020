from PyQt4 import QtGui  # (the example applies equally well to PySide)
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
import pandas as pd
import csv
import numpy as np




##read data from file
##method #1
#f=open("data.csv", "r")
#if f.mode == 'r':
#	contents = f.read()
#	print(contents[1:5])
#
##method 2
Data=pd.read_csv('data.csv',usecols=['value'])
unit=pd.read_csv('data.csv',usecols=['unit'])
Conv_data = Data.rename_axis('value').values
T_data=Conv_data.transpose()
T_data=T_data[0,0:5]

print(T_data)
print(Conv_data)
print(Data)
print(unit)

## Always start by initializing Qt (only once per application)
app = QtGui.QApplication([])

## Define a top-level widget to hold everything
#w = QtGui.QWidget()
win = pg.GraphicsWindow(title="Read data")

## Create some widgets to be placed inside
btn = QtGui.QPushButton('star')
text = QtGui.QLineEdit('enter text')
listw = QtGui.QListWidget()
Plot = pg.PlotWidget()

##data part
#here it's a pre-defined values for testing
hour = [1,2,3,4,5]#,6,7,8,9,10]
temperature = [30,32,34,32,33,31,29,32,35,45]


## Create a grid layout to manage the widgets size and position
layout = QtGui.QGridLayout()
win.setLayout(layout)

## Add widgets to the layout in their proper positions
layout.addWidget(btn, 0, 0)   # button goes in upper-left
layout.addWidget(text, 1,0)   # text edit goes in middle-left
layout.addWidget(listw, 2, 0)  # list widget goes in bottom-left
layout.addWidget(Plot, 0, 1, 3, 1)  # plot goes on right side, spanning 3 rows

## plot the data on the PlotWidget
Plot.plot(hour, T_data)

## Display the widget as a new window
win.show()
#btn.show()

## Start the Qt event loop
app.exec_()

