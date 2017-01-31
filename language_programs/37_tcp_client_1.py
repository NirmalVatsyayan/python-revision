import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname() 
port = 17642
s.connect((host,port))


while True:
    
    s.send(bytes("Hello dhondhu!!!!","UTF-8"))
    resp = s.recv(1024).decode('UTF-8')
    print(resp)
    time.sleep(1)
    
s.close()
print("\ndone")