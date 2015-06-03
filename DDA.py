import sys
import pylab


from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):  # создаем главное окно.
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.window = QtGui.QWidget(self)
        self.resize(500, 650)
        screen = QtGui.QDesktopWidget().screenGeometry()
        # задаем размер
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)
        self.setWindowTitle('DDA-линии')
        # вставляем кнопки
        self.b = QtGui.QPushButton('График', self)
        self.b.setGeometry(65, 250, 75, 35)
        self.connect(self.b, QtCore.SIGNAL('clicked()'), self.Call)
        self.bu = QtGui.QPushButton('Выход', self)
        self.bu.setGeometry(300, 240, 75, 35)
        self.connect(self.bu, QtCore.SIGNAL('clicked()'),
                     QtCore.SLOT('close()'))

    def closeEvent(self, event):  # вопрос о подтверждении выхода
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?",
                                           QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.Yes)
        if reply == QtGui.QMessageBox.Yes:
            self.message('And remember:\n',
                         'Reality is an illusion, the universe is a hologram',
                         'buy gold, bye!',
                         'Secret')
            event.accept()
        else:
            event.ignore()
    Call = lambda self:inquiryDialog.get_data()


class inquiryDialog(QtGui.QDialog):  # окно диалога
    def __init__(self, parent=None):  # оформляем
        global t1, t2, t3, t4
        super(inquiryDialog, self).__init__(parent)
        self.setWindowTitle('Координаты')
        self.setGeometry(650, 410, 150, 150)
        self.begin = QtGui.QLineEdit(self)
        self.end = QtGui.QLineEdit(self)
        self.tb = QtGui.QLabel(';', self)
        self.te = QtGui.QLabel(';', self)
        self.nbegin = QtGui.QLabel('Начало: (', self)
        self.nend = QtGui.QLabel('Конец:   (', self)
        self.begin1 = QtGui.QLineEdit(self)
        self.end1 = QtGui.QLineEdit(self)
        self.beginn = QtGui.QLabel(')', self)
        self.endn = QtGui.QLabel(')', self)
        self.OKbutton = QtGui.QPushButton('Ok', self)
        self.Canbutton = QtGui.QPushButton('Cansel', self)
        self.connect(self.OKbutton, QtCore.SIGNAL('clicked()'), self.setCor)
        self.connect(self.Canbutton, QtCore.SIGNAL('clicked()'),
                     QtCore.SLOT('close()'))
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
        grid.addWidget(self.Canbutton, 7, 7)
        grid.addWidget(self.OKbutton, 7, 6)
        grid.addWidget(Label, 1, 2, 1, 7)
        grid.addWidget(QtGui.QLabel(''), 6, 1, 1, 6)
        self.setLayout(grid)

    def message(self, message, name):  # выводит сообщение в нужное время
        reply = QtGui.QMessageBox.question(self, name,
                                           message, QtGui.QMessageBox.Yes)

    def setCor(self):  # реализация алгоритма DDA-линии
        try:
            global t1, t2, t3, t4
            # переводим введенные числа в вещественный тип
            t1 = float(self.begin.text())
            t2 = float(self.begin1.text())
            t3 = float(self.end.text())
            t4 = float(self.end1.text())
        except ValueError:  # контролируем ввод
            self.message('Неверный тип ввода данных!\n',
                         'Вводить нужно числа вещественного или целого типа',
                         'Error')
            self.close
        self.accept()
        # округляем
        xstart = round(t1)
        xend = round(t3)
        ystart = round(t2)
        yend = round(t4)
        # находим число шагов
        Len = max(abs(xend-xstart), abs(yend-ystart))+1
        # увеличиваем значение и заполняем массив
        dx = (t3-t1)/Len
        dy = (t4-t2)/Len
        i = 0
        x = []
        y = []
        x += [t1]
        y += [t2]
        i += 1
        while (i < Len):
            x += [x[i-1] + dx]
            y += [y[i-1] + dy]
            i += 1
        x += [t3]
        y += [t4]
        # чертим прямую
        pylab.plot(x, y)
        pylab.show()

    def get(self):
        return self.begin

    @staticmethod
    def get_data(parent=None):
        a = inquiryDialog(parent)
        result = a.exec_()
        x = a.get()
        return (x.text(), result == QtGui.QDialog.Accepted)
if __name__ == "__main__":  # запуск
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    pal = main.palette()
    pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Background,
                 QtGui.QBrush(QtGui.QPixmap("Bill.png")))
    main.setPalette(pal)
    main.show()
    app.exec_()
