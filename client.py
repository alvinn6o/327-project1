import socket
import os
import sys

# Use SERVER_HOST env var in Docker (set to "server"), else localhost for local testing
HOST = os.environ.get('SERVER_HOST', '127.0.0.1')
PORT = 5001

# connect client socket to same port as server with TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# vertify client connection
print(f'Client connected to server host {HOST}, port {PORT}')

# In Docker (no TTY), run auto mode; otherwise interactive mode for local use
if sys.stdin.isatty():
    # this is for input prompt which was used during local runs
    while True:
        message = input('Send message to server: ')
        s.sendall(message.encode('utf-8'))
        if message == 'exit':
            break
        response = s.recv(1024).decode('utf-8')
        print(f'Response from server: {response}')
else:
    # this is used for docker run which sends the following messages to show its connected and can communicate with server
    messages = ["Hello from client!", "Docker is cool!", "exit"]
    for msg in messages:
        s.sendall(msg.encode('utf-8'))
        if msg != "exit":
            response = s.recv(1024).decode('utf-8')
            print(f'Response: {response}')

s.close()
print('Client closed')

