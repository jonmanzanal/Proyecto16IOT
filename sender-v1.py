import time
from grove.gpio import GPIO
import paho.mqtt.client as mqtt

  
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


gpio1 = 5
gpio2 = 16
gpio3 = 18
gpio4 = 22
gpio5 = 22

sensor1 = GPIO(gpio1, GPIO.IN)
sensor2 = GPIO(gpio2, GPIO.IN)
sensor3 = GPIO(gpio3, GPIO.IN)
sensor4 = GPIO(gpio4, GPIO.IN)
sensor5 = GPIO(gpio5, GPIO.IN)

client = mqtt.Client()
client.on_connect = on_connect
client.connect("192.168.1.105", 1883, 60)
client.loop_start()

while True:
    status=""
    if sensor1.read():
        status+="H"
    else:
        status+="L"
    if sensor2.read():
        status+="H"
    else:
        status+="L"
    if sensor3.read():
        status+="H"
    else:
        status+="L"
    if sensor4.read():
        status+="H"
    else:
        status+="L"
    if sensor5.read():
        status+="H"
    else:
        status+="L"

    print(status)
    print('{}'.format(potencia.value))
    time.sleep(0.1)
    client.publish("status",status)
    time.sleep(2)
    
