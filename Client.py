import socket 

connection = ("10.0.2.15", 9999)
clientSocket = socket.socket()
clientSocket.connect(connection)
try:
    while True:
        data = input("> ")
        clientSocket.send(str.encode(data))
        received = clientSocket.recv(2048)
        print("Server: {}".format(received.decode('utf-8')))
except KeyboardInterrupt:
    print("Exiting..")

    
