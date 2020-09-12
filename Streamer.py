# This Python file uses the following encoding: utf-8

import multiprocessing
import struct
import socket
import threading
from PIL.ImageQt import ImageQt

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap

SERVER = '0.0.0.0'
PORT = 777

class Streamer:
    def __init__(self):
        self.socket = None
        self.connection = None
        pass

    def connectTCP(self, label):
        self.socket.listen(0)
        self.connection = self.socket.accept()[0].makefile('rb')
        try:
            while True:
                image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
                if not image_len:
                    break
                image_stream = io.BytesIO()
                image_stream.write(connection.read(image_len))
                image_stream.seek(0)
                qim = ImageQt(image_stream)
                pix = QtGui.QPixmap.fromImage(qim)
                label.setPixmap(pix)
        finally:
            self.connection.close()
            self.socket.close()

    def start_stream(self, label):
        self.close_stream()
        self.socket = socket()
        self.socket.bind(SERVER, PORT)
        connectTCP(label)

    def close_stream(self):
        if self.socket != None and self.connection != None:
            self.connection.close()
            self.socket.close()

    def __del__(self):
        del self.connection
        del self.socket
