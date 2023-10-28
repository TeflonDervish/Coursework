from PyQt5.QtWidgets import *
import sys

from Forms.LoginWindow import Ui_LoginWindow

class Window1(QMainWindow):
    def __init__(self):
        super(Window1, self).__init__()

        self.setWindowTitle("Редактор кода")
        self.move(200, 200)
        self.setFixedSize(400, 400)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QWidget
    ui = Ui_LoginWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())