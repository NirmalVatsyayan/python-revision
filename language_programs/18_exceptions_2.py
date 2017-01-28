class MyDummyException(Exception):
    def __init__(self, msg):
        self.msg = msg

try:
    raise(MyDummyException("first dummy exception!!"))
except MyDummyException as abc:
    print(abc.msg)


try:
    raise(MyDummyException("second dummy exception!!"))
except MyDummyException as abc:
    print(abc.msg)
