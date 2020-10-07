import struct
import socket
import time
import picamera

SERVER = '0.0.0.0'
SOCKET = 777
RESOLUTION = (640, 480)

server_socket = socket.socket()
server_socket.bind((SERVER, SOCKET))
server_socket.listen(0)

connection = server_socket.accept()[0].makefile('wb')
try:
	with picamera.PiCamera() as camera:
		camera.resolution = RESOLUTION
        time.sleep(2)
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
	server_socket.close()
