import threading
import datetime
import time

from random import randint

count = 100
global_list = []
global_tup = (1,2,3,4)
global_dict = {}

'''
 GIL ->  Global interpreter lock
 Assigning an object value to a global variable is an atomic operation in Python. 
 Other threads cannot read a variable incorrectly by reading it while it's being 
 assigned. The GIL guarantees this in the C implementation of Python, 
 but other implementations can and do make that same guarantee in different ways.
'''


def print_function(args, mutex_obj):
    '''
    glbal primitive types will work fine even without mutex
    '''
    '''
    global count
    print(threading.current_thread().name, "count is  ",count)
    count = count + 1
    print(threading.current_thread().name, "new count is ",count)
    '''
    
    # you need not to use global key word to access list, tup or dict
    #print(global_list)
    print(global_tup+global_tup)
    #print(global_dict)

    print(threading.current_thread().name, "list is  ",global_list)
    global_list.append(threading.current_thread().name)
    print(threading.current_thread().name, "list is  ",global_list)


    #mutex_obj.lock()
    #time.sleep(args)
    #print(args," inside print function at time ",datetime.datetime.now()\
    #    , " name -> ",threading.current_thread().name)
    #mutex_obj.release()

if __name__ == '__main__':
    mutex_obj = threading.Lock()

    thread_holder = []
    print("starting program at ",datetime.datetime.now())
    for value in range(0,10):
        thread_obj = threading.Thread(target=print_function, args=(randint(0,5),mutex_obj))
        thread_holder.append(thread_obj)

        #using below code will make our program sequential
        #thread_obj.start()
        #thread_obj.join()
        
        # using below code will make our program unable to use shared variable from mail
        #thread_obj.start()
    
    # best way to use, start all thread and join them together
    [thread_obj.start() for thread_obj in thread_holder]
    [thread_obj.join() for thread_obj in thread_holder]
    print("exiting main thread")
