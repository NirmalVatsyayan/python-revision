class Student(object):
    #class variable
    session = "2017-18"

    def __init__(self, a, b, c):
        #instance variables
        self.name = a
        self.age = b
        self.roll_no = c
        self.__something = 100+c

    def use_private(self):
        print("here i am")
        print(self.__something)

stu = Student("linga", 20, 100)
print(stu.name)
print(stu.age)
print(stu.roll_no)
print(stu.session)


stu.use_private()

print(Student.session)
