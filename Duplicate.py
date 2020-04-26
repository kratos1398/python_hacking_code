import os
from hashlib import md5
from sys import argv
## line 5 allows the user to input any absolute path to a directory within the terminal
if len(argv) == 2 and os.path.exists(argv[1]) and os.path.isdir(argv[1]):
    hashDict = {}
    path = argv[1]
    for dirpaths, dirnames, filenames in os.walk(path):
        for files in filenames:
            fullPath = os.path.join(dirpaths,files)
            md5_hash = md5()
            with open(fullPath, "rb") as f:
                for block in iter(lambda: f.read(4096), b""):
                    md5_hash.update(block)
                fileHashes = md5_hash.hexdigest()
            if fileHashes in hashDict:
                hashDict[fileHashes].append(fullPath)
            else:
                hashDict[fileHashes] = [fullPath]
        
    for k in hashDict.keys():
        if len(hashDict[k]) > 1:
            print("Duplicate hash: {}".format(k))
            for i in hashDict[k]:
                print("\t {}".format(i))

    nextStuff = input("Wanna Delete a Duplicate? (y or n) ")
    if nextStuff.lower().startswith('y'):
        delete = input("Which file: ")
        os.remove(delete)  
        print("{} was deleted".format(delete))
    else:
        quit()  
else:
    print("Not a directory.")