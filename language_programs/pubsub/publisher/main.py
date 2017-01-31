from publisher import Publisher

if __name__ == '__main__':
    pub = Publisher(channel='foo')
    for i in range(1000):
        pub.send("sending %s "%i)
    pub.close()