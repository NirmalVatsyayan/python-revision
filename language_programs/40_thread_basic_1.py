#!/usr/bin/python
import _thread
import time

'''
threading module is more powerful than this
'''


def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print("%s Eating: %s" % ( threadName, time.ctime(time.time()) ))

#try:
_thread.start_new_thread( print_time, ("Thread-1", 1, ) )
_thread.start_new_thread( print_time, ("Thread-2", 1, ) )
#except:
#   print("Error: unable to start thread")

while 1:
   pass