# Control de stock Con drones automatizados
<a name="top"></a>
## **Indice:**
- ### [**Objetivo**](#Item1)
- ### [**Dron**](#Item2)
- ### [**Librerias**](#Item3)  
    - ### [**OpenCV**](#Item4)  
    - ### [**Djitellopy**](#Item5)  
    - ### [**Time**](#Item6)  
    - ### [**Barcode**](#Item7)  
    - ### [**Qrcode**](#Item8)  
    - ### [**Pyzbar**](#Item9)  
- ### [**Funcionamiento**](#Item10)  



<a name="Item1"></a>
## **Objetivo** 

---
Este proyecto busca presentar a los drones como una herrmienta para el apoyo logistico en las tomas fisicas, reduciendo el reisgo para el personal ademas de los costos necesarios para la movilizacion de este personal, haciendo uso del alcance y la versatilidad de los drones para estas tomas fisicas 

---

<a name="Item2"></a>
## **Dron**
<br/>
<br/>

![DRON TELLO](https://skymotion.com.co/wp-content/uploads/2020/06/medium_aeb2fa7f-0bb6-4c10-a8a9-b75b39e9527d.jpg)


Se decide usar [Dron Tello](https://m.dji.com/product/tello) de [DJI](https://www.dji.com/)
 debido a su enfoque en el aprendizaje y su bajo costo, ademas de venir preparado para ser programado de manera agil, lo cual premite los testeos de la primera version de este proyecto, con el fin de conocer sus alcances y limitaciones, para determinar lo que se buscara en la proxima iteracion del mismo.

<br/>
<br/>
<br/>


a
***

<a name="Item3"></a>
# **Librerias**


<a name="Item4"></a>
- ## **Opencv** 
    
  Es una de las librerias principales, ya que es la que se encarga de renderizar las imagenes a travez del video recibido por la camara del dron. [**Opencv**](https://opencv.org/) es una libreria de codigo abierto basada en inteligencia artificial y maching lerning, en este momento del desarrollo dependemos de esta para la interpretacion de las imagenes, pero cabe mencionar que apenas estamos haciendo uso del potencial de esta libreria, asi que dentremos un **#TODO** importante para conocer hasta que punto podriamos exprimirla para un punto mas avanzado en el desarrollo del proyecto  

  ######  <div style="text-align: right">[**opencv-python 4.6.0.66**](https://pypi.org/project/opencv-python/)
  ~~~
  pip install opencv-python
  ~~~

<a name="Item5"></a>
- ## **Djitellopy** 
    
  Esta libreria es la encargada del control de todas las funciones del dron, es bastante potente aunque en las pruebas realizadas su respuesta no es la mejor comparada con la aplicacion propia de [DJI](https://www.dji.com/)
  ######  <div style="text-align: right">[**djitellopy 2.4.0**](https://pypi.org/project/djitellopy/)  
  ~~~
  pip install djitellopy
  ~~~

<a name="Item6"></a>

- ## **Time**
  
  Con esta libreria accedemos al reloj interno del ordenador, para controlar la secuencia que seguira el dron basados en tiempos, no tiene que ser instalada ya que viene dentro de las librerias estandar de python

<a name="Item7"></a>

- ## **Python-barcode**

  Esta libreria se utiliza para generar codigos de barras usando distintos tipos de codificacion. para el proyecto se uso el [**code128**]( https://es.wikipedia.org/wiki/Code_128) debido a su alta densidad y que nos permite codificar caracteres alfanumericos
    ######  <div style="text-align: right">[**python-barcode 0.24.0**](https://pypi.org/project/python-barcode/)
  ~~~
  pip install python-barcode
  ~~~

<a name="Item8"></a>

- ## **Qrcode** 
    
    Es similar a la anterior pero usando codigos [**qr**]() que tambien estan siendo usados para las pruebas
    ######  <div style="text-align: right">[**QRCode 7.3.1**](https://pypi.org/project/qrcode/)
    ~~~
    pip install qrcode
    ~~~

<a name="Item9"></a>

- ## **Pyzbar** 
    
    Esta libreria tiene un algoritmo que detecta en una imagen los codigos ya sean qr o codigos de barras, devolviendonos no solo el contendido del codigo sino su posicion su tamaño entre otros datos referente a los mismo, es a donde se envian las imagenes capturadas por [**Opencv**](https://opencv.org/)
    ######  <div style="text-align: right">[**Pyzbar 0.19**](https://pypi.org/project/pyzbar/)
    ~~~
    pip install pyzbar
    ~~~

- ## **Threading** 
    
    Esta libreria es la encargada de ejecutar procesos de forma paralela a nuestro codigo principal con el fin de que no se interrumpa ninguno de los procesos que se requieran en constante ejecucion, esta basada en el uso de los distintos hilos del procesador  
    ###### <div style="text-align: right">[**Threading**](https://docs.python.org/es/3.8/library/threading.html)


 
    <br/>
    <br/>

---
////////////////////////////////////////////////////////////////////////////////////////////

---

<br/>


<a name="Item10"></a>

## **Funcionamiento**


- **Version 1.0**

  ---

    El dron esta transmitiendo de manera constante la visualizacion de la camara y decodificando los codigos en los tiempos que se le indican, pero su movimiento es impredecible, se estan realizando pruebas modificando los intervalos de vuelo, deteccion de codigo, envio de instrucciones. el metodo usado actualmente para el movimiento del dron es de [**Djitellopy**](#Item5)  

    ~~~

    send_rc_control(left_right_velocity: int, forward_backward_velocity: int, up_down_velocity: int,yaw_velocity: int)

    ~~~

    en las pruebas de vuelo no se a conseguido la estabilidad y presicion deseada por lo que se estan evaluando metodos  alternativos

  ---

 ## [**Ir arriba**](#top) 


