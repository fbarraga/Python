# APIS
# Python APIs: Consumint informació d'un servei web tipus API Restful 

## Objetius

* Introduir els conceptes sobre serveis web
* Diferències entre API SOAP i API REST
* Conèixer les característiques dels serveis web API Restful
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


## Funcionament d'una API

Una API es fonamentalmente una URL on nosaltres anirem a consultar la informació que proveeix la API. Aquesta URL es un punt d'entrada, i cadascuna de les opcions de consulta/modificació les anomenarem Endpoints.

Així per exemple l'entrada a l'API de consulta del temps es : https://api.openweathermap.org/data/3.0/onecall . Els endpoints que té aquesta API son per exemple:

https://api.openweathermap.org/data/3.0/onecall?lat=30.489772&lon=-99.771335
https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units={units}


## Connexió a una API REST

* Normalment per connectar a una API Rest haurem de seguir els següents passos:
  1. Identificar-nos a la web que proveeix la API. Ens donarà un usuari i password
  2. A partir de l'usuari/password generar un token. Un token serveix per afegir-ho a la crida de l'API i així el proveidor de l'API pot saber qui està fent la consulta i aplicar càrrecs en cas de que sigui de pagament. El token no és res més que un hash que es fa sobre les dades de l'usuari normalment. El token es personal no s'ha de donar mai a conèixer a ningú.
  3. Consultar a la documentació de l'API com s'han de fer les consultes.
  4. Amb el mètode requests, preparar com s'ha de fer la consulta i executar la petició
  5. Recuperar les dades que retorna la API en format JSON
  6. Tractar el JSON.

## Exemples

1. Consultes amb `curl` des de línia de comandes, o directament amb el navegador:

    * API sense key: https://swapi.co (Veure Documentació)

            curl https://swapi.dev/api/
            curl https://swapi.dev/api/people/1/ | json_pp 

    * API amb key: https://openweathermap.org/. Ver Documentació de l'API: https://openweathermap.org/api. Accedir i crear una API key nova.

            export open_weather_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            curl https://api.openweathermap.org/data/2.5/weather?q=Sevilla&units=metric&APPID=open_weather_key&mode=json'


2. ¿Com podem realitzar consultes http amb python3? Utilizant la llibrería `requests`.

    * Instal·lació de `requests`:

            python3 -m venv env
            source env/bin/activate

            pip install requests

    * Consulta a swapi
            ```python
            import requests
            r=requests.get("https://swapi.dev/api/people/1/")
            r.status_code            
            r.json()
            datos=r.json()
            print(datos["name"])
            >>> Luke Skywalker
            ```
            
    * Consulta openwheathermap:

            ```python
            import requests
            import os
            api_key=os.getenv("open_wheather_key")
            parametros={"q":"Sevilla","mode":"json","units":"metric","APPID":api_key}
            r=requests.get("http://api.openweathermap.org/data/2.5/weather",params=parametros)
            r.status_code
            >>>200
            r.url
            >>>'http://api.openweathermap.org/data/2.5/weather?q=Sevilla&units=metric& APPID=xxx&mode=json'
            r.json()
            datos=r.json()
            print(datos["main"]["temp"])
            ```
            
    * Demo1: Temperatura: https://openweathermap.org/api
    * Demo2: Fútbol: https://es.besoccer.com/api/documentacion
    * Demo3: Cine: https://developers.themoviedb.org/3/getting-started/introduction
    
    
***
[Index](../../README.md)
