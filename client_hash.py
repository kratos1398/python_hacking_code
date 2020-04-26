import socket
import os

connection = ("10.0.2.15", 9999)
clientSocket = socket.socket()
clientSocket.connect(connection)
try:
    while True:
        filename = input("Enter a file name: ")
        clientSocket.send(str.encode(filename))
        recieved = clientSocket.recv(2048)
        recieved = recieved.decode('utf-8')
        print("Server hashed the file: {}".format(recieved))
except KeyboardInterrupt:
    print("Exiting..")

    



