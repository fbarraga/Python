# APIS
# Python APIs: Consumint informació d'un servei web tipus API Restful 

## Objetius

* Introduir els conceptes sobre serveis web
* Conèixer les característiques dels serveis web API Restful.cer las características de los servicios web API Restful
* Conèixer el llenguatge de marques `json` 
* Utilitzar python per realitzar peticions a un servei web API restful
* Utilitzar python para tractar la informació obtinguda del servei web en formato json


## Serveis web

* És un mètode de comunicació entre màquines/programes mitjançant la xarxa (normalment Internet)
* Les pàgines web les utilitzen les persones.
* Els serveis web el utilitzen els programes.
* Web Programable: mitjançant diferents APIS (web API) podem configurar gran quantitat d'aplicacions basades en recursos de la web.
* Podem consumir (només lectura) recursos d'un servei web
* Podem modificar (lectura/escriptura) els recursos de un servei web
* Bàsicament podem trobar dos tipus de APIs:
  * API REST (Representational State Transfer): on s'intercanviarà informació principalment en format JSON.
  * API SOAP (Simple Object Access Protocol): on s'intercanviarà informació principalment en format XML



## JSON

Tal com hem vist en capítols anteriors JSON (JavaScript Object Notation) és un llenguatge de  marques que ens permet representar informació.

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

Els fitxers JSON tenen dos estructures básiques que es mapegen amb objectes de Python:
* Diccionaris
* Llistes

## Python3  y REST

* Podem utilitzar Python3 per crear programes que utilitzin API RESTful per consumir/modificar els recursos d'un servei web. Per fer-ho haurem de fer servir dos llibreries:
    * requests: Ens permet realitzar peticions HTTP i gestionar la resposta del servidor.
    * json: Ens permet treballar amb informació en formato json, que serà la que recuperarem o enviarem al servei web.


## Connexió a una API REST

* Normalment per connectar a una API Rest haurem de seguir els següents passos:
  1. 

## Exemples

1. Consultes amb `curl` des de línia de comandes:

    * API sense key: https://swapi.co (Ver Documentación)

            curl https://swapi.co/api/people/
            curl https://swapi.co/api/people/1/ | json_pp 

    * API amb key: https://openweathermap.org/. Ver Documentación de la API: https://openweathermap.org/api. Acceder y crear un API key nueva.

            export open_wheather_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            curl curl "http://api.openweathermap.org/data/2.5/weather?q=Sevilla&mode=json&units=metric&APPID=$open_wheather_key" | json_pp

2. ¿Cómo podemos realizar consultas http con python3? Utilizando la librería `requests`.

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
    