import threading
import datetime
import time
import psycopg2

from random import randint


def print_function(args, incr, mutex_obj):
    data_id = None
    old_price = None
    
    mutex_obj.acquire()
    print(threading.current_thread().name ,"  ordered for increasing price by  ",incr)
    conn = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='postgres'")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM Cars where id=1")

    rows = cur.fetchall()
    for data in rows:
        print(threading.current_thread().name, "  >>>>   ",data)
        data_id = data[0]
        old_price = data[2]
    
    print(threading.current_thread().name, " sleeping for ",args)
    time.sleep(0)
    print(threading.current_thread().name, " updating ")
    new_price = old_price + incr
    data = (new_price, data_id)
    cur.execute("UPDATE Cars SET price=%s where id=%s",data)
    conn.commit()

    conn.close()
    mutex_obj.release()

if __name__ == '__main__':
    mutex_obj = threading.Lock()

    thread_holder = []
    print("starting program at ",datetime.datetime.now())
    for value in range(0,2):
        thread_obj = threading.Thread(target=print_function, args=(randint(3,10),randint(100,200),mutex_obj))
        thread_holder.append(thread_obj)

    [thread_obj.start() for thread_obj in thread_holder]
    [thread_obj.join() for thread_obj in thread_holder]
    print("exiting main thread")
