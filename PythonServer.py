#!/usr/bin/env python3
"""
 Python base Server
 This Server is a sigle Threaded and it can backlog the maximum of 200 client request
 Transmit any Object
"""

import socket
import pickle #module used to convert objects to bytes

HEADERSIZE = 10 #

serverSockerObject = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSockerObject.bind(("192.168.1.205",8080))
serverSockerObject.listen(200) #listen and queue up  five request connection 

#main loop of the web server
print(f"*** server is running ***")
while True:
    (clientsocket,address) = serverSockerObject.accept()
    print(f"Connection from {address} has been established!")

    
    userObject = {"fname": "Sboniso","sname":"Gordon","lname":"Mzizi"}
    userObjectInBytes = pickle.dumps(userObject)
    #adding fix string size to the payload allowing the client to determine the transmitted data size
    userObjectTransmit = bytes(f'{len(userObjectInBytes):<{HEADERSIZE}}',"utf-8")+userObjectInBytes

    clientsocket.send(userObjectTransmit)

    