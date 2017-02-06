import numpy as np

'''
Broadcasting is a powerful mechanism that allows numpy to work 
with arrays of different shapes when performing arithmetic operations. 
Frequently we have a smaller array and a larger array, 
and we want to use the smaller array multiple times to perform some 
operation on the larger array.
'''

if False:
    data = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
    v = np.array([1, 0, 1])

    y = np.empty_like(data)   # Create an empty matrix with the same shape as x

    # Add the vector v to each row of the matrix x with an explicit loop
    for i in range(4):
        y[i, :] = data[i, :] + v

    # Now y is the following
    # [[ 2  2  4]
    #  [ 5  5  7]
    #  [ 8  8 10]	
    #  [11 11 13]]
    print(y)

if False:
    data = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
    v = np.array([1, 0, 1])
    vv = np.tile(v, (4, 1))  # Stack 4 copies of v on top of each other
    print(vv)                # Prints "[[1 0 1]
                             #          [1 0 1]
                             #          [1 0 1]
                             #          [1 0 1]]"
    y = data + vv  # Add x and vv elementwise
    print(y)    # Prints "[[ 2  2  4
                #          [ 5  5  7]
                #          [ 8  8 10]
                #          [11 11 13]]"


if False:
    data = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
    v = np.array([1,0,1])
    print(v+data)

if False:
    x = np.array([1,2,3])
    y = np.array([7,8])
    
    print(x.shape)
    print(np.reshape(x, (3,1))*y)
