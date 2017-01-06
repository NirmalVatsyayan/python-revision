'''for loops'''
name = "srikar"
array = [1, 2, 3, 4, 5]

'''
for data in array:
    print(data)

for data in name:
    print(data)

#nested for-loop
for data in name:
    for value in array:
        print(data,"  ->  ",value)
'''

''' while loops '''
'''
age = 100

while age > 90:
    print("Your age is ",age)
    age = age - 1

'''
import time

counter = 0
while True:
    if counter == 5:
        counter = counter + 1
        continue
    if counter > 7:
        break

    print("value of counter is ",counter)
    counter = counter + 1