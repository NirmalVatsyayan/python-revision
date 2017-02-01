import configparser


class Config(object):

    def __init__(self):

        configParser = configparser.RawConfigParser()   
        configFilePath = 'config.txt'
        configParser.read(configFilePath)

        self.ip = configParser.get('channel', 'ip')
        self.port = configParser.get('channel', 'port')
        self.subscriber_server_port = configParser.get('channel', 'subscriber_server_port')
        

    def get_ip(self):
        return self.ip

    def get_port(self):
        return int(self.port)
    
    def get_subscriber_server_port(self):
        return int(self.subscriber_server_port)
