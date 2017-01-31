import socket, select
BUFFER = []

class ChannelSocket(object):
      
    CONNECTION_LIST = []    # list of socket clients
    RECV_BUFFER = 4096      # Advisable to keep it as an exponent of 2
    
    
    def __init__(self,ip,port):

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('0.0.0.0', port))
        self.server_socket.listen(10)
 
        # Add server socket to the list of readable connections
        self.CONNECTION_LIST.append(self.server_socket)
        print(self.CONNECTION_LIST)
    
    def start_channel_server(self):
 
        while 1:
            # list of sockets ready for select
            read_sockets,write_sockets,error_sockets = select.select(self.CONNECTION_LIST,[],[])
     
            for sock in read_sockets:
                 
                #Handling new connection
                if sock == self.server_socket:
                    # Handle the case in which there is a new connection recieved through server_socket
                    sockfd, addr = self.server_socket.accept()
                    self.CONNECTION_LIST.append(sockfd)
                    print("Client (%s, %s) connected" % addr)
                     
                #handling message from client
                else:
                    
                    try:
                        
                        data = sock.recv(self.RECV_BUFFER).decode("utf-8")
                        #print("received data publisher  ->",data)
                        # echo back the client message
                        if data:
                            BUFFER.append(data)
                            #sock.send(bytes('','UTF-8'))
                     
                    # client disconnected, so remove from socket list
                    except:
                        print("Client (%s, %s) is offline" % addr)
                        sock.close()
                        self.CONNECTION_LIST.remove(sock)
                        #print("buffer is ",BUFFER)
                        continue
             
        server_socket.close()


class ChannelSubscriberSocket(object):
      
    CONNECTION_LIST = []    # list of socket clients
    RECV_BUFFER = 4096      # Advisable to keep it as an exponent of 2
    
    
    def __init__(self,ip,port):

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('0.0.0.0', port))
        self.server_socket.listen(10)
 
        # Add server socket to the list of readable connections
        self.CONNECTION_LIST.append(self.server_socket)
        print(self.CONNECTION_LIST)
    
    def start_channel_subscriber_server(self):
 
        while 1:
            # Get the list sockets which are ready to be read through select
            read_sockets,write_sockets,error_sockets = select.select(self.CONNECTION_LIST,[],[])
     
            for sock in read_sockets:
                 
                #New connection
                if sock == self.server_socket:
                    # Handle the case in which there is a new connection recieved through server_socket
                    sockfd, addr = self.server_socket.accept()
                    self.CONNECTION_LIST.append(sockfd)
                    print("Client (%s, %s) connected" % addr)
                     
                #Some incoming message from a client
                else:
                    # Data recieved from client
                    try:
                        
                        data = sock.recv(self.RECV_BUFFER).decode("utf-8")
                        #print("data received from subscriber ->",data)
                        # echo back the client message
                        if data:
                            data = int(data)
                            try:
                                return_data = "publisher sent "+BUFFER[data]
                            except:
                                # all publisher data read by receiver, intimate to wait 
                                # but dont break connection as last index will be lost
                                return_data = "no more publisher messages pending, wait !!"
                            
                            sock.send(bytes(return_data,'UTF-8'))

                     
                    # client disconnected, so remove from socket list
                    except:
                        #broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                        print("Client (%s, %s) is offline" % addr)
                        sock.close()
                        self.CONNECTION_LIST.remove(sock)
                        continue
             
        server_socket.close()
