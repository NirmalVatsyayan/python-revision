'''this is a module doc string'''

# welcome to python
#print("Hello world !!")

# this is sigle line comment

'''
this is multi line comment
second line of comment
tird line of comment
'''


#python variables are dynamic typed.
#a variable can hold value of any type


x = True
print("name is ", x, " of type ", type(x), " at location ", id(x))

name = 100
print("name is ",name, " of type ",type(name), " at location ",id(name))

name = "Nirmal"
print("name is ",name, " of type ",type(name), " at location ",id(name))

name = 4.0
print("name is ",name, " of type ",type(name), " at location ",id(name))

'''
2 types of methods are generally present:

1) accessor  -  it dont effect the original copy
2) mutator  - it makes changes in original data

every class in python have accessor methods but not all
have mutator ones, like string, tuple, int, float

when any class dont have mutator methods present, we call
them immutable
'''
name = "nirmal vatsyayan"
#accessor
print(name.upper())

sig = name.split()

#mutator
sig.reverse()
print(sig)
