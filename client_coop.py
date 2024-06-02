import random
import string
import time
import threading
from socket import *


class Client:

    def __init__(self):
        # Connect
        serverIP = '127.0.0.1'
        serverPort = int(input("Connection Port: "))
        addr = (serverIP, serverPort)
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(addr)
        self.serverSocket = s

        # Input
        self.username = input("Input your username: ")
        print()
        s.send(self.username.encode())

    # Sends user messages formatted with their username
    # concatenated to the server.
    def input_handling(self):
        while True:
            message = self.username + ": " + input()
            print('\033[1A' + '\033[K', end='')
            self.serverSocket.send(message.encode())

    # Prints messages received from other users (sent via
    # the server)
    def message_handling(self):
        while True:
            message = self.serverSocket.recv(1024).decode()
            print(message)


client1 = Client()


threading.Thread(target=client1.input_handling).start()
threading.Thread(target=client1.message_handling).start()
