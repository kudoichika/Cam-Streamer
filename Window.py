# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QComboBox

from Streamer import Streamer
from Dialog import Dialog

import os

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.dict = {} # make sure to avoid duplicates

        self.combo = QComboBox()
        self.combo.addItem('Choose a Connection')
        self.combo.setMaximumWidth(700)

        self.loadMemory()
        self.updateCombos()

        self.addButton = QPushButton('New')
        self.addButton.setMaximumWidth(80)
        self.addButton.clicked.connect(self.newConfig)

        configLayout = QHBoxLayout()
        configLayout.addWidget(self.combo)
        configLayout.addWidget(self.addButton)

        self.video = QImage()
        self.streamer = Streamer()

        self.label = QLabel()
        self.label.setPixmap(QPixmap.fromImage(self.video))

        self.connectButton = QPushButton('Connect')
        self.disconnectButton = QPushButton('Disconnect')
        self.connectButton.setMaximumWidth(150)
        self.disconnectButton.setMaximumWidth(150)
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.connectButton)
        buttonLayout.addWidget(self.disconnectButton)

        self.connectButton.clicked.connect(self.connect)
        self.disconnectButton.clicked.connect(self.disconnect)

        layout = QVBoxLayout()
        layout.addLayout(configLayout)
        layout.addWidget(self.label)
        layout.addLayout(buttonLayout)

        self.setLayout(layout)
        self.setFixedSize(600, 350)
        self.setWindowTitle("Streaming Application")

    def loadMemory(self):
        if os.path.exists('config.ufd'):
            with open('config.ufd', 'r') as file:
                lines = file.read().splitlines()
                for i in range(len(lines)//3):
                    self.dict[lines[3*i]] = {
                        'ip': lines[3*i+1],
                        'port': lines[3*i+2],
                        'save': True
                    }
        print("Dict", self.dict)

    def updateCombos(self):
        self.combo.clear()
        for key in self.dict:
            print(key)
            self.combo.addItem(key)

    def newConfig(self):
        self.d = Dialog(self)
        self.d.show()

    def connect(self):
        choice = self.dict[str(self.combo.currentText())]
        ip = choice['ip']
        port = int(choice['port'])
        self.streamer.start_stream(self.label, ip, port)

    def disconnect(self):
        self.streamer.close_stream()

    def closeEvent(self, event):
        with open('config.ufd', 'w') as file:
            for key in self.dict:
                print(key)
                if self.dict[key]['save']:
                    print(key, 'Writing\n')
                    file.write(key + os.linesep)
                    file.write(self.dict[key]['ip'] + os.linesep)
                    file.write(self.dict[key]['port'] + os.linesep)

    def __del__(self):
        del self.dict
        del self.combo
        del self.addButton
        del self.video
        del self.streamer
        del self.label
        del self.connectButton
        del self.disconnectButton
