import scapy
scapy.send(IP(dst="192.168.86.81")/ICMP())