import struct
import socket
import time
import picamera

SERVER = '192.168.1.185'
SOCKET = 777
RESOLUTION = (640, 480)

client_socket = socket.socket()
client_socket.connect((SERVER, SOCKET))

connection = client_socket.makefile('wb')
try:
    with picamera.PiCamera() as camera:
        camera.resolution = RESOLUTION
        time.sleep(2)
        start = time.time()
        stream = io.BytesIO()
        for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())
            stream.seek(0)
            stream.truncate()
    connection.write(struct.pack('<L', 0))
finally:
    connection.close()
    client_socket.close()
