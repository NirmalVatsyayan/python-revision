'''
Find the sum of all the multiples of 3 or 5 below 1000.

1) find all multiples of 3
2) find all multiples of 5
3) find sum of them


Q1 - Is 1000 inclusive or exclusive

Q2 - Do we need to check divisibility with both numbers or 1

pseudo code:

divisible_by_3
divisible_by_5

Iterate through 0-1000:
    check if variable is divisible by 3:
        if yes:
        	add in divisible_by_3 list
        
    check if variable is divisible by 5:
        if yes:
        	add in divisible_by_5 list
        
initialize a sum variable
iterate though the both result list:
   add all values of list in sum variable

print sum
'''


data_list_3 = []
data_list_5 = []

result = 0

for data in range(1, 1001):
    if data % 3 == 0:
        data_list_3.append(data)
    
    if data % 5 == 0:
        data_list_5.append(data)


for x in data_list_3:
    result = result + x

for x in data_list_5:
    result = result + x

print(result)
