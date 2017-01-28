
tup1 = ('physics', 'chemistry', 1997, 2000)


print(tup1)
print(type(tup1))

print(tup1[0])
print(tup1[-1])
print(tup1[3])

print(tup1[0:len(tup1)])
print(tup1[:3])
print(tup1[2:])


print(">>>>>>>>>>>>>>>>")
data_list = list(tup1)
print(data_list)
print(type(data_list))

data_list.append(11111)
data_list.append(22222)
print(data_list)


print(">>>>>>>>>>>>>>>")

print(id(tup1))
print(id(data_list))

print(tup1)

tup2 = (1, 2, 3, 4, 5, 6, 7 )

#print("tup1[0]: ", tup1[0])
#print("tup2[1:5]: ", tup2[1:5])

print(tup1 + tup2)
print(tup1*4)

#data = list(tup1)
#print(type(data), "   ",data)



tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print(tup1)
print(id(tup1))

tup1 = tup1 + tup2
print(id(tup1))
print(tup1)