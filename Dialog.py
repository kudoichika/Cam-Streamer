# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QCheckBox

class Dialog(QtWidgets.QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self)

        self.parent = parent

        nameLabel = QLabel('Name: ')
        self.nameText = QLineEdit()

        nameLayout = QHBoxLayout()
        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(self.nameText)

        connLabel = QLabel('Address (IPv4): ')
        self.connText = QLineEdit()
        portLabel = QLabel('Port: ')
        self.portText = QLineEdit()
        self.portText.setMaximumWidth(50)

        connLayout = QHBoxLayout()
        connLayout.addWidget(connLabel)
        connLayout.addWidget(self.connText)
        connLayout.addWidget(portLabel)
        connLayout.addWidget(self.portText)

        self.checkBox = QCheckBox('Save this configuration to my list for later')

        closeButton = QPushButton('Close')
        saveButton = QPushButton('Save')
        closeButton.clicked.connect(self.closeDialog)
        saveButton.clicked.connect(self.saveDialog)
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(closeButton)
        buttonLayout.addWidget(saveButton)

        layout = QVBoxLayout()
        layout.addLayout(nameLayout)
        layout.addLayout(connLayout)
        layout.addWidget(self.checkBox)
        layout.addLayout(buttonLayout)

        self.setLayout(layout)
        self.setFixedSize(400, 200)

    def saveDialog(self):
        if not self.checkBox.isChecked():
            print("Check Box Not Checked")
        if self.nameText.text() in self.parent.dict:
            print("Replacing Key Value")
        self.parent.dict[self.nameText.text()] = {
            'ip': self.connText.text(),
            'port': self.portText.text(),
            'save': self.checkBox.isChecked()
        }
        self.parent.updateCombos()
        self.closeDialog()

    def closeDialog(self):
        self.close()

    def __del__(self):
        del self.nameText
        del self.connText
        del self.portText
        del self.checkBox
