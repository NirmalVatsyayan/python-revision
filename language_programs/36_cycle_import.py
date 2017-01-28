import 36_cycle_import

class Demo(object):
    def __init__(self):
        self.name = "linga"
        self.__title = "reddy"

    def __func(self):
        print("ok")

    def __eq__(self, other):
        print("Inside lt")


obj = Demo()
obj1 = Demo()

print(obj < obj1)
print(obj > obj1)


