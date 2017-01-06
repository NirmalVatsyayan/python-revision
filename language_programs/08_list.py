data = [1, 2, True,"Nirmal Vatsyayan", 2.4, ["ok"]]
print(type(data))

for value in data:
	print(value,"  type is ",type(value))


data = []

#append a value in list
data.append(1)
print(data)

#extending a list by adding all value from another list
new_data = [1000,111,1]
data.extend(new_data)
print(data)


#insert in a list at given position
data.insert(0, 100)
print(data)

#remove 1st occurence of item from list with value similar to argument
data.remove(1)
print(data)

#returns min/max value from list

list1, list2 = ['xyz', 'lmn', 'abc'], [456, 700, 200]

print("Max value element : ", max(list1))
print("Max value element : ", max(list2))

print("Min value element : ", min(list1))
print("Min value element : ", min(list2))

#reverse a list
list1.reverse()
print(list1)

#sort a list
list2.sort()
print(list2)

#find index of element in list, if not present it will give error
#print(list2.index('a')) # error
print(list2.index(200))


#pop element from list
print(list2)

print(list2.pop()) # by default last element
print(list2.pop(1)) # index can also be passed
