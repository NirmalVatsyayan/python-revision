import numpy as np

'''
create an array and specify required data type
for implicit type conversion
'''
arr = np.array([[1,2,3,4],[0,0,0,0]], dtype=complex)
print(arr)


'''
create an array using np range
'''

a = np.arange(10, dtype=float)
print(a)


'''
create an array using python range
'''
a = np.array(range(10), dtype=float)
print(a)


#create an array of particular size with
#all elements having 0 value
zero_arr = np.zeros((3,4))
print(zero_arr)


#create an array of a size and
#fill it with 1s
one_arr = np.ones((3,4), dtype=np.int16)
print(one_arr)

#create an uninitialized array of size
#its output contains garbage/ may vary
empty_arr = np.empty((2,2))
print(empty_arr)


#array of random numbers | value always between 0, 1
#numbers are from probability distribution
x = np.random.random(10)
print(x)

x = np.random.random((3,3))


#array of random numbers | values greater than 1 also numbers 
#are from gaussian distribution with mean 0 and variance 1 (pretty close)
x = np.random.randn(10)
print(x)

x = np.random.randn(10, 10)
print(x)

print(x)