import os
import argparse
from cryptography.fernet import Fernet
from sys import argv

def generationKey(filename):
    key = Fernet.generate_key()
    with open(filename, mode='w') as f:
        f.write(bytes.decode(key) + '\n')
    return key

parser = argparse.ArgumentParser(description="This is cipher, decipher program")
group = parser.add_mutually_exclusive_group()
group.add_argument("-e","--encrypt",metavar="PLAINTEXT",help="Enter text to encrpyt")
group.add_argument("-d","--decrypt",metavar="CIPHERTEXT",help="Enter text to decrpyt")
otherGroup = parser.add_mutually_exclusive_group(required=True)
otherGroup.add_argument("-k","--key",metavar="FILENAME",help="enter filename that has existing key in it")
otherGroup.add_argument("--genkey",metavar="FILENAME",help="Generate a key and put in specified txt file")

if len(argv) == 1:
    argv.append("--help")

args = parser.parse_args()

if args.key:
    if os.path.isfile(args.key):
        with open(args.key) as f:
            key = f.readline()
elif args.genkey:
    if os.path.isfile(args.genkey):
        key = generationKey(args.genkey)

f = Fernet(key)

if args.encrypt:
    result = bytes.decode(f.encrypt(str.encode(args.encrypt)))
elif args.decrypt:
    result = bytes.decode(f.decrypt(str.encode(args.decrypt)))
print(result)