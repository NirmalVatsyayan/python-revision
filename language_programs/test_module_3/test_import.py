
class Demo(object):
    def __init__(self):
        self.name = "linga"
        self.__title = "reddy"

    def __func(self):
        print("ok")

    def __gt__(self, other):
        return True
