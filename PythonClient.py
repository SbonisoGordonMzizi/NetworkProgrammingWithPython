#!/usr/bin/env python3
"""
  Python base client server
  can recieve and process any object

"""

import socket
import pickle

HEADERSIZE = 10

clientSocketObject = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocketObject.connect((socket.gethostname(),8080))
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
    
    