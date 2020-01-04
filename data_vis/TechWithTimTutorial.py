# link to tutorial https://www.youtube.com/watch?v=Vde5SH8e1OQ
# buttons: https://www.youtube.com/watch?v=-2uyzAqefyE&list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj&index=3&t=0s

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):                # heritage from QMainWindow
    def __init__(self):
        super(MyWindow, self).__init__()    # constructor

        self.setGeometry(150, 150, 800, 600)  # xpos, ypos, width, height of window. (0,0) is top left corner of screen
        self.setWindowTitle("Telemetry 2020")

        self.initUI()                       # initialize the UI function


    def initUI(self):

        # adding label
        self.label = QtWidgets.QLabel(self)      # self is the parent window
        self.label.setText("What ever you want it to be")
        self.label.move(50, 50)                  # position your label

        # adding button
        self.b1 = QtWidgets.QPushButton(self)    # self is the parent window
        self.b1.setText("Click me")              # set the text on the button
        self.b1.move(200, 200)                   # positioning of the button
        self.b1.clicked.connect(self.click)      # connect the button to an event

    def click(self):
        self.label.setText("You clicked me but the text is really long so it doesn't fit inside"
                           "the original box")
        self.update()

    def update(self):
        self.label.adjustSize()                 # updates the size of the label


def window():
    app = QApplication(sys.argv)  # gives the system info regarding OS, screen etc
    win = MyWindow()  # make a window

    win.show()  # to show the window
    sys.exit(app.exec_())  # just for closing the window without any issues

window()

'''
def click():
    print("clicked")


def window():
    app = QApplication(sys.argv)            # gives the system info regarding OS, screen etc
    win = QMainWindow()                     # make a window
    win.setGeometry(150, 150, 800, 600)     # xpos, ypos, width, height of window. (0,0) is top left corner of screen
    win.setWindowTitle("Telemetry 2020")

    # adding label
    label = QtWidgets.QLabel(win)           # win is the parent
    label.setText("What ever you want it to be")
    label.move(50, 50)                      # position your label

    # adding button
    b1 = QtWidgets.QPushButton(win)         # win is the parent
    b1.setText("Push me")                   # set the text on the button
    b1.move(200, 200)                       # positioning of the button
    b1.clicked.connect(click)               # connect the button to an event



    win.show()                              # to show the window
    sys.exit(app.exec_())                   # just for closing the window without any issues

window()
'''




