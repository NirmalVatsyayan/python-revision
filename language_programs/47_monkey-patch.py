
# show simple class and function

class Name(object):

    def retName(self,name):
        print("Inside retName method of class Name")
        print("Argument passed is ",name)
        return 'Nirmal'


name = Name()
val = name.retName('What\'s your name??')
print(val)


# show class variable and instance variable
class Employee(object):
    #class variable
    empCount = 0

    def __init__(self, name, salary):
        #instance variable
        self.name = name
        self.salary = salary
        print("Inside constructor with name ",name," salary ",salary)
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
        print("Total Employee %d" % self.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)

emp1 = Employee("Dhondhu", 2000)


emp1.displayCount()
emp1.displayEmployee()

print(" >>>>>>>>>>>>>>>>>>>>>>>>  ")
print(" >>>>>>>>>>>>>>>>>>>>>>>>  ")

emp2 = Employee("Just chill", 5000)
emp2.displayCount()
emp2.displayEmployee()
#print("Total Employee %d" % Employee.empCount)


# monkey patching object on fly
print(hasattr(emp1, 'age'))
setattr(emp1, 'nirmal', 'owner')
print(getattr(emp1, 'nirmal'))

print(dir(emp1))
delattr(emp1, 'nirmal')
#print(hasattr(emp1, 'nirmal'))
setattr(emp1, 'nirmal', 'owner')
#print(hasattr(emp1, 'nirmal'))
print(dir(emp1))
print(emp1.nirmal)
delattr(emp1, 'nirmal')
print(dir(emp1))

