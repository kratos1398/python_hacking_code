from sys import argv
import os

if len(argv) ==2 and os.path.isfile(argv[1]):
    fullfilePath = os.path.join(os.getcwd(), argv[1])
    fileSize = os.path.getsize(fullfilePath)
    print "file size: %s bytes" % (fileSize)
else:
    print "Not a file."