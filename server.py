# Title: Server Script
# Authors:
#   Cooper Wharton
#   Kyle Jeng
# Institution:
#   University of Washington Seattle
#   Spring 2024
#   EE 419
#   Prof. Mahmood Hameed
# Version: 1.0
#   Stable, Working
# Date: 06.02.2024

import random
import string
import time
import threading
from socket import *


# Server object
class Server:
    def __init__(self):
        # clients contains tuples with client info as such:
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
            # Continuously accept connections
            s, addr = self.serverSocket.accept()
            # Notify when connection is made
            print('Accepted connection from ', addr)
            # first communication is always username per spec.
            username = s.recv(1024).decode()
            self.clients.append((s, addr, username))
            # create a new anonymous thread for this client
            # shut down of client connection is out of the scope of this project
            new_thread = threading.Thread(target=self.client_handling, args=(s, addr))
            new_thread.start()
            # thread not stored anywhere

    def broadcast(self, user_message):
        for client in self.clients:
            # 1st in client tuple is socket of that connection
            client[0].send(user_message)

    def client_handling(self, client_socket, client_address):
        while True:
            data = client_socket.recv(1024)
            self.broadcast(data)


server1 = Server()
