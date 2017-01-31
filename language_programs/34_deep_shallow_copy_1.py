from copy import deepcopy, copy

'''
Deep copy is related to nested structures, if you have list of lists, 
then deepcopy copies the nested lists also, so it is recursive copy. With just copy, 
you have a new outer list but inner lists are references.

Assignment does not copy, it simply sets the reference to the old data. 
So you need copy to create a new list with same contents.
'''

list1 = [1,2,3]
print(id(list1))

list2 = deepcopy(list1)
print(id(list2))


list3 = list1
print(id(list3))

list4 = copy(list1)
print(id(list4))


list5 = list1[:]

data_dict = {'OK':1}
data_dict_1 = data_dict.copy()