# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 14:02:32 2017

@author: fahad

This is TCP client code. Make sure that Server and Client can Ping eachother
before running the code, else it would not work.

"""

import socket
import sys
import time


TCP_IP = '192.168.31.148' # IP address of the server
TCP_PORT = 50007
BUFFER_SIZE = 1024 # To store charachters
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creating Socket
print('Client socket is created')
try:
    s.connect((TCP_IP, TCP_PORT))
    print('Connected')
except:
    print('An Error Occured!')
    sys.exit()

while True:
    MESSAGE = input('Please Enter ')    # Taking input from user
    message_bytes = MESSAGE.encode('utf-8')    ## Converting Message into Bytes
    s.sendall(message_bytes)    # Sending data to server
    if MESSAGE.upper() == 'C':    # Enter C to break/stop the loop
        break
    data = s.recv(BUFFER_SIZE) # Receiving data from server
    print ("received data:", data.decode('utf-8')) # Decoding received data and printing
    time.sleep(1) ## 1 second delay
s.close()   # Closing the TCP socket
print('Communication Closed')
