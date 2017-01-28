'''
instance/object methods
static method

'''


class Base(object):

    def __init__(self, moustache):
         self.moustache = "awesome"

    @classmethod    
    def func(cls):
        print("in base: " + cls.__name__)
        print("in base: " , cls.i)
        

    @staticmethod
    def demo():
        print("this is a static method")

class Child(Base):
    i = 10

    def __init__(self, moustache):
        self.name = "linga"
        super(Child, self).__init__(moustache)

    @classmethod
    def show(cls):
        print("in child class ",cls.i)
        print("in child: " + cls.__name__)

    def ok(self):
        print("moustache -> ", self.moustache)
        print(">>>>>>>>>>>>  ",self.i)


#static
Base.demo()
b = Base("awesome")
b.demo()


#instance methods
c = Child("awesome")
c.ok()
c.show()
c.func()
print("question of sai -> ",c.i)
#class methods
