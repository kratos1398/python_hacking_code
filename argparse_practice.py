import argparse
import os

parser = argparse.ArgumentParser(description= "This is a program to show you the sizes of files")
parser.add_argument('-f','--files',metavar="",help="Type the absolute path to a directory")
args = parser.parse_args()

if args.files:
    path = args.files
else:
    path = raw_input("Enter a full path to a directory: ")

for dirpaths, dirnames, filenames in os.walk(path):
    for f in filenames:
        fullPath = os.path.join(dirpaths,f)
        fileSize = os.path.getsize(fullPath)
        print("{} \t {}".format(fullPath, fileSize))
