import socket
import sys
import time



TCP_IP = ''
TCP_PORT = 50007
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Server socket is created')
try:
    s.bind((TCP_IP, TCP_PORT))
except:
    print('Error: No binding could be done')
    sys.exit()

s.listen(0)
print('Socket is now listening')

conn,addr = s.accept()
print('Connection address:', addr)

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data:
       break
    ReceivedData = str(data.decode('utf-8'))
    print('Received data: ', ReceivedData)
    conn.sendall(data) #echo
    if ReceivedData == 'c':
        break
conn.close()
time.sleep(1)
print('Connection closed!')
    
