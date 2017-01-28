'''operator overloading error example, file doc'''

class Student(object):
    '''this is an awesome student class'''
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def message(self):
        '''this is comment for message function'''
        print(self.name, " is awesome !!")

    def __le__(self, other):
        if self.roll_number <= other.roll_number:
            return True
        else:
            return False
    
    def __lt__(self, other):
        if self.roll_number < other.roll_number:
            return True
        else:
            return False

    def __gt__(self, other):
        return True

    def __ge__(self, other):
        return True

    def __ne__(self, other):
        return True

    def __eq__(self, other):
        return True

linga = Student("linga", 1)

joshua = Student("Joshua", 2)

print(linga <= joshua)
print(linga < joshua)
print(linga > joshua)
print(linga >= joshua)
print(linga == joshua)
print(linga != joshua)

#BIF
#print(dir())

#prints file name
#print(__file__)


#print __main__
#print(__name__)

#prints module level docs
#print(__doc__)

#print(__builtins__)
#print(__loader__)
#print(__spec__)
#print(__package__)

