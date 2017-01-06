#list comprehensions

data_list = [x for x in range(0,10)]
print(data_list)

#filters all odd numbers
data_list = [x for x in range(0,10) if x%2]
print(data_list)

#filters all even numbers
data_list = [x for x in range(0,10) if not x%2]
print(data_list)


#tuple generator
data_tup = (x for x in range(0,10))
print(tuple(data_tup))


#set comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

#dict comprehensions
dict_data = {key: key**2 for key in range(5)}
print(dict_data)
