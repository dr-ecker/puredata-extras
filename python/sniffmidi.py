import sys
import socket

midi_device = sys.argv[1]

f = open(midi_device,"rb")
print("Connected to " + midi_device)

while(True):
    a=f.read(3)
    msg = str(int(a[0])) + " " + str(int(a[1])) + " " + str(int(a[2])) + ";"
    print(msg)
