# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtWidgets import QApplication
from Window import Window
from Dialog import Dialog

if __name__ == "__main__":
    app = QApplication([])
    w = Window()
    w.show()
    sys.exit(app.exec_())
