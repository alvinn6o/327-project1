# TCP server that listens for incoming messages

import socket
import threading


HOST = '0.0.0.0' # define to listen on all interfaces
PORT = 5001

# handle multiple clients
def handle_client(client_socket, client_addr):
    print(f'Connection from {client_addr}')

    # keep listening until client exits
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message or message == 'exit':
            client_socket.close()
            break

        print(f'Client {client_addr} message: {message}')
        client_socket.send(f'Received message: {message}'.encode('utf-8'))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # for TCP, UDP uses SOCK_DGRAM

s.bind((HOST, PORT)) # bind socket to port 5001

s.listen(5) # listens to multiple

print(f'TCP server host {HOST} and port {PORT}')

while True:
    # thread to
    client_socket, client_addr = s.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_addr))
    client_thread.start()



    



