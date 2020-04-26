import socket

serverSocket = socket.socket()
serverSocket.bind(("0.0.0.0",9999))
serverSocket.listen(1)
print("Listening..")
clientSocket,clientAddress = serverSocket.accept()
while True:
    try:
        data = clientSocket.recv(2048)
        print("Client: {}".format(data.decode("utf-8")))
        sendData = input("> ")
        clientSocket.send(str.encode(sendData))
    except KeyboardInterrupt:
        print("Exiting..")
        quit()
