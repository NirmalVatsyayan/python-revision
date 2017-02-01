from sys import platform


print(platform)

if platform == 'linux':
    print("import linux libraries")
elif platform == 'win32':
    print("import windows libraries")
