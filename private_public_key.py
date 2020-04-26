from nacl import utils
from nacl.public import PrivateKey, Box
from nacl.encoding import Base64Encoder

fabianKey = PrivateKey.generate()
fabianPub = fabianKey.public_key

allisonKey = PrivateKey.generate()
allisonPub = allisonKey.public_key

fabianBox = Box(fabianKey,allisonPub)
allisonBox = Box(allisonKey,fabianPub)

message = input("> ")
message = str.encode(message)

encryptedMessage = fabianBox.encrypt(message, encoder=Base64Encoder)
print("Plain text: {}".format(message))
print("Encrypted text: {}".format(encryptedMessage))
print("Allison received message")
print("She now decrypted it: {}".format(allisonBox.decrypt(encryptedMessage,encoder=Base64Encoder)))