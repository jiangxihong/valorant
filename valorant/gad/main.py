from Login import *
from Signup import *
import sys
from func import *
import sys
from random import randint
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QLabel, QWidget,QLineEdit, QToolButton, QGroupBox, QMessageBox)
from PyQt5.QtCore import pyqtSignal,Qt 
from PyQt5.QtGui import QIcon,QFont
import func
import Signup
import FirstPage

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login.Login()
    login.show()
    sys.exit(app.exec_())