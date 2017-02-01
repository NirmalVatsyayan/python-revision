import socket
import time

class SubscriberSocket(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.socket = None

    def establish_connection(self):
        self.socket = socket.socket()         
        host = self.ip 
        port = self.port                
        self.socket.connect(('0.0.0.0', port))

    def receive(self):
        i = 0
        while 1:
            self.socket.send(bytes(str(i),'UTF-8'))
            data = self.socket.recv(1024).decode("utf-8")
            if 'no more' in data:
                print("all publisher data received , sleeping for 10 seconds")
                time.sleep(10)
            else:
                i += 1
                print("received data from publisher    -    ",data)
                time.sleep(1)

    def close(self):
        self.socket.close()
