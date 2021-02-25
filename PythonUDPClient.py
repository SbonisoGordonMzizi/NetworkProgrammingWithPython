#!/usr/bin/env python3
"""
   This is a UDP base python client
"""

import socket

SERVER_PORT = 10001
SERVER_IPADD = "192.168.1.205"
BUFFER_SIZE = 64000

def client():
    serverSocketObject = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    serverSocketObject.connect((SERVER_IPADD,SERVER_PORT))

    print("UDP Client")
    delay = 0.5
    receivedData = ''
    while True:
        message = "Hello UDP Server"
        serverSocketObject.send(message.encode("utf-8"))
        print("waiting up to {} seconds for a replay".format(delay))
        serverSocketObject.settimeout(delay)

        try:
            receivedData = serverSocketObject.recv(BUFFER_SIZE)
        except socket.timeout:
            delay *= 2
            if delay > 4:
                raise RuntimeError("I Think the Server is down")
        else:
            break


    print(receivedData.decode("utf-8"))

if __name__ == "__main__":
    client()