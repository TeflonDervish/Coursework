from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from WindowStarts.LoginWindow import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LoginWindow()
    win.show()
    sys.exit(app.exec_())
