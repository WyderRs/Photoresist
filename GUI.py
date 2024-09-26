import PyQt5
from PyQt5 import QtWidgets, uic

import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('MainW.ui', self)
        # Кнопка 1
        self.button_1 = self.findChild(QtWidgets.QPushButton, 'pushButton_1')
        self.button_1.clicked.connect(self.Button_1)
        # Кнопка 1
        self.button_2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.button_2.clicked.connect(self.Button_2)
        # Кнопка 1
        self.button_3 = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
        self.button_3.clicked.connect(self.Button_3)
        # Кнопка 1
        self.button_4 = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
        self.button_4.clicked.connect(self.Button_4)
        # Кнопка 1
        self.button_5 = self.findChild(QtWidgets.QPushButton, 'pushButton_5')
        self.button_5.clicked.connect(self.Button_5)
        # Кнопка 1
        self.button_6 = self.findChild(QtWidgets.QPushButton, 'pushButton_6')
        self.button_6.clicked.connect(self.Button_6)
        # Кнопка 1
        self.button_7 = self.findChild(QtWidgets.QPushButton, 'pushButton_7')
        self.button_7.clicked.connect(self.Button_7)
        # Кнопка 1
        self.button_8 = self.findChild(QtWidgets.QPushButton, 'pushButton_8')
        self.button_8.clicked.connect(self.Button_8)
        # Кнопка 1
        self.button_9 = self.findChild(QtWidgets.QPushButton, 'pushButton_9')
        self.button_9.clicked.connect(self.Button_9)
        # Кнопка 1
        self.button_10 = self.findChild(QtWidgets.QPushButton, 'pushButton_10')
        self.button_10.clicked.connect(self.Button_10)
        # Кнопка 1
        self.button_11 = self.findChild(QtWidgets.QPushButton, 'pushButton_11')
        self.button_11.clicked.connect(self.Button_11)
        # Кнопка 1
        self.button_12 = self.findChild(QtWidgets.QPushButton, 'pushButton_12')
        self.button_12.clicked.connect(self.Button_12)
        # Кнопка 1
        self.button_13 = self.findChild(QtWidgets.QPushButton, 'pushButton_13')
        self.button_13.clicked.connect(self.Button_13)
        # Кнопка 1
        self.button_14 = self.findChild(QtWidgets.QPushButton, 'pushButton_14')
        self.button_14.clicked.connect(self.Button_14)
        # Кнопка 1
        self.button_15 = self.findChild(QtWidgets.QPushButton, 'pushButton_15')
        self.button_15.clicked.connect(self.Button_15)
        # Кнопка 1
        self.button_16 = self.findChild(QtWidgets.QPushButton, 'pushButton_16')
        self.button_16.clicked.connect(self.Button_16)
        # Кнопка 1
        self.button_17 = self.findChild(QtWidgets.QPushButton, 'pushButton_17')
        self.button_17.clicked.connect(self.Button_17)
        # Кнопка 1
        self.button_18 = self.findChild(QtWidgets.QPushButton, 'pushButton_18')
        self.button_18.clicked.connect(self.Button_18)
        # Кнопка 1
        self.button_19 = self.findChild(QtWidgets.QPushButton, 'pushButton_19')
        self.button_19.clicked.connect(self.Button_19)
        # Кнопка 1
        self.button_20 = self.findChild(QtWidgets.QPushButton, 'pushButton_20')
        self.button_20.clicked.connect(self.Button_20)
        # Кнопка 1
        self.button_21 = self.findChild(QtWidgets.QPushButton, 'pushButton_21')
        self.button_21.clicked.connect(self.Button_21)
        # Кнопка 1
        self.button_22 = self.findChild(QtWidgets.QPushButton, 'pushButton_22')
        self.button_22.clicked.connect(self.Button_22)
        # Кнопка 1
        self.button_23 = self.findChild(QtWidgets.QPushButton, 'pushButton_23')
        self.button_23.clicked.connect(self.Button_23)
        # Кнопка 1
        self.button_24 = self.findChild(QtWidgets.QPushButton, 'pushButton_24')
        self.button_24.clicked.connect(self.Button_24)
        # Кнопка 1
        self.button_25 = self.findChild(QtWidgets.QPushButton, 'pushButton_25')
        self.button_25.clicked.connect(self.Button_25)

        # Линия 1
        self.lineText_1 = self.findChild(QtWidgets.QLineEdit, 'lineEdit')

        self.show()



    def Button_1(self):
        print("But1")
    def Button_2(self):
        print("But2")
    def Button_3(self):
        print("But3")
    def Button_4(self):
        print("But4")
    def Button_5(self):
        print("But5")
    def Button_6(self):
        print("But6")
    def Button_7(self):
        print("But7")
    def Button_8(self):
        print("But8")
    def Button_9(self):
        print("But9")
    def Button_10(self):
        print("But10")
    def Button_11(self):
        print("But11")
    def Button_12(self):
        print("But12")
    def Button_13(self):
        print("But13")
    def Button_14(self):
        print("But14")
    def Button_15(self):
        print("But15")
    def Button_16(self):
        print("But16")
    def Button_17(self):
        print("But17")
    def Button_18(self):
        print("But18")
    def Button_19(self):
        print("But19")
    def Button_20(self):
        print("But20")
    def Button_21(self):
        print("But21")
    def Button_22(self):
        print("But22")
    def Button_23(self):
        print("But23")
    def Button_24(self):
        print("But24")
    def Button_25(self):
        print("But25")

def GUI_Begin():
    app = QtWidgets.QApplication(sys.argv)
    wind = MainWindow()

    app.exec_()
