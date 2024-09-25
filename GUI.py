import PyQt5
from PyQt5 import QtWidgets, uic
import sys
from MainW import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('C:/Users/uSER/PycharmProjects/PhotoresistSoftware/MainW.ui', self)
        # Кнопка 1
        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.button.clicked.connect(self.ButtonSend)

        self.show()


    def ButtonSend(self):
        print('Send')

def GUI_Begin():
    app = QtWidgets.QApplication(sys.argv)
    wind = MainWindow()

    app.exec_()
