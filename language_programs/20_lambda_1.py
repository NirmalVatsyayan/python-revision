'''
lambda functions - anonymous functions

additional functions - filter() , map() , reduce() (pending)

*args,**kwargs (pwnding with example)

generators , iterators

config file read

file handling


'''

def f(x) : 
	return x+2

g = lambda x:x+2

print(f(10))
print(f(12))

print(g(10))
print(g(12))


temp_list = [2, 18, 9, 22, 17, 24, 8, 12, 27]
g = filter(lambda x: x % 3 == 0, temp_list)
h = filter(lambda x: x % 3 == 0, temp_list)
print(list(g))
print(tuple(h))

i = map(lambda x: x * 2 + 10, temp_list)
print(list(i))

j = map(lambda x: (float(9)/5)*x + 32, temp_list)
print(list(j))


g = lambda x: True if x % 2 == 0 else False
print(g(1))
print(g(2))