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

from collections import Counter
from collections import defaultdict
from collections import namedtuple
from collections import deque

def show_counter():
    counter = Counter()
    for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
        counter[word] += 1

    print(counter)

    print(counter.most_common(2))

    c = Counter({'red': 4, 'blue': 2})
    print(sorted(c.elements()))

    print(c.most_common(1))


def show_defaultDict():
    ice_cream = defaultdict(lambda:"vanilla")

    ice_cream['Linga'] = 'Reddy'
    ice_cream['Nirmal'] = 'Vatsyayan'

    print(ice_cream['Linga'])
    print(ice_cream['Nirmal'])
    print(ice_cream['Srikar'])


def show_namedTuple():
    Company = namedtuple('Company', 'name location website')
    mp = Company(name='blah', location='delhi', website='blah.com')

    mp1 = Company('blah1', 'new delhi', 'blah1.com')

    print(mp.name, "  ", mp.location, " ", mp.website)
    print(mp1.name, "  ", mp1.location, " ", mp1.website)


def show_deque():
    d = deque()
    d.append('a')
    d.append('b')
    d.append('c')
    print(d)

    print(d.popleft())
    print(d)
    d.appendleft('nirmal')
    print(d)


