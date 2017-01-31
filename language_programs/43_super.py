'''
question asked by linga
'''

class Student(object):
    c = "1111"

    def __init__(self):
        self.name = "linga"
        self.roll_number = "1"


class Programmer(Student):
    '''this is a programmer class'''

    def __init__(self):
        self.language = "python"
        super(Programmer, self).__init__()

    def print_data(self):
        '''this is a print data function'''
        print(self.name)
        print(self.roll_number)
        print(self.language)
        print(self.c)


obj = Programmer()
obj.print_data()

print(__doc__)   # call module doc
print(obj.__doc__)  # call class doc
print(obj.print_data.__doc__) # call function doc
