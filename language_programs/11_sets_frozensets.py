#basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
#print(type(basket))

#print(basket)

#print(len(basket))



data = set()
#print(data)
data.add(1)
data.add(2)
data.add(3)
data.add(1)
data.add("this is a set")

#print(data)


#copy a set
data_backup = data.copy()
#print(data_backup)

#clear a set
data.clear()
#print(data)


#a = {x for x in 'abracadabra' if x not in 'abc'}
#a = {x for x in 'abracadabra'}
#print(a)

#discard fetches the element from set
#if element is not present it will not 
#give any error
#a.discard('r')
#a.discard('z')
#a.discard('y')
#print(a)


#pop fetches the first element
#a = set()
#a.add(1)
#print(a.pop())
#print(a.pop())
#print(a.pop())
#print(a.pop())
#print(a.pop())

#print(a)
#print(len(a))
#print(a.pop())
#print(a.pop())   # it will give error as no data is present in set


#remove removes the element from set
#if not present it will raise key error
a = set()
a.add(1)
a.add(2)
#print(a)

a.remove(1)
#print(a)
#a.remove(3) # error


#difference between sets
x = {"a","b","c","d","e"}
y = {"b","c"}

z = {"c","d"}

#print(">>>>   ",x.difference(y))
#print(">>>>   ",y.difference(x))
#print(">>>>>   ",x.difference(y).difference(z))


#we could also use - operator to see difference
#set does not support + and * operation
#print(x - y)
#print(x - y - z)


#find common elements from sets
#x = {"a","b","c","d","e"}
#y = {"c","d","e","f","g"}
#print(x.intersection(y))


#find if a set is subset of another set
#x = {"a","b","c","d","e"}
#y = {"c","d"}
#print(x.issubset(y))

#superset
#print(x.issuperset(y))


#frozen sets cannot be changed
cities = frozenset(["Frankfurt", "Basel","Freiburg"])
print(cities)
print(len(cities))
#cities.pop() # error here

#mutables are - set & list
#immutables - frozenset & tuples & string & integers
