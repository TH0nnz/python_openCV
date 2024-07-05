# import socket
# import cv2
# import io
# from PIL import Image
# import numpy as np
#
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
# s.bind(("172.20.10.10", 9091))
# while True:
#     data, IP = s.recvfrom(100000)
#     bytes_stream = io.BytesIO(data)
#     image = Image.open(bytes_stream)
#     img = np.asarray(image)
#     cv2.imshow("12", img)
#     if cv2.waitKey(1) == ord("q"):
#         break


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.bind(("172.20.10.10", 9091))  # 绑定自身IP与端口

app = []  # 存放APP的IP地址
while True:
    data, IP = s.recvfrom(100000)
    if data.split(b":")[0] == b"e4a":  # APP标识符
        app.append(IP)

    elif data.split(b":")[0] == b"esp32":  # esp32标识符

        for i in app:  # 有多少个APP地址就发多少个
            s.sendto(data.split(b":", 1)[1], i)
