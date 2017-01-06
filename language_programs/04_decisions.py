'''if statements'''
'''
data = 10
print("result of condition is :",data<100)

if data < 100:
    print("data is less than 100")
    print("print1")
    print("print2")
    print("print3")

    print("outside indentation")


'''
'''
#if else statement
data = 101

if data > 100:
    print("data is greater than 100")
else:
    print("data is less than 100")

#if-elif-else chain
'''

'''
if data >0 and data < 10:
    print("data is between 0 & 9")
elif data >= 10 and data < 20:
    print("data is between 10 and 19")
elif data >= 20 and data < 30:
    print("data is between 20 and 29")
else:
    print("data is greater than 30")

'''

'''
if data < 5 or data > 100:
    print("we are here <5 OR >100")
elif data < 10 or data > 50:
    print("we are here <10 OR >50")
else:
    print("inside else block")

'''
#nested if-else

data = 49

if data > 10:
    print("data is >10")
    if data > 20:
        print("data is >20")
        if data > 30:
            print("data is >30")
            if data > 40:
                print("data is >40")
else:
    print("we are inside else block")








