import random
import string
import time
import threading
from socket import *

class Server:
    def __init__(self):
        # clients[client] = (socket, addr, username)
        self.clients = []
        serverIP = '127.0.0.1'
        serverPort = int(input('Server port: '))
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((serverIP, serverPort))
        s.listen(5)
        self.serverSocket = s
        print('Server is listening on port ', serverPort)
        self.start_server()

    def start_server(self):
        while True:
            s, addr = self.serverSocket.accept()
            print('Accepted connection from ', addr)
            username = s.recv(1024).decode()
            self.clients.append((s, addr, username))
            new_thread = threading.Thread(target=self.client_handling, args=(s, addr))
            new_thread.start()
            # thread not stored anywhere

    def broadcast(self, user_message):
        for client in self.clients:
            client[0].send(user_message)

    def client_handling(self, client_socket, client_address):
        while True:
            data = client_socket.recv(1024)
            self.broadcast(data)

server1 = Server()