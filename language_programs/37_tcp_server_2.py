import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("",17642))
s.listen(5)
connect, address = s.accept()

while True:    
    resp = (connect.recv(1024)).strip().decode('UTF-8')
    print("received ",resp)
    connect.send(bytes("You said '" + resp + "' to me\n","UTF-8"))
    
connect.close()
print("\ndone",address)