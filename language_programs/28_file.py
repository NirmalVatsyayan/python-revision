'''
file_ptr = open("/home/demo/demo.txt")
read
write
append

#r - read mode
#a - append mode
#w - write mode
#r+ - reading and writing




import csv - csv writer
'''

'''
#read
file_ptr = open("demo.txt", "r")

#for data in file_ptr.readlines():
#    print(data)

data = file_ptr.read()
print(data)
print(data.split("\n"))

file_ptr.close()
'''


#write
file_ptr = open("demo.txt", "w")
file_ptr.write("this is new content\n")
file_ptr.write("this is another new line")
file_ptr.close()



#append
file_ptr = open("demo.txt", "a")
file_ptr.write("this is append new content\n")
file_ptr.write("this is another append new line")
file_ptr.close()


file_ptr = open("demo.txt", "r+")
file_ptr.write("this r+ content\n")
file_ptr.write("this r+ new line")
file_ptr.close()
