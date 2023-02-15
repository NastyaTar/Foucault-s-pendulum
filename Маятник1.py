from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


class Attvud(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Моделирование колебаний маятника Фуко")
        Dialog.resize(542, 626)

        self.Result = QtWidgets.QPushButton(Dialog)
        self.Result.setGeometry(QtCore.QRect(370, 250, 161, 32))
        self.Result.setObjectName("Result")
        self.Result.clicked.connect(self.result)

        self.G = QtWidgets.QLabel(Dialog)
        self.G.setGeometry(QtCore.QRect(30, 170, 231, 16))
        self.G.setObjectName("G")

        self.L = QtWidgets.QLabel(Dialog)
        self.L.setGeometry(QtCore.QRect(30, 40, 60, 16))
        self.L.setObjectName("L")

        self.R = QtWidgets.QLabel(Dialog)
        self.R.setGeometry(QtCore.QRect(30, 210, 161, 16))
        self.R.setObjectName("R")

        self.Time = QtWidgets.QLabel(Dialog)
        self.Time.setGeometry(QtCore.QRect(30, 70, 151, 16))
        self.Time.setObjectName("Time")

        self.Ampl = QtWidgets.QLabel(Dialog)
        self.Ampl.setGeometry(QtCore.QRect(30, 100, 151, 16))
        self.Ampl.setObjectName("Ampl")

        self.const_2 = QtWidgets.QLabel(Dialog)
        self.const_2.setGeometry(QtCore.QRect(190, 130, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(18)

        self.const_2.setFont(font)
        self.const_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.const_2.setLineWidth(1)
        self.const_2.setTextFormat(QtCore.Qt.AutoText)
        self.const_2.setObjectName("const_2")

        self.L_2 = QtWidgets.QLineEdit(Dialog)
        self.L_2.setGeometry(QtCore.QRect(280, 40, 113, 21))
        self.L_2.setObjectName("L_2")

        self.Time_2 = QtWidgets.QLineEdit(Dialog)
        self.Time_2.setGeometry(QtCore.QRect(280, 70, 113, 21))
        self.Time_2.setObjectName("Time_2")

        self.Ample = QtWidgets.QLineEdit(Dialog)
        self.Ample.setGeometry(QtCore.QRect(280, 100, 113, 21))
        self.Ample.setObjectName("Ample")

        self.G_2 = QtWidgets.QLineEdit(Dialog)
        self.G_2.setGeometry(QtCore.QRect(280, 170, 113, 21))
        self.G_2.setObjectName("G_2")

        self.R_2 = QtWidgets.QLineEdit(Dialog)
        self.R_2.setGeometry(QtCore.QRect(280, 210, 113, 21))
        self.R_2.setObjectName("R_2")

        self.lbl = QtWidgets.QLabel(Dialog)
        self.lbl.setGeometry(QtCore.QRect(30, 300, 500, 580))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def result(self):
        g = float(self.G_2.text())
        L = int(self.L_2.text())
        R = float(self.R_2.text())
        time = int(self.Time_2.text())
        ampl = int(self.Ample.text())
        lamda = 3  # широта
        k_1 = 1
        k_2 = 1
        graphic = self.lbl

        # время
        t = np.arange(0, time, ampl)
        # определяем функции
        a_ = 1j * (np.sqrt(g / L) * t)
        a = np.exp(a_)

        b_ = 1j * ((-1) * np.sqrt(g / L) * t)
        b = np.exp(b_)

        c_ = 1j * (R * np.sin(lamda) * (-1) * t)

        c = np.exp(c_)
        u = (k_1 * a + k_2 * b) * c
        # разделение реальной и комплексной части
        x = u.real
        y = u.imag
        plt.xlim(-2.5, 2.5)
        plt.ylim(-2.5, 2.5)

        # строим график
        plt.plot(x, y, 'g')
        plt.grid()
        plt.savefig('Fuko.jpg')
        img = Image.open('Fuko.jpg').resize((511, 321)).save('Fuko.jpg')
        pix = QPixmap('Fuko.jpg')
        graphic.setPixmap(pix)
        graphic.move(20, 160)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Result.setText(_translate("Dialog", "Построить график"))
        self.G.setText(_translate("Dialog", "Ускорение свободного падения"))
        self.L.setText(_translate("Dialog", "Длина"))
        self.R.setText(_translate("Dialog", "Угловая скорость земли"))
        self.Time.setText(_translate("Dialog", "Диапазон времени до "))
        self.Ampl.setText(_translate("Dialog", "Амплитуда колебаний "))
        self.const_2.setText(_translate("Dialog", "Константы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Attvud()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())