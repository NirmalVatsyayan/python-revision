def lotus(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@lotus
def flower():
    print("I am flower")


flower()
