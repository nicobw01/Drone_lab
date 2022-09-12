# Control de stock Con drones automatizados
<a name="top"></a>
## **Indice:**
- ### [**objetivo**](#Item1)
- ### [**dron usado**](#Item2)
- ### [**Librerias**](#Item3)  
    - ### [**Djitello**](#Item4)  
    - ### [**Time**](#Item5)  
    - ### [**Barcode**](#Item6)  



<a name="Item1"></a>
## **Objetivo** 

---
Este proyecto busca presentar a los drones como una herrmienta para el apoyo logistico en las tomas fisicas, reduciendo el reisgo para el personal ademas de los costos necesarios para la movilizacion de este personal, haciendo uso del alcance y la versatilidad de los drones para estas tomas fisicas 

---

<a name="Item2"></a>
## **Dron usado**

![DRON TELLO](https://skymotion.com.co/wp-content/uploads/2020/06/medium_aeb2fa7f-0bb6-4c10-a8a9-b75b39e9527d.jpg)


Se decide usar [Dron Tello](https://m.dji.com/product/tello) de [DJI](https://www.dji.com/)
 debido a su enfoque en el aprendizaje y su bajo costo, ademas de venir preparado para ser programado de manera agil, lo cual premite los testeos de la primera version de este proyecto, con el fin de conocer sus alcances y limitaciones, para determinar lo que se buscara en la proxima iteracion del mismo.

<br/>
<br/>
<br/>
<br/>
<br/>


***

<a name="Item3"></a>
# **Librerias**


<a name="Item4"></a>
- ## **Djitello** 
    
  Esta libreria es la encargada del control de todas las funciones del dron, es bastante potente aunque en las pruebas realizadas su respuesta no es la mejor comparada con la aplicacion propia de [DJI](https://www.dji.com/)  
  ~~~
  pip install djitello
  ~~~

<a name="Item5"></a>

- ## **Time**
  
  Con esta libreria accedemos al reloj interno del ordenador, para controlar la secuencia que seguira el dron basados en tiempos, no tiene que ser instalada ya que viene dentro de las librerias estandar de python

<a name="Item6"></a>

- ## **Barcode**
  Esta libreria se utiliza para generar codigos de barras usando distintos tipos de codificacion. para el proyecto se uso el [**code128**](https://es.wikipedia.org/wiki/Code_128) debido a su alta densidad y que nos permite codificar caracteres alfanumericos






## -[**subir**](#top) 


