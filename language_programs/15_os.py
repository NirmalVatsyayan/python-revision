import os

'''have a lot of modules for unix non compatible to windows'''


#windows
'''name of os dependent module imported'''
print(os.name)


'''environment'''
print(os.environ)

'''current directory path'''
print(os.getcwd())

path = os.getcwd()

'''change path'''
os.chdir(path)

print(os.getlogin())

print(os.getppid())


