from hashlib import md5
import os
try:
    print("This program will compare the hashs of two files and see if they are the same or not.")
    try:
        filename = input("Input Filename: ")
        if os.path.exists(filename) and os.path.isfile(filename):
            pass
        else:
            print("This is not a file")
            quit()
        filename2 = input("Input another Filename: ")
        if os.path.exists(filename2) and os.path.isfile(filename2) and filename != filename2:
            pass
        else:
            print("This is not a file\n or you simply wrote the same file twice")
            quit()

        md5_hash = md5()
        md5_hash2 = md5()
        with open(filename, "rb") as f:
            for block in iter(lambda: f.read(4096), b""):
                md5_hash.update(block) # this adds the block within the hash function
            first= md5_hash.hexdigest()

        with open(filename2, "rb") as f:
            for block in iter(lambda: f.read(4096), b""):
                md5_hash2.update(block) # this adds the block within the hash function
            second = md5_hash2.hexdigest()


        # 'first', is the first filename hash and 'second' is the second filename hash
        if first == second:
            print("They are the same!!")
            print("{} hash : {}".format(filename,first))
            print("{} hash: {}".format(filename2,second))
            then = input("Would you like to delete one of them? ")
            while True:
                if then.lower().startswith('y'):
                    pass
                else:
                    quit()
                after = input("Which one would you like to delete? ")
                if after == filename:
                    os.remove(filename) 
                    print(" {} was deleted.".format(filename))
                    quit()
                elif after == filename2:
                    os.remove(filename2)
                    print("{} was deleted.".format(filename2))
                    quit()
                else:
                    print("Invalid entry")
                    continue

        else:    # this is if first != second.
            print("They are different.")
            print("{} hash : {}".format(filename,first))
            print("{} hash : {}".format(filename2,second))
    except IOError:
        print("Exiting..")       
except KeyboardInterrupt:
    print("FORCE EXITTING")   
