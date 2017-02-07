import numpy as np

a = np.array([3, 3, 1], float)
b = np.array([0, 3, 2], float)

if False:
    '''
    comparing 2 numpy arrays
    '''
    print(a>b)
    print(a>=b)

    print(a<b)
    print(a<=b)

    print(a==b)
    print(a!=b)

if False:
    '''
    comparing numpy array with scalar
    '''
    print(a>2)

if False:
    '''
    The any and all operators can be used 
    to determine whether or not any or all 
    elements of a Boolean array are true:
    '''
    print(any(a))
    print(all(a))


if False:
    '''
    logical operation in numpy
    '''
    a = np.array([1, 3, 0], float)
    print(a>0)
    print(a<3)

    print(np.logical_and(a > 0, a < 3))

    print(np.logical_not(a))
    print(np.logical_or(a>0, a<3))


if False:
    '''
    The where function forms a new array from two 
    arrays of equivalent size using a Boolean filter 
    to choose between elements of the two. 
    Its basic syntax is where(boolarray, truearray, falsearray):
    '''
    a = np.array([1, 3, 0], float)
    print(np.where(a != 0, 1 / a, a))

