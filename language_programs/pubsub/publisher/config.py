import configparser


class Config(object):

    def __init__(self):

        configParser = configparser.RawConfigParser()   
        configFilePath = 'config.txt'
        configParser.read(configFilePath)

        self.publisher_ip = configParser.get('publisher', 'ip')
        self.publisher_channel_1_port = configParser.get('publisher', 'channel1_port')

    def get_ip(self):
        return self.publisher_ip

    def get_channel_1_port(self):
        return int(self.publisher_channel_1_port)