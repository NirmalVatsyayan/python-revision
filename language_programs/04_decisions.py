'''
if 

if - else

if - else if - else if - else | chained if-else

nested if-else
'''

'''if statements
data = 101
print("result of condition is : ",data < 100)

if data < 100:
    print("data is less than 100")
    print("print1")
    print("print2")
    print("print3")

print("outside indentation")

'''

'''
#if else statement
data = 99

if data > 100:
    print("data is greater than 100")
else:
    print("data is less than 100")
'''
#if-elif-else chain
'''
data = 31

if data > 0 and data < 10:
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


1 || enter a value from user
     get its difference from 100
     print its modulas with 100

2 || enter multiple values from command line
     calculate their sum
     print results based upon their sign (+, -)

3 || get your name and title from command line
     print difference between their length in words

     if the difference is 2:
        it should print, "congrats the difference is 2"


data = 51

if data > 10:
    print("data is > 10")
    if data > 20:
        print("data is >20")
        if data > 30:
            print("data is >30")
        else:
            print("data is less than 30")
    else:
        print("data is less than 20")
else:
    print("data is less than 10")




if data > 10:
    print("data is >10")
    if data > 20:
        print("data is >20")
        if data > 30:
            print("data is >30")
            if data > 40:
                print("data is >40")
            else:
                print("ok not greater than 40")
        else:
            print("not greater than 30")
    else:
        print("Not greater than 20")
else:
    print("we are inside else block")

