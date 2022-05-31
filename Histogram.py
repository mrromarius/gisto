# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Histogram.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QRect, QSize



class Ui_Histogram(object):
    def setupUi(self, Histogram):
        Histogram.setObjectName("Histogram")
        Histogram.resize(1343, 865)
        Histogram.setStyleSheet("background-color:rgb(174, 221, 242)")

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)

        self.centralwidget = QWidget(Histogram)
        self.centralwidget.setObjectName(u"centralwidget")
        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setGeometry(QRect(410, 70, 800, 600))
        self.graphWidget.setMaximumSize(QSize(800, 600))
        self.graphWidget.setBaseSize(QSize(800, 600))
        Histogram.setCentralWidget(self.centralwidget)

        self.pushButton = QtWidgets.QPushButton(Histogram)
        self.pushButton.setGeometry(QtCore.QRect(410, 10, 131, 31))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border-radius: 30px;\n"
"border: 1.5px solid")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_gisto = QtWidgets.QPushButton(Histogram)
        self.pushButton_gisto.setGeometry(QtCore.QRect(542, 10, 131, 31))
        self.pushButton_gisto.setFont(font)
        self.pushButton_gisto.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border-radius: 30px;\n"
"border: 1.5px solid")
        self.pushButton_gisto.setObjectName("pushButton_gisto")

        self.lineEdit_1 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_1.setGeometry(QtCore.QRect(150, 50, 61, 31))
        self.lineEdit_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label = QtWidgets.QLabel(Histogram)
        self.label.setGeometry(QtCore.QRect(110, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:10;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Histogram)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:10;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Histogram)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 91, 31))
        self.label_3.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Histogram)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 91, 31))
        self.label_4.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Histogram)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 91, 31))
        self.label_5.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Histogram)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 91, 31))
        self.label_6.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Histogram)
        self.label_7.setGeometry(QtCore.QRect(10, 170, 91, 31))
        self.label_7.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Histogram)
        self.label_8.setGeometry(QtCore.QRect(10, 260, 91, 31))
        self.label_8.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Histogram)
        self.label_9.setGeometry(QtCore.QRect(10, 230, 91, 31))
        self.label_9.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Histogram)
        self.label_10.setGeometry(QtCore.QRect(10, 290, 91, 31))
        self.label_10.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Histogram)
        self.label_11.setGeometry(QtCore.QRect(10, 320, 91, 31))
        self.label_11.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Histogram)
        self.label_12.setGeometry(QtCore.QRect(10, 200, 91, 31))
        self.label_12.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Histogram)
        self.label_13.setGeometry(QtCore.QRect(10, 410, 91, 31))
        self.label_13.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Histogram)
        self.label_14.setGeometry(QtCore.QRect(10, 380, 91, 31))
        self.label_14.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Histogram)
        self.label_15.setGeometry(QtCore.QRect(10, 440, 91, 31))
        self.label_15.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Histogram)
        self.label_16.setGeometry(QtCore.QRect(10, 470, 91, 31))
        self.label_16.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Histogram)
        self.label_17.setGeometry(QtCore.QRect(10, 350, 91, 31))
        self.label_17.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Histogram)
        self.label_18.setGeometry(QtCore.QRect(10, 560, 91, 31))
        self.label_18.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Histogram)
        self.label_19.setGeometry(QtCore.QRect(10, 530, 91, 31))
        self.label_19.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Histogram)
        self.label_20.setGeometry(QtCore.QRect(10, 590, 91, 31))
        self.label_20.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Histogram)
        self.label_21.setGeometry(QtCore.QRect(10, 620, 91, 31))
        self.label_21.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(Histogram)
        self.label_22.setGeometry(QtCore.QRect(10, 500, 91, 31))
        self.label_22.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(Histogram)
        self.label_23.setGeometry(QtCore.QRect(10, 710, 91, 31))
        self.label_23.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Histogram)
        self.label_24.setGeometry(QtCore.QRect(10, 680, 91, 31))
        self.label_24.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(Histogram)
        self.label_25.setGeometry(QtCore.QRect(10, 740, 91, 31))
        self.label_25.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(Histogram)
        self.label_26.setGeometry(QtCore.QRect(10, 770, 91, 31))
        self.label_26.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(Histogram)
        self.label_27.setGeometry(QtCore.QRect(10, 650, 91, 31))
        self.label_27.setStyleSheet("background-color: rgb(250, 250, 125);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.label_27.setObjectName("label_27")
        self.lineEdit_2 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 80, 61, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 110, 61, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 140, 61, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 170, 61, 31))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_7.setGeometry(QtCore.QRect(150, 230, 61, 31))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_10 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_10.setGeometry(QtCore.QRect(150, 320, 61, 31))
        self.lineEdit_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 200, 61, 31))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_9 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_9.setGeometry(QtCore.QRect(150, 290, 61, 31))
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_8.setGeometry(QtCore.QRect(150, 260, 61, 31))
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_12 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_12.setGeometry(QtCore.QRect(150, 380, 61, 31))
        self.lineEdit_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_15 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_15.setGeometry(QtCore.QRect(150, 470, 61, 31))
        self.lineEdit_15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_11 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_11.setGeometry(QtCore.QRect(150, 350, 61, 31))
        self.lineEdit_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_19 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_19.setGeometry(QtCore.QRect(150, 590, 61, 31))
        self.lineEdit_19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_17 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_17.setGeometry(QtCore.QRect(150, 530, 61, 31))
        self.lineEdit_17.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_14 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_14.setGeometry(QtCore.QRect(150, 440, 61, 31))
        self.lineEdit_14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_13 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_13.setGeometry(QtCore.QRect(150, 410, 61, 31))
        self.lineEdit_13.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_18 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_18.setGeometry(QtCore.QRect(150, 560, 61, 31))
        self.lineEdit_18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_16 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_16.setGeometry(QtCore.QRect(150, 500, 61, 31))
        self.lineEdit_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_20 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_20.setGeometry(QtCore.QRect(150, 620, 61, 31))
        self.lineEdit_20.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_21.setGeometry(QtCore.QRect(150, 650, 61, 31))
        self.lineEdit_21.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_25 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_25.setGeometry(QtCore.QRect(150, 770, 61, 31))
        self.lineEdit_25.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_25.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_24 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_24.setGeometry(QtCore.QRect(150, 740, 61, 31))
        self.lineEdit_24.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_24.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_22 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_22.setGeometry(QtCore.QRect(150, 680, 61, 31))
        self.lineEdit_22.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_23.setGeometry(QtCore.QRect(150, 710, 61, 31))
        self.lineEdit_23.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_23.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_46 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_46.setGeometry(QtCore.QRect(290, 650, 61, 31))
        self.lineEdit_46.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_46.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.lineEdit_39 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_39.setGeometry(QtCore.QRect(290, 440, 61, 31))
        self.lineEdit_39.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_39.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.lineEdit_41 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_41.setGeometry(QtCore.QRect(290, 500, 61, 31))
        self.lineEdit_41.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_41.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.lineEdit_35 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_35.setGeometry(QtCore.QRect(290, 320, 61, 31))
        self.lineEdit_35.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_35.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.lineEdit_36 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_36.setGeometry(QtCore.QRect(290, 350, 61, 31))
        self.lineEdit_36.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_36.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.lineEdit_40 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_40.setGeometry(QtCore.QRect(290, 470, 61, 31))
        self.lineEdit_40.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_40.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.lineEdit_48 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_48.setGeometry(QtCore.QRect(290, 710, 61, 31))
        self.lineEdit_48.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_48.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.lineEdit_30 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_30.setGeometry(QtCore.QRect(290, 170, 61, 31))
        self.lineEdit_30.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_30.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.lineEdit_31 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_31.setGeometry(QtCore.QRect(290, 200, 61, 31))
        self.lineEdit_31.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_31.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.lineEdit_37 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_37.setGeometry(QtCore.QRect(290, 380, 61, 31))
        self.lineEdit_37.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_37.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.lineEdit_29 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_29.setGeometry(QtCore.QRect(290, 140, 61, 31))
        self.lineEdit_29.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_29.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_43 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_43.setGeometry(QtCore.QRect(290, 560, 61, 31))
        self.lineEdit_43.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_43.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.lineEdit_33 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_33.setGeometry(QtCore.QRect(290, 260, 61, 31))
        self.lineEdit_33.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_33.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_26 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_26.setGeometry(QtCore.QRect(290, 50, 61, 31))
        self.lineEdit_26.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_26.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_50 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_50.setGeometry(QtCore.QRect(290, 770, 61, 31))
        self.lineEdit_50.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_50.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.lineEdit_42 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_42.setGeometry(QtCore.QRect(290, 530, 61, 31))
        self.lineEdit_42.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_42.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.lineEdit_38 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_38.setGeometry(QtCore.QRect(290, 410, 61, 31))
        self.lineEdit_38.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_38.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.lineEdit_45 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_45.setGeometry(QtCore.QRect(290, 620, 61, 31))
        self.lineEdit_45.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_45.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.lineEdit_27 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_27.setGeometry(QtCore.QRect(290, 80, 61, 31))
        self.lineEdit_27.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_27.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_47 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_47.setGeometry(QtCore.QRect(290, 680, 61, 31))
        self.lineEdit_47.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_47.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.lineEdit_32 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_32.setGeometry(QtCore.QRect(290, 230, 61, 31))
        self.lineEdit_32.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_32.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.lineEdit_49 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_49.setGeometry(QtCore.QRect(290, 740, 61, 31))
        self.lineEdit_49.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_49.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.lineEdit_34 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_34.setGeometry(QtCore.QRect(290, 290, 61, 31))
        self.lineEdit_34.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_34.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.lineEdit_28 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_28.setGeometry(QtCore.QRect(290, 110, 61, 31))
        self.lineEdit_28.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_28.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_44 = QtWidgets.QLineEdit(Histogram)
        self.lineEdit_44.setGeometry(QtCore.QRect(290, 590, 61, 31))
        self.lineEdit_44.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:30px;\n"
"")
        self.lineEdit_44.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_44.setObjectName("lineEdit_44")

        self.retranslateUi(Histogram)
        QtCore.QMetaObject.connectSlotsByName(Histogram)

    def retranslateUi(self, Histogram):
        _translate = QtCore.QCoreApplication.translate
        Histogram.setWindowTitle(_translate("Histogram", "Dialog"))
        self.pushButton.setText(_translate("Histogram", "На главную "))
        self.pushButton_gisto.setText(_translate("Histogram", "Загрузить график"))
        self.label.setText(_translate("Histogram", "Запросы в Яндекс"))
        self.label_2.setText(_translate("Histogram", "Запросы в Google"))
        self.label_3.setText(_translate("Histogram", "Запрос №1"))
        self.label_4.setText(_translate("Histogram", "Запрос №2"))
        self.label_5.setText(_translate("Histogram", "Запрос №4"))
        self.label_6.setText(_translate("Histogram", "Запрос №3"))
        self.label_7.setText(_translate("Histogram", "Запрос №5"))
        self.label_8.setText(_translate("Histogram", "Запрос №8"))
        self.label_9.setText(_translate("Histogram", "Запрос №7"))
        self.label_10.setText(_translate("Histogram", "Запрос №9"))
        self.label_11.setText(_translate("Histogram", "Запрос №10"))
        self.label_12.setText(_translate("Histogram", "Запрос №6"))
        self.label_13.setText(_translate("Histogram", "Запрос №13"))
        self.label_14.setText(_translate("Histogram", "Запрос №12"))
        self.label_15.setText(_translate("Histogram", "Запрос №14"))
        self.label_16.setText(_translate("Histogram", "Запрос №15"))
        self.label_17.setText(_translate("Histogram", "Запрос №11"))
        self.label_18.setText(_translate("Histogram", "Запрос №18"))
        self.label_19.setText(_translate("Histogram", "Запрос №17"))
        self.label_20.setText(_translate("Histogram", "Запрос №19"))
        self.label_21.setText(_translate("Histogram", "Запрос №20"))
        self.label_22.setText(_translate("Histogram", "Запрос №16"))
        self.label_23.setText(_translate("Histogram", "Запрос №23"))
        self.label_24.setText(_translate("Histogram", "Запрос №22"))
        self.label_25.setText(_translate("Histogram", "Запрос №24"))
        self.label_26.setText(_translate("Histogram", "Запрос №25"))
        self.label_27.setText(_translate("Histogram", "Запрос №21"))
        self.lineEdit_1.setText(_translate("Histogram", u"0", None))
        self.lineEdit_2.setText(_translate("Histogram", u"0", None))
        self.lineEdit_3.setText(_translate("Histogram", u"0", None))
        self.lineEdit_4.setText(_translate("Histogram", u"0", None))
        self.lineEdit_5.setText(_translate("Histogram", u"0", None))
        self.lineEdit_6.setText(_translate("Histogram", u"0", None))
        self.lineEdit_7.setText(_translate("Histogram", u"0", None))
        self.lineEdit_8.setText(_translate("Histogram", u"0", None))
        self.lineEdit_9.setText(_translate("Histogram", u"0", None))
        self.lineEdit_10.setText(_translate("Histogram", u"0", None))
        self.lineEdit_11.setText(_translate("Histogram", u"0", None))
        self.lineEdit_12.setText(_translate("Histogram", u"0", None))
        self.lineEdit_13.setText(_translate("Histogram", u"0", None))
        self.lineEdit_14.setText(_translate("Histogram", u"0", None))
        self.lineEdit_15.setText(_translate("Histogram", u"0", None))
        self.lineEdit_16.setText(_translate("Histogram", u"0", None))
        self.lineEdit_17.setText(_translate("Histogram", u"0", None))
        self.lineEdit_18.setText(_translate("Histogram", u"0", None))
        self.lineEdit_19.setText(_translate("Histogram", u"0", None))
        self.lineEdit_20.setText(_translate("Histogram", u"0", None))
        self.lineEdit_21.setText(_translate("Histogram", u"0", None))
        self.lineEdit_22.setText(_translate("Histogram", u"0", None))
        self.lineEdit_23.setText(_translate("Histogram", u"0", None))
        self.lineEdit_24.setText(_translate("Histogram", u"0", None))
        self.lineEdit_25.setText(_translate("Histogram", u"0", None))
        self.lineEdit_26.setText(_translate("Histogram", u"0", None))
        self.lineEdit_27.setText(_translate("Histogram", u"0", None))
        self.lineEdit_28.setText(_translate("Histogram", u"0", None))
        self.lineEdit_29.setText(_translate("Histogram", u"0", None))
        self.lineEdit_30.setText(_translate("Histogram", u"0", None))
        self.lineEdit_31.setText(_translate("Histogram", u"0", None))
        self.lineEdit_32.setText(_translate("Histogram", u"0", None))
        self.lineEdit_33.setText(_translate("Histogram", u"0", None))
        self.lineEdit_34.setText(_translate("Histogram", u"0", None))
        self.lineEdit_35.setText(_translate("Histogram", u"0", None))
        self.lineEdit_36.setText(_translate("Histogram", u"0", None))
        self.lineEdit_37.setText(_translate("Histogram", u"0", None))
        self.lineEdit_38.setText(_translate("Histogram", u"0", None))
        self.lineEdit_39.setText(_translate("Histogram", u"0", None))
        self.lineEdit_40.setText(_translate("Histogram", u"0", None))
        self.lineEdit_41.setText(_translate("Histogram", u"0", None))
        self.lineEdit_42.setText(_translate("Histogram", u"0", None))
        self.lineEdit_43.setText(_translate("Histogram", u"0", None))
        self.lineEdit_44.setText(_translate("Histogram", u"0", None))
        self.lineEdit_45.setText(_translate("Histogram", u"0", None))
        self.lineEdit_46.setText(_translate("Histogram", u"0", None))
        self.lineEdit_47.setText(_translate("Histogram", u"0", None))
        self.lineEdit_48.setText(_translate("Histogram", u"0", None))
        self.lineEdit_49.setText(_translate("Histogram", u"0", None))
        self.lineEdit_50.setText(_translate("Histogram", u"0", None))

