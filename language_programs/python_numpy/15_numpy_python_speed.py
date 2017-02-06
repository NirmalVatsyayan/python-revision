import numpy as np
import datetime

a = np.random.randn(100)
b = np.random.randn(100)

T = 100000

#using dot product using for loop
def python_dot_product(a, b):
    result = 0
    for e, f in zip(a,b):
        result += e*f

    return result

def invoke_python_dot(T, a, b):
    time1 = datetime.datetime.now()

    for t in range(T):
        python_dot_product(a, b)
    
    time2 = datetime.datetime.now()
    return (time2 - time1).total_seconds()

#using numpy dot function

def numpy_dot_product(a, b):
    return a.dot(b)

def invoke_numpy_dot(T, a, b):
    time1 = datetime.datetime.now()

    for t in range(T):
        numpy_dot_product(a, b)

    time2 = datetime.datetime.now()
    return (time2 - time1).total_seconds()

python_dot_time = invoke_python_dot(T, a, b)
numpy_dot_time = invoke_numpy_dot(T, a, b)
print("python loop dot product time -> ", python_dot_time)
print("numpy dot product time -> ", numpy_dot_time)
print("numpy is faster than python by magnitude -> ", python_dot_time/numpy_dot_time)
