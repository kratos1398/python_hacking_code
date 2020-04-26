# this program hashs any file you enter in. 


from hashlib import md5

filename = raw_input("Enter the file name: ")
md5_hash = md5()
# this opens the file and saves the name as 'f' within the program. 
with open(filename, "rb") as f: # this opens the file in read only in byte form
    for block in iter(lambda: f.read(4096), b""): # in memory, your only gonna store 4096 bytes
        md5_hash.update(block)
    print md5_hash.hexdigest()