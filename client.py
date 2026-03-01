import socket

HOST = '127.0.0.1' #local
PORT = 5001 # check for match in server



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # for TCP, UDP uses SOCK_DGRAM

s.connect((HOST, PORT))

print(f'Client connected to server host {HOST}, port {PORT}')

while True:
    message = input(f'Send message to server: ')
    s.sendall(message.encode('utf-8'))
    if message == 'exit':
        break
    
    response = s.recv(1024).decode('utf-8')
    print(f'Response from server: {response}')
    
s.close()
print('Client closed')

