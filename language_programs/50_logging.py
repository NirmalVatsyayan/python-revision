'''logging test module'''
import profile
import cProfile
import logging


'''
info - 1 -- debug
warning -2 - debug
error - 3
critical - 4
'''

#logger -> handler (files) -> formatter (msg format)

def do_logging():
    '''doc'''
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

    logger.info('Hello there !!')

def call_logging():
    '''doc'''
    do_logging()



do_logging()
#cProfile.run('call_logging()')
