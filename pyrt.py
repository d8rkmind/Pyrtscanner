#!/bin/python3

import socket 
import sys
from datetime import datetime as dt

#target defination 
portl =[]                                       # List to store port numbers
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  #resolving host name from given argument
else: 
    print("Invalid amount of arguments \n Syntax : python3 pyrt.py '<ip address or domain>' ")
    sys.exit()

print("-" * 50)
print("Scanning target "+ target)
print("Time Started  : "+ str(dt.now()))
print("-" * 50)

try:
    for port in range(1,10000):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))                    # scanning for openports 
        print("\n Checking at "+ target +":" +str(port)+"\t")
        if result == 0:
            portl.append(port)
        s.close()

except KeyboardInterrupt:
    print("\n Bye for now")
    sys.exit()
    
except socket.gaierror:
    print("\n Hostname couldnot be resolved")
    sys.exit()

except socket.error:
    print("\n Error couldnt found")
    sys.exit()

print("*" * 50) 

for i in portl:
    print("\n\tFound open port : {}\n".format(i))

print("*" * 50)
