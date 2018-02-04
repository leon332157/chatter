import socket
import time
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while True:
 try:
  s.send(MESSAGE)
  time.sleep(2)
  if s.recv == None:
      print 'bad'
  else:
      print 'sent'
 except KeyboardInterrupt:
     break
s.close()