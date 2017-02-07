import numpy as np

a = np.array(range(10), dtype=float)
b = np.array([[1,2], [3,4], [5,6], [7,8]])

if False:
    '''
    1-D array iteration
    '''
    for x in a:
        print(x)


if False:
    '''
    2-D array iteration 
    '''
    for x in b:
        print(x)


if False:
    '''
    multiple assignment in 2-D array iteration
    '''
    print("Type 1")
    for a1,a2 in b:
        print(a1, " ", a2)
    
    print("Type 2")
    for (a1, a2) in b:
        print(a1, " " , a2)

if False:
    a = np.array(range(10), dtype=float)
    b = np.array([[0, 2], [3, -1], [3, 5]], float)

    #sum of values of array
    print(a.sum())
    print(b.sum(axis=0))  #1d 0 + 3 + 3,  2+-1+5
    print(b.sum(axis=1))  #2d 0+2, 3+-1 , 3+5

    #product of values of array
    print(a.prod())
    print(b.prod(axis=0))
    print(b.prod(axis=1))

    #mean of values of array
    print(a.mean())
    print(b.mean(axis=0))
    print(b.mean(axis=1))

    #variance of values of array
    print(a.var())
    print(b.var(axis=0))
    print(b.var(axis=1))

    #standard deviation of values of array
    print(a.std())
    print(b.std(axis=0))
    print(b.std(axis=1))

    #max value and its index in array
    print(a.max())
    print(a.argmax())

    print(b.max(axis=0))
    print(b.argmax(axis=0))

    print(b.max(axis=1))
    print(b.argmax(axis=1))

    #min value and its index in array
    print(a.min())
    print(a.argmin())

    print(b.min(axis=0))
    print(b.argmin(axis=0))

    print(b.min(axis=1))
    print(b.argmin(axis=1))

    '''

            p  p  p  p  p
            o  o  o  o  o
            s  s  s  s  s

     dim 2  0  1  2  3  4

            |  |  |  |  |
  dim 0     ↓  ↓  ↓  ↓  ↓
  ----> [[[ 0  1  2  3  4]   <---- dim 1, pos 0
  pos 0   [ 5  6  7  8  9]   <---- dim 1, pos 1
          [10 11 12 13 14]]  <---- dim 1, pos 2
  dim 0
  ---->  [[15 16 17 18 19]   <---- dim 1, pos 0
  pos 1   [20 21 22 23 24]   <---- dim 1, pos 1
          [25 26 27 28 29]]] <---- dim 1, pos 2
            ↑  ↑  ↑  ↑  ↑
            |  |  |  |  |

     dim 2  p  p  p  p  p
            o  o  o  o  o
            s  s  s  s  s

            0  1  2  3  4

    '''


    x = [[[ 0 ,  1,  2,  3,  4],
          [ 5,  6,  7,  8,  9],
          [10, 11, 12, 13, 14]],

          [[15, 16, 17, 18, 19],
          [20, 21, 22, 23, 24],
          [25, 26, 27, 28, 29]]]


    a = np.array(x)

    print(a.sum(axis=0))
    print(a.sum(axis=1))
    print(a.sum(axis=2))


if True:
    a = np.array([1, 2, 3], float)
    b = np.array([0, 1, 1], float)
    print(np.dot(a,b))

    a = np.array([[0, 1], [2, 3]], float)
    b = np.array([2, 3], float)
    c = np.array([[1, 1], [4, 0]], float)

    print(np.dot(a, c))