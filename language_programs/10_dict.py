'''
1) More than one entry per key not allowed
   No duplicate key

2) Keys must be immutable. Which means you can use strings, 
   numbers, tuples and frozensets as dictionary keys.
'''
#hashing
#collision prevention techniques in hashing
#chaining
#buckets

#O(1) - retrieval

data = {'Name': 'Nirmal', 'Age': 26, 'Class': 'lowest'}
#print(data)
print(type(data))


print("dict['Name']: ", data['Name'])
print("dict['Age']: ", data['Age'])

#update value for existing key
data['Age'] = 8 # update existing entry
#print(data)

#add new key-value
data['School'] = "DPS School"
#print(data)

#delete a key
del data['Name']
#print(data)

#length of dictionary
print(len(data))

#convert dict to string
print('string', str(data))
val = str(data)
print(val, "    ",type(val))

#print(data)
#print all keys of dict
print(data.keys())

#print all values of dict
print(data.values())

#print key value in 1 go
print(data.items())

for key, value in data.items():
	print(key, " :  ", value)



key1 -> value
key2 -> value
key3 -> value
key4 -> value
key5 -> value

#fetch value from key
#print(data['School'])
print(data.get('School'))

#print(data['team'])
#print(data.get('team'))


#shallow copy of a dict
new_dict = data.copy()
#print(new_dict)

#clear all data from dict
print(data)
data.clear()
print(data)
