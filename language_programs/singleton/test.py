from singleton import Config

c1 = Config()
print(id(c1))

c2 =Config()
print(id(c2))


print(c2.get_name())
print(c2.get_code())


print(c2.get_student_numbers())

'''
meta class - class of class

singleton - you could create object of any class,
only once in life time of a program
'''
