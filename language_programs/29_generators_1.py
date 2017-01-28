'''
Iterables

When you create a list, 
you can read its items one by one. 
Reading its items one by one is called iteration:


Generators are iterators

but you can only iterate over them once. 
Its because they do not store all the values in memory, 
they generate the values on the fly

Yield is a keyword that is used like return, 
except the function will return a generator.
'''

def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter >= n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)
'''
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
'''
for x in f:
	# no linefeed is enforced by  end="":  
	#asked in class by nisar
    print(x, " ", end="") # 
print()



'''
def getelement():
	abc = [1,2,3,4]
	for val in abc:
		yield val

g = getelement()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''

'''
def cityGenerator():
	yield "delhi"
	yield "MUMBAI"
	yield "hyderabad"
	yield "indore"
	yield "gr noida"
	yield "gurgaon"
	yield "york"

g = cityGenerator()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''