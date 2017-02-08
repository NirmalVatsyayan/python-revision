val = "{}, {}".format("reddy", "linga")

x = "python"
y = "language"

a = "i am a student of "+x +" "+y #string concatenation

b = "i am a student of %s %s" % (x, y)  #string formatting

c = "i am a student of {} {}".format(x, y)

d = "i am a student of {1} {0}".format(x, y)

names = "{0}, {1} and {2}".format('John', 'Bill', 'Sean')
m='{1},{2} and {0}'.format('c','d','a')


def StringContainer():
    # define a class
    class String:
        def __init__(self):
            self.content_string = ""

        def len(self):
            return len(self.content_string)

    # return the class definition
    return String

# create the class definition
container_class = StringContainer()
#container_class is alias of String class

# create an instance of the class
wrapped_string = container_class()
print(type(wrapped_string))


len_str = wrapped_string.len()
print(len_str)

wrapped_string.content_string = 'emu emissary'

len_str = wrapped_string.len()
print(len_str)
