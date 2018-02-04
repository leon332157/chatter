import socket
import time
import os
import platform
import pickle
while True:
 TCP_IP = raw_input('ip:')
 TCP_PORT = int(raw_input('port:'))
 BUFFER_SIZE = 1024
 MESSAGE = raw_input('message:')
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect((TCP_IP, TCP_PORT))
 s.send(pickle.dumps(MESSAGE))