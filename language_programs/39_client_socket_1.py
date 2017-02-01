import socket               
import time

s = socket.socket()         
host = socket.gethostname() 
port = 12348            
s.connect((host, port))

while True:
    print(s.recv(1024).decode("utf-8"))
    time.sleep(1)
    data = [1,2,3]
    #data = (1,2,"dhondhu")

    #data = {1:'a',2:'b',3:'c'}
    #data = 1
    #inp = str(data)
    s.send(bytes(str(data),'UTF-8'))
s.close()                  