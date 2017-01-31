from config import Config
from publisher_socket import PublisherSocket

cfg = Config()


class Publisher(object):

    def __init__(self,channel):
        self.ip = cfg.get_ip()

        if channel == 'foo':
            self.port = cfg.get_channel_1_port()
        else:
            self.port = cfg.get_channel_1_port()

        self.sock = PublisherSocket(self.ip,self.port)
        self.sock.establish_connection()
    
    def send(self,data):
        self.sock.send(data)    

    def close(self):
        self.sock.close()