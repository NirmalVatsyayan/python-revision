from multiprocessing import Process, Queue, Lock, Manager
import multiprocessing
import time


man = Manager()
print(dir(man))
lock_obj = man.Lock()
list_obj = man.list()

def hello_world(lock_obj, list_obj):
    for i in range(0,2):
        print("inside process ",multiprocessing.current_process().name)
        list_obj.append(i)
        print(list(list_obj))
        time.sleep(5)
        print("quitting process")
    

for data in range(0,3):
    process_obj = Process(target=hello_world,args=(lock_obj,list_obj))
    process_obj.start()
    process_obj.join()
