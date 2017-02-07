import numpy as np

if False:
    '''
    This is the same as applying min(max(x, minval), maxval) 
    to each element x in an array.
    '''
    a = np.array([6, 2, 5, -1, 0], float)
    print(a.clip(0,2))    

if False:
    '''
    Unique elements in numpy array
    '''    
    a = np.array([1, 1, 4, 5, 5, 5, 7], float)
    print(np.unique(a))

if True:
	'''
    Extract diagonal of 2-d array
	'''
	a = np.array([[1, 2], [3, 4]], float)
	print(a.diagonal())
