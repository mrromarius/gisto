import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5 import QtWidgets
 
 


win = pg.GraphicsWindow()
win.resize(800,350)
win.setWindowTitle('pyqtgraph example: Histogram')
plt1 = win.addPlot()

y1=int(input("Запрос 1? "))
y2=int(input("Запрос 2? "))
y3=int(input("Запрос 3? "))
y4=int(input("Запрос 4? "))
y5=int(input("Запрос 5? "))
y6=int(input("Запрос 6? "))

x = [1, 2, 3, 4, 5, 6, 7]
y = [y1, y2, y3, y4, y5, y6]
 
 
plt1.plot(x, y, stepMode=True, fillLevel=0, brush=(0,0,255,150))
 
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()
