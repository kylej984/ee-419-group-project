# Comment including group member names and their contributions at the start 
# of Client.py.
# Kyle Jeng: 
# Cooper Wharton: 

from threading import *
from socket import *

# To run a sub-process for a function called "my_func" the following syntax is used
# my_func_thread = Thread(target = my_func, args = ()) # arguments are passed in separately
# my_func_thread.start() # Start a subprocess for the function

# Example
# example_thread = Thread(target = test_rectangle.area_print, args = ())
# example_thread.start()

# my_socket = socket(AF_INET, SOCK_STREAM) # Socket of type IPv4 & TCP

# # Bind socket to an address
# IP = "127.0.0.1" # Loopback IP in this example
# port = 50001
# addr = (IP, port) # Tuple of IP and port number
# my_socket.bind(addr) # Bind an identifier tuple to a socket

# # Put a TCP socket on listening mode
# num_connections = 10
# my_socket.listen(num_connections) # num_connections specifies the number of unaccepted 
# # connections that the system will allow before refusing new connections

class Client:

    # creates a client socket with the user entering server IP or 
    # hostname and port. After the socket is created, a connection to the server 
    # should be established. Once a connection is established between the client 
    # and server, ask the user to enter a username and send it to the server.
    def __init__(self):
        # Connect
        IP = input("Input your server IP: ")
        PORT = input("Input your port: ")
        ADDR = (IP, PORT)
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind(ADDR)
        # Input
        self.USERNAME = input("Input your username: ")
        # Send to server // How do I do that?

    
    # Sends user messages formatted with their username 
    # concatenated to the server.
    def input_handling(self):
        MESSAGE = input("Input your message: ")
        MESSAGE = self.USERNAME + ": " + MESSAGE
        return MESSAGE

    # Prints messages received from other users (sent via 
    # the server)
    def message_handling(self,message):
        print(message)
    