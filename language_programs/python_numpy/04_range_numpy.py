import numpy as np

#To create sequences of numbers, NumPy provides a function 
#analogous to range that returns arrays instead of lists

#will print every number from 0, 10
range1 = np.arange(0,10)
print(range1)

#will print numbers at interval of 2
#upper limit is exclusive as python range,
#here 10 will never be printed
range2 = np.arange(0,10,2)
print(range2)

# it will print 9 numbers from 0 to 2
range3 = np.linspace( 0, 2, 9 )
print(range3)
