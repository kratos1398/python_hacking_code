import socket
from nacl import utils
from nacl.public import PrivateKey, Box
from nacl.encoding import Base64Encoder

allisonKey = PrivateKey.generate()
allisonPub = allisonKey.public_key

clientSocket = socket.socket()
clientSocket.connect(("192.168.56.1",9999))
clientSocket.send(str.encode(str(allisonPub)))
data = clientSocket.recv(2048)
allisonBox = Box(allisonKey,data.decode('utf-8'))
print("Secure communication secure.")
while True:
    recieved = clientSocket.recv(2048)
    recieved = allisonBox.decrypt(recieved,encoder=Base64Encoder)
    print("Server: {}".format(recieved.decode('utf-8')))
    message = input("> ")
    message = allisonBox.encrypt(message,encoder=Base64Encoder)
    clientSocket.send(str.encode(message))

