#!/usr/bin/env python3
"""
   This is a UDP base python server
"""
import socket
import time

PORT = 10001
IP_ADDRESS = "192.168.1.205"
BUFFER_SIZE = 64000


def server():

    serverSocketObject = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    serverSocketObject.bind((IP_ADDRESS,10001))

    print("Listening ay {}".format(socket.gethostname()))

    while True:
        clientData , address = serverSocketObject.recvfrom(BUFFER_SIZE)
        print(clientData.decode("utf-8"),address)

        time.sleep(2) #simulate the responces delay

        serverSocketObject.sendto(f"Hello UDP Client {IP_ADDRESS} ".encode("utf-8"),address)


if __name__ == "__main__":
     server()