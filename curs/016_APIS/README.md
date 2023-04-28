# Python requests: Consumiendo información de un servicio web Restful

## Objetivos

* Introducir los conceptos sobre servicios web
* Conocer las características de los servicios web API restful
* Conocer el lenguaje de marcas json 
* Utilizar python para realizar peticiones a un servicio web API restful
* Utilizar python para tratar la información obtenida del servicio web en formato json

## Nivel

Intermedio

## ¿Qué aprenderás en el taller?

* Las características principales de los servicios web API restful
* Las formas de autentificación para conectar a los servicios web API restful
* Las características fundamentales del lenguaje de marcas json
* El uso de la librería *requests* de python que nos permite realizar peticiones HTTP
* El tratamiento de información formateada en json desde python

## Conocimientos previos

* Conocimientos básicos del protocolo HTTP
* Conocimientos básicos de python3


## Servicio web
Servicios Web
▸ Es un método de comunicación entre máquinas/programas a través de la red (normalmente Internet)
▹ Las páginas web la usan las personas.
▹ Los servicios web lo usan los programas.
▸ WEB PROGRAMABLE: mediante diferentes APIs (web API) podemos configurar gran cantidad de aplicaciones basadas en 
recursos de la Web
▹ Podemos consumir (solo lectura) recursos de un servicio 
web
▹ Podemos modificar (lectura/escritura)los recursos de un 
servicio web




3. JSON
JSON JSON (JavaScript Object Notation) es un lenguaje de  marcas que nos permite representar información.

{
  "colors": [
    {
      "color": "black",
      "code": {
        "rgba": [255,255,255,1],
        "hex": "#000"
      }
    },
    {
      "color": "white",
        "rgba": [0,0,0,1],
        "hex": "#FFF"
      }
    }
}


Dos estructuras básicas:
▸ Diccionarios
▸ Listas

4. Python3  y REST
Python3 y REST
▸ Podemos usar Python3 para crear programas que utilice API RESTful para consumir/modificar los recursos de un servicio 
web. Para ello vamos a usar dos librerías: 
▹ requests: Nos permite realizar peticiones HTTP y gestionar la respuesta del servidor.
▹ json: Nos permite trabajar con información en formato json 



## Desarrollo

1. Ver presentación
2. Consultas con `curl` desde línea de comandos:

    * API sin key: https://swapi.co (Ver Documentación)

            curl https://swapi.co/api/people/
            curl https://swapi.co/api/people/1/ | json_pp 

    * API con key: https://openweathermap.org/. Ver Documentación de la API: https://openweathermap.org/api. Acceder y crear un API key nueva.

            export open_wheather_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            curl curl "http://api.openweathermap.org/data/2.5/weather?q=Sevilla&mode=json&units=metric&APPID=$open_wheather_key" | json_pp

3. ¿Cómo podemos realizar consultas http con python3? Utilizando la librería `requests`.

    * Instalación de `requests`:

            python3 -m venv env
            source env/bin/activate

            pip install requests

    * Consulta a swapi

            >>> import requests
            >>> r=requests.get("https://swapi.co/api/people/1/")
            >>> r.status_code
            200
            >>> r.json()
            >>> datos=r.json()
            >>> print(datos["name"])
            Luke Skywalker

    * Consulta openwheathermap:

            >>> import requests
            >>> import os
            >>> api_key=os.getenv("open_wheather_key")
            >>> parametros={"q":"Sevilla","mode":"json","units":"metric","APPID":api_key}
            >>> r=requests.get("http://api.openweathermap.org/data/2.5/weather",params=parametros)
            >>> r.status_code
            200
            >>> r.url
            'http://api.openweathermap.org/data/2.5/weather?q=Sevilla&units=metric& APPID=xxx&mode=json'
            >>> r.json()
            >>> datos=r.json()
            >>> print(datos["main"]["temp"])

            
    * Demo1: Temperatura: https://openweathermap.org/api
    * Demo2: Fútbol: https://es.besoccer.com/api/documentacion
    * Demo3: Cine: https://developers.themoviedb.org/3/getting-started/introduction
    