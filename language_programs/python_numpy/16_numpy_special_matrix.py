import numpy as np

if False:
    #creating identity matrix
    a = np.identity(4, dtype=float)
    print(a)


if False:
	#creating eye matrix
	#eye function creates matrices with ones along k-th diagonal
    print("Ones at 1-st diagonal")
    a = np.eye(4, k=1, dtype=float)
    print(a)

    print("Ones at 2-nd diagonal")
    b = np.eye(4, k=2, dtype=float)
    print(b)

    print("Ones at negative 1-st diagonal")
    b = np.eye(4, k=-1, dtype=float)
    print(b)


if True:
    #sort a numpy array
    a = np.array([6, 2, 5, -1, 0], float)
    print(sorted(a)) #returns a list
    a.sort()
    print(a)

