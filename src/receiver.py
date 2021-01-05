import socket
from grove.gpio import GPIO
import time

led = GPIO(22, GPIO.OUT)
listensocket = socket.socket() #Creates an instance of socket
Port = 8012 #Port to host server on
maxConnections = 999
IP = socket.gethostname() #IP address of local machine
listensocket.bind(('',Port))
p=0
vibra = False
#Starts server
listensocket.listen(maxConnections)
print("Server started at " + IP + " on port " + str(Port))

#Accepts the incomming connection
(clientsocket, address) = listensocket.accept()
print("New connection made!")

running = True
while running:
    message = clientsocket.recv(1024).decode() #Gets the incomming message
    print(message)
    if not message == "0":
        p=int(message)
        led.write(p)
        time.sleep(0.1)
    else:
        vibra = False
        led.write(0)
        time.sleep(0.1)
