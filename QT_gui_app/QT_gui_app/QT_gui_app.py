import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QIcon('pythonlogo.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())