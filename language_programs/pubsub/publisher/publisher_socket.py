import socket
import time

class PublisherSocket(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.socket = None

    def establish_connection(self):
        self.socket = socket.socket()         
        host = self.ip 
        port = self.port                
        self.socket.connect(('0.0.0.0', port))

    def send(self,data):
        self.socket.send(bytes(data,'UTF-8'))
        time.sleep(1)


    def close(self):
        self.socket.close()