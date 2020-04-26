import socket
connection = ("192.168.56.1", 9999)
clientSocket = socket.socket()
clientSocket.connect(connection)
while True:
    try:
        data = input("> ")
        clientSocket.send(str.encode(data))
        recieved = clientSocket.recv(2048)
        print("Server: " + recieved.decode('utf-8'))
    except KeyboardInterrupt:
        print("Exiting..")
        break
