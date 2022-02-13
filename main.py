#!/usr/bin/env python3

import time
import threading
import sys
import server
import clientA
import clientB

def server_thread():
    server.thread_start()

def client_thread():
    clientA.thread_start()
    clientB.thread_start()

if __name__ == '__main__':
    try:
        s = threading.Thread(target = server_thread,args=())
        s.setDaemon(True)
        s.start()
        time.sleep(2)
        c = threading.Thread(target = client_thread,args=())
        c.setDaemon(True)
        c.start()
        while True:
            c = sys.stdin.read(1)
            if c == 'q':
                sys.exit()
    except KeyboardInterrupt:
        server.server.close()
        clientA.server.close()
        clientB.server.close()
        print('[main]Socket close.')
        sys.exit(1)

