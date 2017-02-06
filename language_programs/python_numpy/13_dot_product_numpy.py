import numpy as np

a = np.array([1, 2])
b = np.array([2, 1])

print(a*b)
print(np.sum(a*b))

print((a*b).sum())

print(np.dot(a, b))
#dot function is also instance method
print(a.dot(b))
print(b.dot(a))



