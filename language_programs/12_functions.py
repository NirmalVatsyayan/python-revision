#def add(x, y):
#    return x + y

#print(add(1, 3))
#print(add("I am ","OK !!"))


#function annotations
def add_more(val1: int, val2: int) -> str:
    return val1 + val2

print(add_more(10, 20))
print(add_more("I am "," Awesome !!"))

'''
#https://github.com/ceronman/typeannotations
@typechecked
def add_again(val1: int, val2: int) -> str:
    return val1 + val2

print(add_again(100, 200))
print(add_again("I am "," Awesome !!"))
'''