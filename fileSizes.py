import sys
import os
import argparse
parser = argparse.ArgumentParser(description="This is to see file sizes.")

parser.add_argument("--file","-f",metavar="",help="Put file name to see single file size")
parser.add_argument("--directory","-d",metavar="",help="Put directory path to see all file sizes in specified directory.")
args = parser.parse_args()

if args.file:
    fileName = args.file
    filenamePath = os.path.join(os.getcwd(),fileName)
    fileSize = os.path.getsize(filenamePath)
    print("{} : {} bytes".format(fileName,fileSize))

if args.directory:
    directoryName = args.directory
    for dirpaths, dirnames, filenames in os.walk(directoryName):
        for f in filenames:
            fullPath = os.path.join(dirpaths,f)
            fileSizes = os.path.getsize(fullPath)
            print("{} : {} bytes".format(f, fileSizes))
    



