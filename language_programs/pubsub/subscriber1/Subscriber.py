from config import Config
from subscriber_socket import SubscriberSocket

cfg = Config()


class Subscriber(object):

    def __init__(self,channel):
        self.ip = cfg.get_ip()

        if channel == 'foo':
            self.port = cfg.get_channel_1_port()
        else:
            self.port = cfg.get_channel_1_port()

        self.sock = SubscriberSocket(self.ip,self.port)
        self.sock.establish_connection()
    
    def receive(self):
        self.sock.receive()    

    def close(self):
        self.sock.close()
