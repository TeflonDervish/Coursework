from PyQt5.QtWidgets import *
import sys

from Forms.LoginWindow import Ui_LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    log = Ui_LoginWindow()
    log.show()
    sys.exit(log.exec_())