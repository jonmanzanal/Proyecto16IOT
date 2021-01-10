import time
from grove.gpio import GPIO

led = GPIO(22, GPIO.OUT)
led2 = GPIO(24, GPIO.OUT)
led3 = GPIO(26, GPIO.OUT)
button = GPIO(5, GPIO.IN)
button2 = GPIO(16, GPIO.IN)
button3 = GPIO(18, GPIO.IN)
count=0
count2=0
count3=0
p=0
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
    return switcher.get(i,10)
while True:
    if button.read():
        count=count+1
        print(count)
        p=potencia(count)
        led.write(p)
    else:
        led.write(0)
        count=0
        time.sleep(0.1)
        
    if button2.read():
        count2=count2+1
        p=potencia(count2)
        led2.write(p)
        
    else:
        led2.write(0)
        count2=0
        time.sleep(0.1)
    if button3.read():
        count3=count3+1
        p=potencia(count3)
        led3.write(p)
        
    else:
        led3.write(0)
        count3=0
        time.sleep(0.1)


    
