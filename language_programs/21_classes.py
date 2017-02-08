'''
classes , objects
polymorphism
inheritance

overloading (not possible)
over riding
*args, **kwargs

abstraction
'''


'''
Only for python 2.x,
in python 3.x new style class
is implicit with old style formats
'''

#old style class
class Test:
    pass

#new style class
class Pest(object):
    pass

x = Test()
y = Pest()


print(type(x))  # it will print type instance
print(type(y))  # it will print class




class SomeName(object):
    pass


class Human(object):
    
    @staticmethod
    def study(*a, **my_dict):
        print(a)
        print(my_dict)
        print("OK Studying !!")

    def talk(self,say="Nothing"):
        print("Human is saying -> ", say)
     
    def complain(self, what):
        print("Human is complaining about -> ", what)

    def act(self):
        print("Human is acting !!")

class Linga(Human):

    def teleport(self):
        print("Linga teleported to mars!!")

    def act(self):
        print("Rajnikant!!")

#nirmal = Human()
#nirmal.talk()

#linga = Linga()
#linga.talk("Something")
#Linga.study()
#linga.act()

#nirmal.act()

#Human.study(1,2,3,name="nirmal",type="Human")
#Human.study("a","b","c","d","e",country="USA", president="Barack obama", "ok")

#Human.study(1,"ok","cool")
#linga = Human()
#linga.talk(1)
#linga.talk("awesome !!")


nirmal = Human()
srikar = Human()

print(hasattr(nirmal, "age"))
setattr(nirmal, 'age', 10)
print(hasattr(nirmal, "age"))
print(nirmal.age)
delattr(nirmal, "age")
print(hasattr(nirmal, "age"))
