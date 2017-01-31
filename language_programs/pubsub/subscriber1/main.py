from Subscriber import Subscriber

if __name__ == '__main__':
    sub = Subscriber(channel='foo')
    #for i in range(1000):
    while 1:
        sub.receive()
