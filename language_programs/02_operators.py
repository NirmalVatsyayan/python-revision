'''
Arithmetic

    Addition  +
    Substraction  - 
    Multiplication  *
    Devision  / 
    Floor devision //
    Modulus  %
    Exponential  **



#trying on int

data1 = 100
data2 = 2

print(data1 + data2)
print(data1 - data2)
print(data1 * data2)
print(data1 / data2)
print(data1 // data2)
print(data1 % data2)
print(data1 ** data2)
'''


'''
#trying on string

data1 = "nirmal"
data2 = "vatsyayan"

print("length of string is ",len(data1))
print("value at 0th index of data1 ",data1[0])
print("string contatenation using + ",data1 + data2)
print("printing strig separated by comma ",data1, data2)
'''

'''
#trying on boolean
data1 = True
data2 = True

print(data1 + data2)
print(data1 - data2)
print(data1 * data2)
print(data1 / data2)  # will give error is data2 = False
print(data1 // data2) # will give error is data2 = False
print(data1 % data2) # will give error is data2 = False
print(data1 ** data2)
'''
'''
#Comparison operators
#< <= > >= == != 


print(2 > 3)
print(2 >= 3)

print(2 < 3)
print(2 <= 3)

print(2 == 3)
print(2 != 3)
'''
'''

name = "nirmal"
title = "vatsyayan"

print(id(name), "   ",id(title))

print(name>title)
print(name>=title)
'''
#string are immutable
#now address of title is similar to name
#title = "nirmal"
#print(id(name), "   ",id(title))

#print(name > title)
#print(name >= title)

#value1 = 1
#value2 = "ok"

'''
'''
#this will not work
#print(value1>value2)

'''
#expression conjunction operators
#and or not
'''

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)
