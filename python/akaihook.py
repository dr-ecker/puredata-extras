#!/usr/bin/python3

import sys
import socket

midi_device = sys.argv[1]

f = open(midi_device,"rb")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",60001))
print("Connected to " + midi_device + " and " + str(60001))

while(True):
    a=f.read(3)
    msg = str(int(a[0])) + " " + str(int(a[1])) + " " + str(int(a[2])) + ";"
    s.sendall(bytes(msg,'utf-8'))
