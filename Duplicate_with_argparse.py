import os
import argparse
from hashlib import md5



parser = argparse.ArgumentParser(description="This is to see all files in a directory.")
parser.add_argument("directory", metavar="",help="Enter absolute path of directory.")
args = parser.parse_args()

hashDict = {}
if args.directory:
    path = args.directory
else:
    path = input("Enter a path: ")
for dirpaths, dirnames, filenames in os.walk(path):
    for files in filenames:
        md5_hash = md5()
        fullPath = os.path.join(dirpaths,files)
        with open(fullPath,"rb") as f:
            for block in iter(lambda: f.read(4096),b""):
                md5_hash.update(block)
            fileHash = md5_hash.hexdigest()
        if fileHash in hashDict:
            hashDict[fileHash].append(fullPath)
        else:
            hashDict[fileHash] = [fullPath]
for i in hashDict.keys():
    if len(hashDict[i]) > 1:
        print("Duplicate hash: {}".format(i))
        for k in hashDict[i]:
            print("\t{}".format(k))
                

