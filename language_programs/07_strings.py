
var1 = 'Hello World!'

#reverse a string
#string[::-1]
#string[start:stop:step]

print("var1[0]: ", var1[0])
print("var1[1:5]: ", var1[1:5])

#capitalize - first alphabet to upper
print(var1.capitalize())

#length of string
print(len(var1))

#check end of string
suffix = "d!";
print(var1.endswith(suffix))

#find string in another string
search = "ll"
print(var1.find(search))

#check if string is alphanumeric
print(var1.isalnum())

#check if string consists only alphabets
print(var1.isalpha())

#check if string consists only digits
data = '1111'
print(data.isdigit())

print(data.isnumeric())

#all alphabets in lower
data = "bc"
print(data.islower())


#convert to lower & upper
data = "OK"
print(data.lower())

data = 'ok'
print(data.upper())

#strip string
val = '  abc'
print(val)
print(val.lstrip())
print(val.rstrip())
print(val.strip())

#split string
val = 'abc,abc,abc,abc'
print(val.split(','))

#max and min value in string
val = "thisisastring"
print(max(val))
print(min(val))

paragraph = '''this is a long string
a paragraph example
long string'''
print(paragraph)
