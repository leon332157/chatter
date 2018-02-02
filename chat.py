import os
import platform
import socket as socket
import time
import threading as th
import _thread as thread
from functools import partial
import random
import pickle
device_list = []
raw_device_list = []
r_device_dict = {}
def msg_recv(conn,addr):
    while True:
     pick = conn.recv(4096)
     if not pick == '':
         break
    print(pickle.loads(pick))
    print('Enter to continue.')
    main()
    return
def msg_serv():
    while True:
     conn, addr = msg_sk.accept()
     s7 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
     try:
         s7.connect(('baidu.com',80))
         ip = s7.getsockname()
     except:
      ip = socket.gethostbyname(socket.gethostname())
     if not addr[0] == ip[0]:
      if not addr[0] == '127.0.0.1':
       thread.start_new_thread(msg_recv,(conn,addr))
def name_serv(name_sk, name_serv_stop, serv_name):
        while True:
            conn, addr = name_sk.accept()
            data = conn.recv(1024)
            if not data:
             conn.send(pickle.dumps(serv_name))
def send_msg(device_list, msg_port, name):
    if not device_list == []:
        pass
    else:
        print('Please get device first!')
        return ()
    f1 = open('Message Send.txt', 'a')
    show_device(device_list)
    r_device_dict.clear()
    for raw_each in device_list:
        each = raw_each.split(' ')
        r_device_dict[each[1]] = each[0]
    name_index = input('Input device name you want to send to:')
    if r_device_dict.get(name_index) == None:
        print('Please input valid name.')
        return ()
    else:
        host = r_device_dict.get(name_index)
    if host == socket.gethostbyname(socket.gethostname()):
        print('Message send to your self will be ignored my your message server.')
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('host'+host)
    try:
        s3.connect((host, msg_port))
        message = input('Message send to' + ' ' + str(name_index) + ':')
        f1.write(str('Time:' + ' ' + str(
            time.ctime()) + ' ' + 'host:' + ' ' + host + ' ' + 'name:' + ' ' + name_index + ' ' + 'message:' + message + '\n'))
        f1.close()
        s3.send(pickle.dumps([name + message]))
    except:
        print('Connection Failed')
    return ()


def get_device(serv_name):
    for i in device_list:
        device_list.pop()
    for i in raw_device_list:
        raw_device_list.pop()
    s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
     s4.connect(('baidu.com', 80))
     raw_ip_ip = s4.getsockname()
    except:
        raw_ip_ip = socket.gethostbyname(socket.gethostname())
    s4.close()
    raw_ip = raw_ip_ip[0]
    ip_list = raw_ip.split('.')
    ip_1 = int(ip_list[0])
    ip_2 = int(ip_list[1])
    ip_3 = int(ip_list[2])
    for i in range(2, 255):
        s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s4.settimeout(float(0.1))
        ip = ('%d.%d.%d.%d') % (ip_1, ip_2, ip_3, i)
        conn_stat = s4.connect_ex((ip, 8885))
        if conn_stat == 0:
            NameRequest = 'Namerequest'
            s4.send(pickle.dumps('\n'+NameRequest+' '+'from'+' '+serv_name+' '+'ip:'+' '+raw_ip))
            raw_device_list.append(ip)
            print(ip + ' ' + 'Successful')
        else:
            print(ip + ' ' + 'Pass')
    for each_device in raw_device_list:
        s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s5.settimeout(5)
        s5.connect((each_device, 8886))
        s5.send(bytes('','utf8'))
        #try:
        raw_name = s5.recv(1024)
        name = str(pickle.loads(raw_name))
        #except socket.timeout:
        print('Receive name time out:'+' '+str(s5.gettimeout())+'(sec)'+' '+'of device ip'+' '+each_device+' '+'setting ip as name.')
         #   name = each_device
        if name == serv_name:
         device_list.append(each_device + ' ' + str(name)+' '+'(Yourself)')
        else:
            device_list.append(each_device+' '+str(name)+'')
        s5.close()
    print('Get device complete.')
    return (device_list)


def show_device(device_list):
    if not device_list == []:
        pass
    else:
        print('Please get device first!')
        return ()
    device_num = 0
    for each in device_list:
        device_num += 1
        print_raw = each.split(' ')
        print(str(device_num) + ')' + ' ' + 'ip:' + ' ' + str(print_raw[0]) + ' ' + 'name:' + ' ' + str(print_raw[1]))

self_ip = '127.0.0.1'
serv_ip = ''
stop_name = th.Event()
msg_port = 8885
name_port = 8886
msg_sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name_sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    msg_sk.bind((serv_ip, msg_port))
    name_sk.bind((serv_ip, name_port))
except:
    print('Server error, please check network port usage :8885 :8886')
    exit(1)
msg_sk.listen(10)
name_sk.listen(10)
serv_name = input('Input your name for chat:')
t1 = th.Thread(target=partial(msg_serv))
t1.setName('msg')
t1.setDaemon(True)
t1.start()
t2 = th.Thread(target=name_serv, args=(name_sk, stop_name, serv_name))
t2.setName('name')
t2.setDaemon(True)
t2.start()
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if s1.connect_ex((self_ip, msg_port)) == 0:
    print("Message server successfully Started, ready to receive message.")
    s1.close()
else:
    print('''Can NOT start server, you will NOT able to get message.''')
    msg_serv_started = False
    s1.connect((self_ip, msg_port))
if s2.connect_ex((self_ip, name_port)) == 0:
    print('Name server successfully started, ready to resopnse name.')
else:
    print('''Can NOT start server, you will NOT able to set name.''')
    name_serv_started = False
    s2.connect((self_ip, name_port))
time.sleep(1)
s1.close()
s2.close()
def main():
 while True:
    slect = input('s=send message, r=refresh device, d=show device list, e=exit:')
    if slect == 's':
        send_msg(device_list, msg_port, serv_name)
    elif slect == 'r':
        get_device(serv_name)
    elif slect == 'e':
        msg_sk.close()
        name_sk.close()
        exit()
    elif slect == 'd':
        show_device(device_list)
    else:
        pass
main()