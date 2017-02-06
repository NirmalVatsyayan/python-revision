'''
tutorial followed
http://cs231n.github.io/python-numpy-tutorial/
'''

'''
In Numpy dimensions are called axes. The number of axes is rank.
 the coordinates of a point in 3D space [1, 2, 1] is an array of rank 1, 
 because it has one axis. That axis has a length of 3.
'''

import numpy as np

data_list = [1,2,3,4]

#array creation
a = np.array(data_list) # create rank1 array RIGHT
a = np.array([1,2,3,4]) # RIGHT
#a = np.array(1,2,3,4) # WRONG

print(type(a))            # Prints "<type 'numpy.ndarray'>"

#the dimensions of the array. This is a tuple of integers 
#indicating the size of the array in each dimension. 
#For a matrix with n rows and m columns, shape will be (n,m). 
#The length of the shape tuple is therefore the rank, or number of dimensions, ndim.
print(a.shape)            # Prints "(3,)" // IMP means 1-d array (row, column)

#the total number of elements of the array. 
#This is equal to the product of the elements of shape.
print(a.size)

#an object describing the type of the elements in the array. 
#One can create or specify dtype’s using standard Python types. 
#Additionally NumPy provides types of its own. numpy.int32, 
#numpy.int16, and numpy.float64 are some examples.
print(a.dtype)

#the size in bytes of each element of the array. 
#For example, an array of elements of type float64 has itemsize 8 (=64/8),
#while one of type complex32 has itemsize 4 (=32/8). 
#It is equivalent to ndarray.dtype.itemsize.
print(a.itemsize)

#the buffer containing the actual elements of the array. Normally, we won’t need to use 
#this attribute because we will access the elements in an array using indexing facilities.
print(a.data)     

#the number of axes (dimensions) of the array. 
#In the Python world, the number of dimensions is referred to as rank.
print(a.ndim)     
