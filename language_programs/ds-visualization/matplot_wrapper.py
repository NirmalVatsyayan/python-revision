import matplotlib, matplotlib.pyplot
import numpy
import types

def show_plot(arg1, arg2=None):

    def real_decorator(f):
        def wrapper(*args, **kwargs):
            matplotlib.pyplot.figure(figsize=(arg1, arg2))
            result = f(*args, **kwargs)
            matplotlib.pyplot.show()
            return result
        return wrapper

    if type(arg1) == types.FunctionType:
        f = arg1
        arg1, arg2 = 10, 5
        return real_decorator(f)
    return real_decorator