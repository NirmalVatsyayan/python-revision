
'''
closure

when you use inner function
lifetime of arguments of outer function
is available to inner function even when control
is outside the scope of outer fuction
'''

def lotus(func):

    def inner():
        print("I got decorated")
        func()

    return inner

def flower():
    print("I am flower")


herb = lotus(flower)
herb()



'''
x = new_func()

def outer():
    print("i am in outer")

    def inner():
        print("i am in inner")
    
    def a_inner():
        print("i am in a inner")

    return inner, a_inner

x, y = outer()

x()
y()

'''
