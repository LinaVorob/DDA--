import os
import sys
import PIL
import math
import matplotlib
import numpy
import pylab
import itertools
import random
from PyQt4 import QtGui, QtCore



class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)
        self.setWindowTitle('DDA-линии')
        self.b=QtGui.QPushButton('График',self)
        self.connect(self.b, QtCore.SIGNAL('clicked()'), self.coordinate)
        #self.But = QGui.QPushButton('Координаты', self)
        #self.connect(self.But, QtCore.SIGNAL('clicked()'), )

    def getLogin(self):
        return (self.begin, self.end, self.begin1, self.end1)

    def Dialog(self):#?
        dialog = LoginDialog(parent)
        result = dialog.exec_()
        t1, t2, t3, t4 = dialog.getLogin()
        return(t1.text(), t2.text(), t3.text(), t4.text(), result==QtGui.QDialog.Accepted)
        
    def coordinate(self):
        print(t1, t2, t3, t4)
        x1 = float(t1)
        y1 = float(t2)
        x2 = float(t3)
        y2 = float(t4)
        xstart = round(x1)
        xend = round(x2)
        ystart = round(y1)
        yend = round(y2)
        Len = max(abs(xend-xstart),abs(yend-ystart))+1
        dx = (x2-x1)/Len
        dy = (y2-y1)/Len

        i = 0
        x = []
        y = []
        x += [x1]
        y += [y1]
        i += 1
        while (i < Len):
            x += [x[i-1] + dx]
            y += [y[i-1] + dy]
            i+=1

        x += [x2]
        y += [y2]
        pylab.plot(x,y)
        pylab.show()

class LoginDialog(QtGui.QDialog):
    
    def __init__(self, parent=None):
        global t1, t2, t3, t4
        super(LoginDialog, self).__init__(parent)
        self.setWindowTitle('Координаты')
        self.setGeometry(650, 410, 150, 150)
        self.begin = QtGui.QLineEdit(self)
        self.end = QtGui.QLineEdit(self)
        self.tb = QtGui.QLabel(';', self)
        self.te = QtGui.QLabel(';', self)
        self.nbegin = QtGui.QLabel('Начало: (', self)
        self.nend = QtGui.QLabel ('Конец:   (', self)
        self.begin1 = QtGui.QLineEdit(self)
        self.end1 = QtGui.QLineEdit(self)
        self.beginn = QtGui.QLabel (')', self)
        self.endn = QtGui.QLabel (')', self)
         
        
        buttons = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel,
                QtCore.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        Label = QtGui.QLabel('Введите 2 числа через точку с запятой', self)

        grid = QtGui.QGridLayout(self)
        
        grid.addWidget(self.nbegin, 2, 2)
        grid.addWidget(self.begin, 2, 3)
        grid.addWidget(self.tb, 2, 4)
        grid.addWidget(self.begin1, 2, 5)
        grid.addWidget(self.beginn, 2, 6)
        
        grid.addWidget(self.nend, 4, 2)
        grid.addWidget(self.end, 4, 3)
        grid.addWidget(self.te, 4, 4)
        grid.addWidget(self.end1, 4, 5)
        grid.addWidget(self.endn, 4, 6)
        
        grid.addWidget(buttons, 7, 6)
        
        grid.addWidget(Label, 1, 2, 1, 7)
        grid.addWidget(QtGui.QLabel(''),6,1,1,6)
        self.setLayout(grid)
        
        
        
if __name__ == "__main__":
   
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    login = LoginDialog()
    login.show()

    app.exec_()
