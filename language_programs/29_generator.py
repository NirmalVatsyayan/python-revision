import sys

#function
def data_func(limit):
    data = [x for x in range(0,limit)] 
    return data

#generator
def data_gen(limit):
    for data in range(0, limit):
        yield data



x = data_gen(int(sys.argv[1]))
print(type(x))

for data in x:
    print(data)

