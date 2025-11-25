import io
import socket
import struct
from PIL import Image
import cv2
import numpy as np
import sys

server_socket = socket.socket()
server_socket.bind((sys.argv[1], int(sys.argv[2])))
server_socket.listen(0)
print("Listening for incoming stream...")

connection = server_socket.accept()[0].makefile('rb')

try:
    while True:
        raw_len = connection.read(struct.calcsize('<L'))
        if not raw_len:
            break

        image_len = struct.unpack('<L', raw_len)[0]
        if not image_len:
            break

        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        image_stream.seek(0)

        image = Image.open(image_stream)
        frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imshow('Video Stream', frame)

        if cv2.waitKey(1) == ord('q'):
            break

finally:
    cv2.destroyAllWindows()
    connection.close()
    server_socket.close()