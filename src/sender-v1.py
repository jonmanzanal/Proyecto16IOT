#Importar librerias
import time
from grove.gpio import GPIO
import paho.mqtt.client as mqtt
from gyro import SensorITG3200

# Se llama a la función cuando el cliente está conectado a mqtt broker / server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

#GPIOs que se utilizan para sensores
gpio1 = 5
gpio2 = 16
gpio3 = 18

#Asignacion funcionalidad
sensor1 = GPIO(gpio1, GPIO.IN)
sensor2 = GPIO(gpio2, GPIO.IN)
sensor3 = GPIO(gpio3, GPIO.IN)

#Parametros y conexion mediante MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.connect("192.168.1.105", 1883, 60)
client.loop_start()

# Parametros del giroscopio
sensor = SensorITG3200(1, 0x68)
sensor.default_init()

#Funcionalidad de tocar los sensores.
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
    gx, gy, gz = sensor.read_data()
    if int(gy)>100:
        status+="R"
    elif int(gy)<-100:
        status+="L"
    else:
        status+="N"
    
    print(status)
    #Envio del estado de los sensores
    client.publish("status",status)
    time.sleep(2)
