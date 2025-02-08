from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from time import sleep

from Data import *
from Classes import *
from MarketMechanics import *
from ProductionMechanics import *
from economic_simulation import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Economic Simulator")

    def initUI(self):
        self.label = QtWidgets.QTextBrowser(self)
        self.label.setText("my first label")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Create Pops')
        self.b1.clicked.connect(createCitizens)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText('Display Data (all)')
        self.b2.move(100, 0)
        self.b2.clicked.connect(self.display)

    def display(self, result):
        result = display_current_info_in_ui()
        self.label.setText(result)
        self.update()

    def update(self):
        self.label.adjustSize()




def window():
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    display_current_info()
    sys.exit(app.exec())

window()