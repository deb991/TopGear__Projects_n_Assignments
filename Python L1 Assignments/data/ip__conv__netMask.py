#!/usr/bin/env python
import socket
import struct

cidr = int(input('Enter CIDR to convert into netmask :: '))
host_bits = 32 - int(cidr)
netmask__1 = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
print(netmask__1)