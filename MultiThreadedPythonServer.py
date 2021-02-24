#!/usr/bin/env python3
"""
 Python base MultiThreadedServer
 This Server is a Multi Threaded and it can communicate with any number of clients
 Transmit any Object
"""

import socket
import pickle #module used to convert objects to bytes
from threading import Thread
import time

HEADERSIZE = 10 
SERVER_IPADD = socket.gethostname()
PORT = 8081

def sendMessageToClient(clientRequestObject,message):
    messageWithMessageLength = f"{len(message):<10}"+message
    clientRequestObject.send(bytes(messageWithMessageLength,"utf-8"))
    

def requestHandler(clientRequestObject,ipAdderss):
    print(f"client connected {ipAdderss}")
    message = "\nWELCOME TO FILE SERVER"
    sendMessageToClient(clientRequestObject,message)
    while True:
        message = clientRequestObject.recv(8192)
        clientMessage = message.decode("utf-8")
        
        try:
            if clientMessage[HEADERSIZE:] == "list":
                list_message = "....listing all files in a server...."
                sendMessageToClient(clientRequestObject,list_message)
                
            elif clientMessage[HEADERSIZE:] == "get":
                get_message = "...downloading file from server..."
                sendMessageToClient(clientRequestObject,get_message)
            
            elif clientMessage[HEADERSIZE:] == "exit":
                clientRequestObject.close()
                break
       
            else:
                message = "...Command Unknown..."
                sendMessageToClient(clientRequestObject,message)
        except  BrokenPipeError:
            pass 
   
        
def main():
    print("[SERVER STATING ...]")
    serverSockerObject = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSockerObject.bind((socket.gethostname(),PORT))
    serverSockerObject.listen(1000) 
    print(f"[SERVER LISTENING ON ({SERVER_IPADD}:{PORT})]")
    count = 0
    while True:
        clientRequestObject,ipAdderss = serverSockerObject.accept()
        print("clientObject Created")
        clientthread = Thread(target=requestHandler,args=(clientRequestObject,ipAdderss))
        clientthread.start()
        print("Name : ",clientthread.getName())
    

if __name__ == '__main__':

    main()
