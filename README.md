# SenseGlove


<!-- TABLA DE CONTENIDOS -->
<details open="open">
  <summary>Tabla de Contenidos</summary>
  <ol>
    <li>
      <a href="#about-the-project">Acerca del Proyecto</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#usage">Funcionalidad</a></li>
    <li><a href="#contributing">Contribuyendo</a></li>
    <li><a href="#bib">Bibliografía</a></li>
    <li><a href="#wiki">Wiki</a></li>
  </ol>
</details>



<!-- ACERCA DEL PROYECTO -->
## Acerca del Proyecto

![iot](https://user-images.githubusercontent.com/43879255/103910351-05449880-5105-11eb-99d7-0b70c2049883.jpeg)


Se propone una solución que utiliza un sistema de control remoto basado en Internet de las cosas (IoT) a través de una red Wi-Fi para simular un apretón de manos, que comprende el control remoto de los motores de vibración en función de los datos que se obtienen a partir de una serie de sensores táctiles capacitivos y un giroscopio. En lugar de usar Bluetooth o un enfoque por cable, estamos usando Wi-Fi para una conexión rápida, confiable y de largo alcance a través de Internet.

Estamos usando Raspberry Pi tanto en el lado emisor como en el receptor, ya que se consume muy poca energía y tiene Wi-Fi incorporado. La solución propuesta se basa en utilizar el protocolo MQTT para el paso de mensajes de máquina a máquina. MQTT es un protocolo ligero con el encabezado TCP más corto y ayuda a lograr una conmutación en tiempo real y un bajo consumo de energía al mismo tiempo.

Simultáneamente, se publican a una base de datos de InfluxDB los datos de los sensores, concretamente el tiempo por pulso de cada uno de los sensores.  


<!-- GETTING STARTED -->
## Getting Started

Para el funcionamiento del proyecto se necesitan unas determinadas librerías. Siga los siguientes pasos para su instalación.

### Instalación

1. Instalación Mosquitto Broker.  
   Para instalar el broker de MQTT, abrimos la terminal e ingresamos el siguiente comando.
   ```sh
   sudo apt-get install mosquitto
   ```  
   Para instalar las bibliotecas de cliente de mqtt para probar la conexión, ingresamos el siguiente comando.  
   ```sh
   sudo apt-get install mosquitto-clients
   ```  
   Para probar el broker, abrimos 2 terminales e ingresamos los siguientes comandos en cada terminal para enlazarnos a un tema y publicar un mensaje.  
   ```sh
   mosquitto_sub –t test
   mosquitto_pub –t test –m hi
   ```  
   Ingresamos el siguiente comando en la terminal para instalar la biblioteca cliente mqtt para python.  
   ```sh
   sudo pip3 instalar paho-mqtt
   ```  

2. Instalación libreria de grove.py  
   Ingresamos los siguiente comandos en la terminal para instalar la biblioteca de grove.  
   ```sh
   git clone https://github.com/Seeed-Studio/grove.py
   cd grove.py
   # Python2
   sudo pip install .
   # Python3
   sudo pip3 install .
   ```  
      
3. Instalación librería de influxdb_client  
   Necesitamos la biblioteca cliente influxdb para publicar los datos en la base de datos de Python. Ingresamos el siguiente comando en la terminal para instalar la libreria influxdb_client.  
   ```sh
   sudo pip3 install influxdb_client
   ```  



## Funcionalidad

**Parte funcional:**
Para probar la funcionalidad del proyecto, deberemos iniciar en una Raspberry Pi el programa llamado _receiver-v1.py_ y en la otra Raspberry Pi el programa _sender-v1.py_.
Comprobamos que los programas se han iniciado correctamente y tocamos un sensor háptico. Al pulsar el sensor se mandará una "H" lo cual significa que esta pulsado sino mandará una "L". Según cuanto tiempo pulsemos vibrara el actuador en la raspberry, la vibración sera mayor o menor, aumentando en 8 unidades por cada segundo pulsado. Cada sensor actuará sobre un motor, el sensor de la izquierda actuá sobre el motor de la izquierda, lo mismo con los sensores del centro y de la derecha. 

![MotorVib_Rasp2](https://user-images.githubusercontent.com/43879255/104036583-dcd79f80-51d3-11eb-8e26-df91f97acd7d.png)
![Sensors_Rasp1](https://user-images.githubusercontent.com/43879255/104036590-dfd29000-51d3-11eb-9297-a35e0e02ce01.png)


Para probar el giroscopio se deberá mantener pulsado los sensores de los extremos (izquierda y derecha), luego al mover el giroscopio vibrará más un actuador u otro según hacia donde lo movamos.  

Para controlar la vibración de los actuadores, podemos utilizar el deslizador. Si situamos el deslizador a un valor cercano a 0 (gnd) la vibración será más intensa, si lo movemos hacia el medio la vibración será la mitad y si lo movemos hasta el final (vcc) la vibración se reducirá por cuatro.


**Publicación de datos:**
Durante la ejecución de los scripts mencionados arriba, la parte receptora va publicando los datos a la base de datos de InfluxDB. En la siguiente imagen se muestra la estructura y los campos que se almacenan, en este caso para el sensor3.

![Sens3](https://user-images.githubusercontent.com/43879255/104035405-61c1b980-51d2-11eb-9170-50745e36e413.JPG)

Los campos que se almacenan son los siguientes:
* **Start_time,stop_time y time**: Son variables autogeneradas por influxDB, la única relevante en nuestro caso es time, indica la hora de la publicación a la BD.
* **Field**: Nombre de la variable, en este caso hace referencia a los sensores (sensor1, sensor2, sensor3)
* **Value**: Tiempo de pulso del sensor.

_Para mayor información, es posible consultar la Wiki [Documentation](https://github.com/jonmanzanal/daicgrupo16/wiki)_



<!-- CONTRIBUTING -->
## Autores y forma de trabajo ✒️

**DAIC Grupo16:**
* **Jon Manzanal** 
* **Javier Martín**

El desarrollo del código del proyecto lo hemos realizado conjuntamente mediante Discord ya que las caractéristicas del proyecto implicaban que alguien tenía que tener las 2 Raspberry en la misma red para poder hacer las pruebas y comprobar que la funcionalidad fuera la correcta. Para realizar los commits respectivos al código hemos utilizado en las Raspberry sólo una cuenta de Github (jonmanzanal), pero hemos desarrollado el código conjuntamente.


También puedes mirar la lista de todos los [contribuyentes](https://github.com/jonmanzanal/daicgrupo16/contributors) que han participado en este proyecto.



<!-- LICENSE -->
## Bibliografia

* N. Crowley, «Getting Started with Python and InfluxDB», InfluxData, mar. 30, 2018. https://www.influxdata.com/blog/getting-started-python-influxdb/ .
* «2 Simple Ways to Implement Python Switch Case Statement», DataFlair, jun. 01, 2018. https://data-flair.training/blogs/python-switch-case/.
* «3.Python_RPi_2019.pdf». Disponible en: https://alud.deusto.es/pluginfile.php/1059875/mod_resource/content/1/3.Python_RPi_2019.pdf.
* «Grove - Introduction in 3-Axis Digital Accelerometer», Hackster.io. https://www.hackster.io/ingo-lohs/grove-introduction-in-3-axis-digital-accelerometer-ea05c3.
* «Lean Green RC Sailing Machine», Hackster.io. https://www.hackster.io/anemoi/lean-green-rc-sailing-machine-2cdde5.
* «MQTT - The Standard for IoT Messaging». https://mqtt.org/ .
* «Python - Functions - Tutorialspoint». https://www.tutorialspoint.com/python/python_functions.htm.
* «Replacements for switch statement in Python?», Stack Overflow. https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python.
* «Seeed-Studio/grove.py», GitHub. https://github.com/Seeed-Studio/grove.py.




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png

