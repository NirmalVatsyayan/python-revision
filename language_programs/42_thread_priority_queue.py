
'''
Multithreaded Priority Queue
The Queue module allows you to create a new queue object that can hold a 
specific number of items. There are following methods to control the Queue −

get(): The get() removes and returns an item from the queue.

put(): The put adds item to a queue.

qsize() : The qsize() returns the number of items that are currently in the queue.

empty(): The empty( ) returns True if queue is empty; otherwise, False.

full(): the full() returns True if queue is full; otherwise, False.

'''
#!/usr/bin/python
 
import queue
import threading
import time
 
exitFlag = 0
 
class StartThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print("Starting " + self.name)
        process_data(self.name, self.q)
        print("Exiting " + self.name)
 
def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)
 
threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
    thread = StartThread (threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1
 
# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()
 
# Wait for queue to empty
while not workQueue.empty():
    pass
 
# Notify threads it's time to exit
exitFlag = 1
 
# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")