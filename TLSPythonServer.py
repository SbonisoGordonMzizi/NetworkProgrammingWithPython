#!/usr/bin/env python3
"""
 Python base Server
 This Server is a sigle Threaded and it can backlog the maximum of 200 client request
 Transmit any Object and Support transit encryption

"""

import socket
import ssl
import pickle #module used to convert objects to bytes

HEADERSIZE = 10 #

def server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('/home/vice/server.crt', '/home/vice/server.key')

    serverSockerObject = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSockerObject.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSockerObject.bind(("192.168.1.205",443))
    serverSockerObject.listen(5) #listen and queue up  five request connection 

    #main loop of the web server
    print(f"*** server is running ***")
    while True:
        clientsocket,address = serverSockerObject.accept()
        print(f"Connection from {address} has been established!")
        ssl_sock = context.wrap_socket(clientsocket, server_side=True)
    
        userObject = {"fname": "Sboniso","sname":"Gordon","lname":"Mzizi"}
        userObjectInBytes = pickle.dumps(userObject)
        #adding fix string size to the payload allowing the client to determine the transmitted data size
        userObjectTransmit = bytes(f'{len(userObjectInBytes):<{HEADERSIZE}}',"utf-8")+userObjectInBytes

        ssl_sock.send(userObjectTransmit)
        ssl_sock.close()

if __name__ == "__main__":
    

    server()  