from channel import Channel
from threading import Thread

if __name__ == '__main__':
    channel = Channel()

    publisher_handler_thread = Thread(target = channel.start_publisher_handler, args = [])
    subscriber_handler_thread = Thread(target = channel.start_subscriber_handler, args = [])

    publisher_handler_thread.start()
    subscriber_handler_thread.start()

    publisher_handler_thread.join()
    subscriber_handler_thread.join()
    

    
    
