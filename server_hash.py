import socket
import os
from hashlib import md5

connection = ("10.0.2.15", 9999)
serverSocket = socket.socket()
serverSocket.bind(connection)
serverSocket.listen(1)
print("Listening...")

clientSocket, clientAddress = serverSocket.accept()
md5_hash = md5()
try:
    while True:
        data = clientSocket.recv(2048)
        data = data.decode('utf-8')
        if os.path.isfile(data):
            filename = os.path.join(os.getcwd(),data)
            with open(filename, "rb") as f:
                for block in iter(lambda: f.read(4096),b""):
                    md5_hash.update(block)
                    fileHash = md5_hash.hexdigest()
                    clientSocket.send(str.encode(fileHash))
                    print("Server sent the hash.")
        else:
            clientSocket.send(str.encode("File does not exist"))
except KeyboardInterrupt:
    print("Exiting..")
except ConnectionAbortedError:
    print("Aborting..")
    
