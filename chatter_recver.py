import socket
import time
import os
import platform
import pickle
TCP_IP = '127.0.0.1'
TCP_PORT = 8885
BUFFER_SIZE = 1024 # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(50)
conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    print "received data:", pickle.loads(data)
    conn.send(data)  # echo
conn.close()