# SIMPLE
# Plots square root function from 0 to 100
import math
from matplot_wrapper import *

@show_plot
def simple():
    x_data = numpy.linspace(0., 100., 1000)

    for x in x_data:
        y = math.sqrt(x)
        matplotlib.pyplot.scatter(x, y)

    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('x')
    axes.set_ylabel('y')

simple()