import os
import configparser

class Singleton(type):
    '''declared and defined meta class'''
    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]

class Config(metaclass=Singleton):

    def __init__(self):
        config = configparser.RawConfigParser()
        config.readfp(open(r'singleton.txt'))
        self.__name = config.get('Configuration', 'NAME')
        self.__code = config.get('Configuration', 'CODE')

        self.__student_count = config.get('Student', 'NUMBERS')

    def get_name(self):
        return self.__name

    def get_code(self):
        return self.__code

    def get_student_numbers(self):
        return self.__student_count
