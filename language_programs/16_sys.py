'''sys library important functions'''
import sys

#version
print("python version is ",sys.version)
print("detail info ",sys.version_info)

#to access command line arguments
print("command line arguments ",sys.argv)

#know your os
print("operating system you are using is ", sys.platform)

#to exit process 
print("exiting")
sys.exit(0)

print("after exit")