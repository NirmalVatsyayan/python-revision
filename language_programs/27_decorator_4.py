
def authentication(func):

    def wrapper():
        print("BEFORE inside decorate of before_func!!!")
        func()
        print("AFTER calling func")
    
    return wrapper

@authentication
def func():
    print("inside func !!!")

if __name__ == '__main__':
    func()
