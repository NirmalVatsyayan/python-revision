from copy import deepcopy, copy

'''
Deep copy is related to nested structures, if you have list of lists, 
then deepcopy copies the nested lists also, so it is recursive copy. With just copy, 
you have a new outer list but inner lists are references.

Assignment does not copy, it simply sets the reference to the old data. 
So you need copy to create a new list with same contents.
'''
'''
list1 = [1,2,3]
print(id(list1))
y = copy(list1)
z = list1.copy()
print(id(y))
y.append(100)
print(y)
print(list1)
'''

list1 = [1,2,3, [100,200]]

list2 = deepcopy(list1)
print(id(list1))
print(id(list2))

list2.append("linga")

print(list2)
print(list1)

list2[3].append("linga reddy")

print(list2)
print(list1)

#data_dict = {'OK':1}
#data_dict_1 = data_dict.copy()

print(dir(list))
