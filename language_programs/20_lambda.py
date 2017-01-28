from functools import reduce

def f(x): 
    return x**2

g = lambda x: x**2
add = lambda x, y: x + y

#print(f(4))
#print(g(4))
#print(add(100,100))



data_list = [2, 18, 9, 22, 17, 24, 8, 12, 27]

#filter function filters from the data list
#print(list(filter(lambda x: x % 3 == 0, data_list)))

data = filter(lambda x: x % 3 == 0, data_list)
#print(type(data))
for x in data:
    pass
    #print(x)

#maps/project a value from another value
#print(list(map(lambda x: x * 2 + 10, data_list)))

#reduces an entire list to a value based upon expression
print(reduce(lambda x, y: x + y, data_list))

sum_value = 0
for data in data_list:
    sum_value = sum_value + data
print(sum_value)

