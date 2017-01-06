'''
Error - cannot be handled (eg syntax errors)

Exception - error detected during runtime , can be handled
eg ImportError, IndexError, KeyError, KeyboardInterrupt, MemoryError
https://docs.python.org/3.5/library/exceptions.html

'''

num = 1
denominator = 0

try:
    data = num/denominator
except ZeroDivisionError as e:
    print("ZeroDivisionError came !! please handle !!")
except IOError as e:
    print("IOError came !!")
except Exception as e:
    print("Any other exception came !!")

print("I have a logic to run !!")

class MyError(Exception):
    
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
 
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))

try:
    raise(MyError(3*2))
    # Value of Exception is stored in error
except MyError as error:
    print('A New Exception occured: ',error.value)
