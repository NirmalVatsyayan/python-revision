'''
from test_module import test
from test_module_2 import testing

#test.print_name("nirmal")

print(testing.add(100, 200))
print(testing.subs(100, 200))
print(testing.multiply(100, 200))
print(testing.divide(100, 200))
'''

from demo_module import arithmetic_op

summation = arithmetic_op.add(100, 200)
print(summation)
