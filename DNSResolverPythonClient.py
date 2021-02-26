#!/usr/bin/env python3
"""
  Python base client server
  can recieve and process any object

"""

import socket
import pickle
import sys

HEADERSIZE = 10
def client(hostname_or_ip, port):
    
    try:
        infolist = socket.getaddrinfo(
        hostname_or_ip, port, 0, socket.SOCK_STREAM, 0,
        socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME,
        )
    except socket.gaierror as e:
        print('Name service failure : ',e)
        sys.exit(1)
    info = infolist[0] # per standard recommendation, try the first one
    socket_args = info[0:3]
    address = info[4]
    clientSocketObject = socket.socket(*socket_args)
    try:
        clientSocketObject.connect(address)
    except socket.error as e:
        print("Network failure : ",e)
    else:    
        while True:
            full_message = b''
            new_message = True
            while True:
                message = clientSocketObject.recv(16)
                if new_message:
                    #getting the size of the transmitted data
                    message_length = int(message[:HEADERSIZE])
                    new_message = False
        
                full_message += message

                if len(full_message) - HEADERSIZE == message_length:
                    print(pickle.loads(full_message[10:]))
                    new_message = True
                    full_message = b''
    
if __name__ == '__main__':
    client("local.tech.com",8080)