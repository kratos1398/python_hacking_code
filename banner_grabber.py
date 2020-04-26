import socket
import argparse
import ipaddress
from sys import exit
import os

top_ten = (80,21,22,23,80,443,3206,139,53,3389)

def grab(ip, port):
    if type(ip) == ipaddress.IPv4Address:  # Check if type is of ipv4
        ip = str(ip)                       # must make it to a string in order for the s.connect_ex to work
        try:
            socket.setdefaulttimeout(2)
            s = socket.socket()
            r = s.connect_ex((ip,port))
            if r == 0:
                byte = str.encode("Data:\r\n")
                s.send(byte)
                banner = s.recv(2048)
                s.close()
                return banner
            else:
                return 
        except ConnectionAbortedError:
            return "Connection Aborted"
        except ConnectionRefusedError:
            return "Conenction Refused"
        except ConnectionResetError:
            return "Connection resested."


parser = argparse.ArgumentParser(description="This is a port scanner")
parser.add_argument("ipaddress", metavar="IP", help="Enter, in CIDR notation, a ip address")
parser.add_argument("-p","--port",metavar="",default=21,type=int,help="Enter a single port number")
parser.add_argument("--topten",action="store_true",help="Chooses the top ten ports")
args = parser.parse_args()

if args.ipaddress:
    ip_range = args.ipaddress
else:
    print("No ip specified")
    exit(1)
ip_range = ipaddress.IPv4Network(ip_range,strict = False)
if ip_range.prefixlen == 32:
    ip_list = [ip_range.network_address]
else:
    ip_list = list(ip_range.hosts())
try:
    for i in ip_list:
        if args.topten:
            ports = top_ten
        else:
            ports = args.port
        print("Host: {}".format(i))
        for p in ports:
            banner = grab(i,p)
            if banner:
                print("\tPort {}: {}".format(p,banner))
                fullPath = os.path.join(os.getcwd(),"openports.txt")
                with open(fullPath, mode='w') as f:
                    openStuff = str(i) + ": " "Port " + str(p) + ": " + str(banner)
                    f.write(openStuff)
                
            else:
                print("\tNot listening on Port {}".format(p))
except KeyboardInterrupt:
    print("Exiting...")

