import configparser


class Config(object):

    def __init__(self):

        configParser = configparser.RawConfigParser()   
        configFilePath = 'config.txt'
        configParser.read(configFilePath)

        self.subscriber_ip = configParser.get('subscriber', 'ip')
        self.subscriber_channel_1_port = configParser.get('subscriber', 'channel1_port')

    def get_ip(self):
        return self.subscriber_ip

    def get_channel_1_port(self):
        return int(self.subscriber_channel_1_port)
