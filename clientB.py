#!/usr/bin/env python3

import threading
import datetime
import time
import socket
import random

ADDRESS = '127.0.0.1'
PORT = 60000
BUFSIZE = 4096

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((ADDRESS, PORT))

def clientMain():
    data = 0
    while True:
        time.sleep(2)
        data = random.randint(0,100)
        server.send(str(data).encode("UTF-8"))
        now = datetime.datetime.now()
        print('[clientB]Send:{0} [{1}]'.format(data, now))

def thread_start():
    t = threading.Thread(target = clientMain,args=())
    t.setDaemon(True)
    t.start()

