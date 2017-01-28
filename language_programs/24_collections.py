#container data types
'''
namedtuple()	factory function for creating tuple subclasses with named fields
deque	list-like container with fast appends and pops on either end
ChainMap	dict-like class for creating a single view of multiple mappings
Counter	dict subclass for counting hashable objects
OrderedDict	dict subclass that remembers the order entries were added
defaultdict	dict subclass that calls a factory function to supply missing values
UserDict	wrapper around dictionary objects for easier dict subclassing
UserList	wrapper around list objects for easier list subclassing
UserString	wrapper around string objects for easier string subclassing

'''

import collections

counter = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
     counter[word] += 1

print(counter)

c = collections.Counter({'red': 4, 'blue': 2})
print(sorted(c.elements()))

print(c.most_common(1))

