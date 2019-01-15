import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets

form_class=uic.loadUiType('C:\\Users\\windows10\PycharmProjects\\untitled2\\untitled.ui')[0]

class MYWindowClass(QtWidgets.QMainWindow, form_class) :
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.ctokbutton.clicked.connect(self.ctokbutton_clicked)
        self.ktocbutton.clicked.connect(self.ktocbutton_clicked)
    def ctokbutton_clicked(self):
        cel = float(self.ctokedit.text())
        fahr = cel * 9 / 5.0 + 32
        self.ctokedit.setText(str(fahr))
    def ktocbutton_clicked(self):
        fahr = float(self.ktocedit.text())
        cel = (fahr - 32) * 5 / 9.0
        self.ktocedit.setText(str(cel))
app = QtWidgets.QApplication(sys.argv)
myWindow = MYWindowClass()
myWindow.show()
app.exec_()