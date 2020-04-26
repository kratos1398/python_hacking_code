import socket

conenction = ("0.0.0.0", 9999)
serverSocket = socket.socket()
serverSocket.bind(conenction)
serverSocket.listen(1)
print("Listening..")
clientSocket, clientAddress = serverSocket.accept() # This is only used in server side
while True:
    try:
        data = clientSocket.recv(2048)
        if len(data) > 0:
            print("Client: " + data.decode('utf-8'))
        sendData =input("> ")
        clientSocket.send(str.encode(sendData)) # to send data, use 1st parameter in .accept()
    except KeyboardInterrupt:
        print("Exiting..")
        break
