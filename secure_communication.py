import socket
from nacl import utils
from nacl.public import PrivateKey, Box
from nacl.encoding import Base64Encoder

fabianKey = PrivateKey.generate()
fabianPub = fabianKey.public_key

serverConnection = socket.socket()
serverConnection.bind(("192.168.56.1",9999))
serverConnection.listen(1)

clientSocket, clientAddr = serverConnection.accept()
print("Listening...")
try:
    while True:
        data = clientSocket.recv(2048)
        print("Recieved data")
        fabianBox = Box(fabianKey,data.decode('utf-8'))
        clientSocket.send(str.encode(fabianPub))
        print("Secure communcation secured.")
        while True:
            message = input("> ")
            message = fabianBox.encrypt(str.encode(message),encoder=Base64Encoder)
            clientSocket.send(message)
            recieved = clientSocket.recv(2048)
            recieved = fabianBox.decrypt(recieved, encoder=Base64Encoder)
            print("Client: {}".format(recieved.decode('utf-8')))
except KeyboardInterrupt:
    print("Force Quit..")
