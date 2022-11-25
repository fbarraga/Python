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
    