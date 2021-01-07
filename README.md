
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

### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Laravel](https://laravel.com)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

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
Necesitamos la biblioteca cliente influxdb para publicar los datos en la base de datos de Python. Ingresamos el siguiente comando en la terminal para instalar la biblioteca influxdb_client.  
     ```sh
   	 sudo pip3 install influxdb_client
    ```  




<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





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

