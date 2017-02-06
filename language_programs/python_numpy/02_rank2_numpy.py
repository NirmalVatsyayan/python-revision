import numpy as np

a = np.array([1,2,3,4]) # RIGHT
#accessing elements
print(a[0], a[1], a[2])   # Prints "1 2 3 4" // IMP no comma bw elements
a[0] = 5                 # Change an element of the array
print(a)                  # Prints "[5, 2, 3 4]"
#a[5] = 10                # will give index out of bound error
#print(a)

b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
print(b)
print(b.shape)                     # Prints "(2, 3)" (row, column)
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"
