#Importar librerias
import time
from grove.gpio import GPIO
import paho.mqtt.client as mqtt
import threading

gpio1 = 22
gpio2 = 24
gpio3 = 26
gpio4 = 20
gpio5 = 21

vibrator1 = GPIO(gpio1, GPIO.OUT)
vibrator2 = GPIO(gpio2, GPIO.OUT)
vibrator3 = GPIO(gpio3, GPIO.OUT)
vibrator4 = GPIO(gpio4, GPIO.OUT)
vibrator5 = GPIO(gpio5, GPIO.OUT)

count_for_vibrator=[0,0,0,0,0]

#Función para hacer que cada motor vibre a una velocidad / frecuencia diferente
def thread_function(vibrator,n):
    print("Thread Started:",str(n))
    global count_for_vibrator
    print(count_for_vibrator[n])
    while True:
        if count_for_vibrator[n]==0:
            vibrator.write(0)
        elif count_for_vibrator[n]<5:
            vibrator.write(1)
            time.sleep((5-count_for_vibrator[n])*0.2)
            vibrator.write(0)
            time.sleep((5-count_for_vibrator[n])*0.2)
        else:
            vibrator.write(1)
# Se llama a la función cuando el cliente está conectado a mqtt broker / server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("status")
    
# Se llama a la función cuando se recibe un mensaje nuevo a través de mqtt
def on_message(client, userdata, msg):
    status=str(msg.payload)[2:-1]
    global count_for_vibrator1
    for i in range(0,4):
        if status[i]=='H':
            count_for_vibrator[i]+=1
        else:
            count_for_vibrator[i]=0
            
# Parametros para iniciar mqtt
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.0.105", 1883, 60)
client.loop_start()

# Arranque 3 hilos para que 3 motores vibren a 3 velocidades diferentes
t1 = threading.Thread(target=thread_function, args=(vibrator1,0,))
t2 = threading.Thread(target=thread_function, args=(vibrator2,1,))
t3 = threading.Thread(target=thread_function, args=(vibrator3,2,))
t4 = threading.Thread(target=thread_function, args=(vibrator4,3,))
t5 = threading.Thread(target=thread_function, args=(vibrator5,4,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
# Espere hasta que se complete un hilo. que no va a hacerlo debido al bucle infinito, así que es una especie de bucle infinito
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
