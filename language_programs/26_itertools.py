from itertools import count
from itertools import islice
from itertools import cycle
from itertools import repeat
from itertools import accumulate
from itertools import permutations
from itertools import combinations
from itertools import tee
from itertools import islice

def demo_count():
    '''
    count(start=0, step=1)

    The count iterator will return evenly spaced values 
    starting with the number you pass in as its start parameter. 
    '''
    for i in count(10):
        if i > 20: 
            break
        else:
            print(i)


def demo_isslice():
    '''
    we loop over count starting at 10 and ending after 5 items.
    '''
    for i in islice(count(10), 5):
        print(i)


def demo_cycle():
    '''
    The cycle iterator from itertools allows you to create an 
    iterator that will cycle through a series of values infinitely
    '''
    count = 0
    for item in cycle('XYZ'):
        if count > 7:
            break
        print(item)
        count += 1

def demo_repeat():
    '''
    The repeat iterators will return an object an 
    object over and over again forever unless you set its times argument
    '''

    iterator = repeat(5, 5)
    while 1:
        try:
            print(next(iterator))
        except:
            break

def demo_accumulate():
    '''
    The accumulate iterator will return accumulated
    sums or the accumulated results of a two argument 
    function that you can pass to accumulate
    
    Here we import accumulate and pass it a range of 10 numbers, 
    0-9. It adds each of them in turn, so the first is 0, 
    the second is 0+1, the 3rd is 1+2, etc.
    '''
    print(list(accumulate(range(10))))


def demo_permutations():
    '''
    The permutations sub-module of itertools will return successive r 
    length permutations of elements from the iterable you give it. 
    '''
    for item in permutations('WXYZ', 2):
        print(''.join(item))


def demo_combinations():
    '''
    If you have the need to create combinations, 
    Python has you covered with itertools.combinations
    '''
    print(list(combinations('WXYZ', 2)))

    for item in combinations('WXYZ', 2):
        print(''.join(item))


def demo_tee():
    '''
    The tee tool will create *n* iterators from a single iterable. 
    '''
    data = 'ABCDE'
    iter1, iter2 = tee(data)
    for item in iter1:
        print(item)

    for item in iter2:
        print(item)


def demo_isslice():
    '''
    '''
    iterator = islice('123456', 4)
    while True:
        try:
            print(next(iterator))
        except:
            break
