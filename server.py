# server.py
import socket
import threading

# Set up the server
HOST = ''  # Listen on all network interfaces
PORT = 12345  # Port to listen on

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

# Broadcast function to send messages to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handle function to manage individual client connections
def handle(client):
    while True:
        try:
            # Receive message from client
            message = client.recv(1024)
            # Broadcast the message to all other clients
            broadcast(message)
        except:
            # Remove and close client if error occurs
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

# Receive function to accept new client connections
def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        # Request and store nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))

        # Start handling thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('Server is listening...')
receive()
