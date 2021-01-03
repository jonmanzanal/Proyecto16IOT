#Importar librerias
import time
from grove.gpio import GPIO
import paho.mqtt.client as mqtt
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import threading

#Parametros InfluxDB para la conexión
token = "svvTGy8YYtsWjVtv8scOjs5fV9G_q-QDxR19poY90TYuPBrzUxvxZ-pLyiqDhs9dA1RT33PGRKNFe9w7rncNJw=="
org = "grupodaic16@gmail.com"
bucket = "grupodaic16's Bucket"

inFluxclient = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=token)
write_api = inFluxclient.write_api(write_options=SYNCHRONOUS)

#GPIOs que se utilizan para vibradores
gpio1 = 22
gpio2 = 24
gpio3 = 26

Objetos de GPIO de grove para el control
vibrator1 = GPIO(gpio1, GPIO.OUT)
vibrator2 = GPIO(gpio2, GPIO.OUT)
vibrator3 = GPIO(gpio3, GPIO.OUT)

#array para ahorrar tiempo al presionar cada sensor. Inicialmente cero, lo que significa que comienza a contar el tiempo después de que comienza el código
count_for_vibrator=[0,0,0]

# función para publicar datos en influxdb
def post_to_influxDB():
    global count_for_vibrator
    global write_api
    data = "mem,host=host1 sensor1="+str(count_for_vibrator[0])+",sensor2="+str(count_for_vibrator[1])+",sensor3="+str(count_for_vibrator[2])
    print(data)
    write_api.write(bucket, org, data)
    
#Función para hacer que cada motor vibre a una velocidad / frecuencia diferente
def thread_function(vibrator,n):
    global count_for_vibrator
    while True:
        if count_for_vibrator[n]==0:
            vibrator.write(0)
        elif count_for_vibrator[n]<10:
            vibrator.write(1)
            time.sleep((10-count_for_vibrator[n])*0.1)
            vibrator.write(0)
            time.sleep((10-count_for_vibrator[n])*0.1)
        else:
            vibrator.write(1)
            time.sleep(1)
            vibrator.write(0)
            time.sleep(1)
# Se llama a la función cuando el cliente está conectado a mqtt broker / server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe('status')
# Se llama a la función cuando se recibe un mensaje nuevo a través de mqtt
def on_message(client, userdata, msg):
    status=str(msg.payload)[2:-1]
    global count_for_vibrator
    t=threading.Thread(target=post_to_influxDB, args=())
    t.start()
    for i in range(0,3):
        if status[i]=='H':
            count_for_vibrator[i]+=1
        else:
            count_for_vibrator[i]=0

# Parametros para iniciar mqtt
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.105", 1883, 60)
client.loop_start()

# Arranque 3 hilos para que 3 motores vibren a 3 velocidades diferentes
t1 = threading.Thread(target=thread_function, args=(vibrator1,0,))
t2 = threading.Thread(target=thread_function, args=(vibrator2,1,))
t3 = threading.Thread(target=thread_function, args=(vibrator3,2,))

t1.start()
t2.start()
t3.start()

# Espere hasta que se complete un hilo. que no va a hacerlo debido al bucle infinito, así que es una especie de bucle infinito
t1.join()
t2.join()
t3.join()
