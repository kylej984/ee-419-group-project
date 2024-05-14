import random
import string
import time
import threading
from socket import *

class Server:
    def __init__(self):
        # clients[client] = (socket, username)
        self.clients = []
        self.serverPort = input('Server port: ')
        s = socket(AF_INET, SOCK_STREAM)
        s.bind(('127.0.0.1', serverPort))
        s.listen(5)
        self.serverSocket = s
        print('Server is listening on port ', serverPort)

    def start_server(self):
        while True:
            s, addr = serverSocket.accept()
            print('Accepted connection from ', addr)
            username = connectionSocket.recv(1024).decode()
            self.clients.append((s, username))
            new_thread = threading.Thread(target=self.client_handling, args=(self, s, addr))
            new_thread.start()
            # thread not stored anyway

    def broadcast(self, user_message):
        for client in self.clients:
            client.send(user_message)

    def client_handling(self, client_socket, client_address):
        while True:
            data = client_socket.recv(1024)
            

