# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 800)
        MainWindow.setStyleSheet("background-color:rgb(174, 221, 242)")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(70, 300, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border-radius: 30px;\n"
"border: 1.5px solid")
        self.pushButton.setCheckable(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 390, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border-radius: 30px;\n"
"border: 1.5px solid")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 480, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border-radius: 30px;\n"
"border: 1.5px solid")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 570, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border-radius: 30px;\n"
"border: 1.5px solid")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 210, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border-radius: 30px;\n"
"border: 1.5px solid")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 660, 371, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border-radius: 30px;\n"
"border: 1.5px solid")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(100, 60, 311, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????????? ????????"))
        self.pushButton.setText(_translate("MainWindow", "?????????????? ???????????????? ??? 1"))
        self.pushButton_2.setText(_translate("MainWindow", "?????????????? ???????????????? ???2"))
        self.pushButton_3.setText(_translate("MainWindow", "?????????????? ???????????????? ???3"))
        self.pushButton_4.setText(_translate("MainWindow", "?????????????? ???????????????? ???4"))
        self.pushButton_5.setText(_translate("MainWindow", "?????????????? ??????????????????"))
        self.pushButton_6.setText(_translate("MainWindow", "???????????????????? ?????????????????????? ???? ????????????????"))
        self.label.setText(_translate("MainWindow", "??O ?????? ???????????????????????? ???????????? ????????????????,?????????????????? ?? ???????????????????? ????????????????????"))
