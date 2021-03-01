#!/usr/bin/env python3
"""
 Python base Client Server
 
 Support transit encryption
"""

import socket
import ssl
import pickle

def client():

    hostname = 'www.example.com'
    # PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations('/home/viceblack/python_server/pythonNetworking/chained.crt')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.connect(("192.168.1.229",443))
    ssock = context.wrap_socket(sock, server_hostname=hostname)

    data = ssock.recv(1024)
    if data:
        print(pickle.loads(data[10:]))

if __name__ == "__main__":
    client()