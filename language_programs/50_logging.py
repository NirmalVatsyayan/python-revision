import profile
import logging
import time

def do_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    # create a file handler
    handler = logging.FileHandler('hello.log')
    handler.setLevel(logging.INFO)

    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)

    logger.info('Hello baby')

def call_logging():
    do_logging()

profile.run('call_logging()')