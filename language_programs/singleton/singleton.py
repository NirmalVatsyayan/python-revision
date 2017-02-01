import os
import configparser

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=Singleton):

    def __init__(self):
        config = configparser.RawConfigParser()
        config.readfp(open(r'singleton.txt'))
        self.name = config.get('Configuration', 'NAME')
        self.code = config.get('Configuration', 'CODE')
