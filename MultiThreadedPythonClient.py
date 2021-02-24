#!/usr/bin/env python3
"""
  Python base client server
  can communicate back and forth with a server while listing and downloading object

"""

import socket
import pickle

HEADERSIZE = 10
PORT=8081

def sendMessageToServer(clientSocketObject ,clientQuery):
    message = clientQuery.lower()
    messageWithMessageLength = f"{len(message):<10}"+message
    clientSocketObject.send(bytes(messageWithMessageLength,"utf-8"))


def userInput(clientSocketObject):
    while True:
        clientQuery = input(">>  ")
        if clientQuery.lower() == "exit":
            sendMessageToServer(clientSocketObject ,clientQuery)
            return 0
            break

        elif clientQuery.lower() == "list":          
            sendMessageToServer(clientSocketObject ,clientQuery)
            message = clientSocketObject.recv(8192)
            print(message.decode("utf-8"))

        elif clientQuery.lower() == "get":
            sendMessageToServer(clientSocketObject ,clientQuery)
            message = clientSocketObject.recv(8192)
            print(message.decode("utf-8"))

        else:
            print(
                """
                Enter exit     : to exit the application
                Enter list     : to list files
                Enter get      : to download file
                """)
             
def clientMain():
    clientSocketObject = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientSocketObject.connect((socket.gethostname(),PORT))
    while True:
        full_message = ''
        new_massage = True
        while True:
            message = clientSocketObject.recv(8192)
            if new_massage:
                transmittedDatalength = int(message[:10])
                new_massage = False

            full_message += message.decode("utf-8")    
        
            if len(full_message) - HEADERSIZE == transmittedDatalength:
                print(full_message[10:])
                full_message = ''
                new_massage = True
                hold = userInput(clientSocketObject)
                if hold == 0:
                    break
        clientSocketObject.close()
        break
    
if __name__ == '__main__':

    clientMain()

       
    
    
    