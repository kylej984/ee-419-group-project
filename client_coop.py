# Title: Server Script
# Authors:
#   Cooper Wharton: Entire server.py file; final draft of the client.py file, including functionalities and testing. Demo video.
#   Kyle Jeng: Initial draft of the client.py file. Includes the input, message_handling, and init.
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


# Client object
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
        # 1st message to server is always your own uname
        s.send(self.username.encode())

    # Sends user messages formatted with their username
    # concatenated to the server.
    def input_handling(self):
        while True:
            message = self.username + ": " + input()
            # black magic for making the formatting look nice
            print('\033[1A' + '\033[K', end='')
            # Sendthe message
            self.serverSocket.send(message.encode())

    # Prints messages received from other users (sent via
    # the server)
    def message_handling(self):
        while True:
            message = self.serverSocket.recv(1024).decode()
            print(message)


client1 = Client()


# Ideally these threads should live in the client object but storing them there causes errors
threading.Thread(target=client1.input_handling).start()
threading.Thread(target=client1.message_handling).start()
