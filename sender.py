import socket
import time
from grove.gpio import GPIO



#Creates instance of 'Socket'
s = socket.socket()
count=0
button = GPIO(5, GPIO.IN)
hostname = '192.168.1.105' #Server IP/Hostname
port = 8012 #Server Port
p=0
s.connect((hostname,port)) #Connects to server
def potencia (i):
    switcher={
        1: 1,
        2: 2,
        3: 3,
        4: 5,
        5: 8,
        6: 13,
        7: 21,
        8: 34
    }
    return switcher.get(i,0)
while True:
    if button.read():
        count=count+1
        p=potencia(count)
        m=str(p)
        s.send(m.encode())
        time.sleep(0.1)
    else:
        p=0
        m=str(p)
        count=0
        s.send(m.encode())
        time.sleep(0.1)