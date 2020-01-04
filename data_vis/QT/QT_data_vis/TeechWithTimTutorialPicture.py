# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TechWithTimTutorialPicture.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 719)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photoFrame = QtWidgets.QLabel(self.centralwidget)
        self.photoFrame.setGeometry(QtCore.QRect(6, 2, 1101, 591))
        self.photoFrame.setText("")
        self.photoFrame.setPixmap(QtGui.QPixmap("lmao.jpg"))
        self.photoFrame.setScaledContents(True)
        self.photoFrame.setObjectName("photoFrame")
        self.lmaoButton = QtWidgets.QPushButton(self.centralwidget)
        self.lmaoButton.setGeometry(QtCore.QRect(220, 620, 131, 41))
        self.lmaoButton.setObjectName("lmaoButton")
        self.eyButton = QtWidgets.QPushButton(self.centralwidget)
        self.eyButton.setGeometry(QtCore.QRect(670, 620, 141, 41))
        self.eyButton.setObjectName("eyButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1111, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lmaoButton.clicked.connect(self.show_lmao)
        self.eyButton.clicked.connect(self.show_ey)             # connecting



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lmaoButton.setText(_translate("MainWindow", "LMAO"))
        self.eyButton.setText(_translate("MainWindow", "EY"))

    def show_lmao(self):
        self.photoFrame.setPixmap(QtGui.QPixmap("lmao.jpg"))            # showing lmao

    def show_ey(self):
        self.photoFrame.setPixmap(QtGui.QPixmap("ey.png"))              # showing ey


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
