import socket      
import time         

s = socket.socket()         
host = socket.gethostname() 
port = 12348 
s.bind((host, port))        

s.listen(5)                 
while True:
   c, addr = s.accept()     
   print('Got connection from', addr)
   c.send(bytes('Thank you for connecting','UTF-8'))
   time.sleep(1)
   data = c.recv(1024).decode("utf-8")
   print(data, "  >>>> ",type(data))
   rec = eval(data)
   print(rec, "  >>> ",type(rec))
   
c.close()                