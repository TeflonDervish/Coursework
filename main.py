from PyQt5.QtWidgets import *
import sys

from Forms.LoginWindow import Ui_LoginWindow

<<<<<<< HEAD
if __name__ == "__main__":
    app = QApplication(sys.argv)
    log = Ui_LoginWindow()
    log.show()
    sys.exit(log.exec_())
=======
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
>>>>>>> 28134ae24f4eadadc84bdf57ee7740b0d16d2a30
