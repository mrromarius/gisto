from ast import Assign
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from PyQt5.QtCore import QRect, Qt
from QueryTable1 import Ui_QueryTable1
import pyqtgraph as pg
import numpy as np



from MainWindow import Ui_MainWindow
from Histogram import Ui_Histogram
from Ontology import Ui_Ontology
from QueryTable1 import Ui_QueryTable1
from QueryTable2 import Ui_QueryTable2
from QueryTable3 import Ui_QueryTable3
from QueryTable4 import Ui_QueryTable4

class GistoWindow(QtWidgets.QMainWindow, Ui_Histogram):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_close)
        self.pushButton_gisto.clicked.connect(self.click_load_gisto)

    def click_close(self):

        self.close()

    def click_load_gisto(self):
        # хороший способ реализации, но тогда нужно полностью сделать генерацию формы
        # https://www.cyberforum.ru/python-graphics/thread1513449.html#post7966919
        print('load gistogram')
        
        # тут делаем жуткий хард-код потому что временя н еждет, можно потом переделать всю форму на динамическое создание
        ya_data = [int(self.lineEdit_1.text()),int(self.lineEdit_2.text()),int(self.lineEdit_3.text()),int(self.lineEdit_4.text()),int(self.lineEdit_5.text()), 
        int(self.lineEdit_6.text()),int(self.lineEdit_7.text()),int(self.lineEdit_8.text()),int(self.lineEdit_9.text()), int(self.lineEdit_10.text()),
        int(self.lineEdit_11.text()),int(self.lineEdit_12.text()),int(self.lineEdit_13.text()),int(self.lineEdit_14.text()),int(self.lineEdit_15.text()), 
        int(self.lineEdit_16.text()),int(self.lineEdit_17.text()),int(self.lineEdit_18.text()),int(self.lineEdit_19.text()), int(self.lineEdit_20.text()),
        int(self.lineEdit_21.text()),int(self.lineEdit_22.text()),int(self.lineEdit_23.text()),int(self.lineEdit_24.text()), int(self.lineEdit_25.text()),
        int(self.lineEdit_26.text()),int(self.lineEdit_27.text()),int(self.lineEdit_28.text()),int(self.lineEdit_29.text()), int(self.lineEdit_30.text()), 
        int(self.lineEdit_31.text()),int(self.lineEdit_32.text()),int(self.lineEdit_33.text()),int(self.lineEdit_34.text()), int(self.lineEdit_35.text()), 
        int(self.lineEdit_36.text()),int(self.lineEdit_37.text()),int(self.lineEdit_38.text()),int(self.lineEdit_39.text()), int(self.lineEdit_40.text()), 
        int(self.lineEdit_41.text()),int(self.lineEdit_42.text()),int(self.lineEdit_43.text()),int(self.lineEdit_44.text()), int(self.lineEdit_45.text()),
        int(self.lineEdit_46.text()),int(self.lineEdit_47.text()),int(self.lineEdit_48.text()),int(self.lineEdit_49.text()), int(self.lineEdit_50.text())]
        y = [i for i in range(1, 52)]
        self.graphWidget.clear()
        self.graphWidget.setGeometry(QRect(410, 70, 800, 600))
        self.graphWidget.plot(y, ya_data, stepMode=True, fillLevel = 0, brush=(0,0,255,150))
        # забавный факт если передаем праметры в грид лайаут происходит ошибка, но зато вырвнивание работает нормально
        # если убрать то все норм, но припервом запуске проиходит смещение графика
        grid = QtWidgets.QGridLayout(self.centralwidget, 'fix_me')
        grid.addWidget(self.graphWidget, 0, 0, Qt.AlignCenter)

class OntoWindow(QtWidgets.QMainWindow, Ui_Ontology):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_close)

    def click_close(self):
        self.close()

class Table1Window(QtWidgets.QMainWindow, Ui_QueryTable1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_close)
        self.pushButton_3.clicked.connect(self.click_save_to_excel)

    def click_close(self):
        self.close()

    def click_save_to_excel(self):
        # https://ru.stackoverflow.com/questions/1119966/%D0%9A%D0%B0%D0%BA-%D1%81%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D1%8C-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5-%D0%B8%D0%B7-qtablewidget-%D0%B2-xls
        # https://ru.stackoverflow.com/questions/1270717/%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D1%8F%D1%82%D1%8C-%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D1%83-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8-%D0%B2-%D1%84%D0%B0%D0%B9%D0%BB-excel
        # https://www.cyberforum.ru/python-graphics/thread2220443.html
        print('смотри комменты')

class Table2Window(QtWidgets.QMainWindow, Ui_QueryTable2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_close)

    def click_close(self):
        self.close()

class Table3Window(QtWidgets.QMainWindow, Ui_QueryTable3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_close)

    def click_close(self):
        self.close()

class Table4Window(QtWidgets.QMainWindow, Ui_QueryTable4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_close)

    def click_close(self):
        self.close()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_5.clicked.connect(self.click_ontol)
        self.ui.pushButton_6.clicked.connect(self.click_gisto)
        self.ui.pushButton.clicked.connect(self.click_table1)
        self.ui.pushButton_2.clicked.connect(self.click_table2)
        self.ui.pushButton_3.clicked.connect(self.click_table3)
        self.ui.pushButton_4.clicked.connect(self.click_table4)

    def click_ontol(self):
        self.onto = OntoWindow()
        self.onto.show()

    def click_table1(self):
        self.table1 = Table1Window()
        self.table1.show()

    def click_table2(self):
        self.table2 = Table2Window()
        self.table2.show()

    def click_table3(self):
        self.table3 = Table3Window()
        self.table3.show()

    def click_table4(self):
        self.table4 = Table4Window()
        self.table4.show()

    def click_gisto(self):
        self.gisto = GistoWindow()
        self.gisto.show()




def main():
    app = QApplication([])
    application = MainWindow()
    application.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()