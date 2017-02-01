from config import Config
from channel_socket import ChannelSocket, ChannelSubscriberSocket

cfg = Config()

class Channel(object):

    def __init__(self):
        self.ip = cfg.get_ip()
        self.port = float(cfg.get_port())
        self.port = int(self.port)
        self.subscriber_server_port = float(cfg.get_subscriber_server_port())
        self.subscriber_server_port = int(self.subscriber_server_port)

    def start_publisher_handler(self):
        self.sock = ChannelSocket(self.ip,int(self.port))
        self.sock.start_channel_server()
   
    def start_subscriber_handler(self):
        self.subscriber_sock = ChannelSubscriberSocket(self.ip,int(self.subscriber_server_port))
        self.subscriber_sock.start_channel_subscriber_server()
