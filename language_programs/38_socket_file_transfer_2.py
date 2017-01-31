
import socket                   

port = 60000                    
s = socket.socket()             
host = socket.gethostname()     
s.bind((host, port))            
s.listen(5)                     

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024).decode('UTF-8')
    print('Server received', repr(data))

    filename='file.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send(bytes('Thank you for connecting','UTF-8'))
    conn.close()
