import io
import socket
import struct
import cv2
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((sys.argv[1], int(sys.argv[2])))
connection = client_socket.makefile('wb')

camera = cv2.VideoCapture(0)  # 0 = default laptop/webcam
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

try:
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Camera error")
            break

        # encode frame as JPEG
        ret, jpeg = cv2.imencode('.jpg', frame)
        data = jpeg.tobytes()

        # send length + frame
        connection.write(struct.pack('<L', len(data)))
        connection.flush()
        connection.write(data)

finally:
    camera.release()
    connection.close()
    client_socket.close()
