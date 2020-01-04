from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(150, 150, 451, 221))
        self.button.setObjectName("Button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button.clicked.connect(self.show_popup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button.setText(_translate("MainWindow", "Show Popup"))

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Tutorial on PyQt5")
        msg.setText("This is the main text")
        msg.setIcon(QMessageBox.Critical)               # Critical, warning, Information, Question or nothing

        # different options for buttons that we can click when popup shows
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ignore | QMessageBox.Ok)

        # set default button
        msg.setDefaultButton(QMessageBox.Ignore)

        # add informative text
        msg.setInformativeText("informative text")

        #add detail text, will be hidden until you click button
        msg.setDetailedText("Hidden detailed text")

        msg.buttonClicked.connect(self.popup_button)

        x = msg.exec_()             # this is what shows the popup

    def popup_button(self, i):      # i will be the widget. will pass button
        print(i.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


'''
All options for buttons in the messagebox

QMessageBox.Ok
QMessageBox.Open
QMessageBox.Save
QMessageBox.Cancel
QMessageBox.Close
QMessageBox.Yes
QMessageBox.No
QMessageBox.Abort
QMessageBox.Retry
QMessageBox.Ignore



'''