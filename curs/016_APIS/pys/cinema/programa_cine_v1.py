import requests
import os


#Usuari fbarragan

api_key=os.getenv("cine_key")
api_key="<get_token>"



URL_BASE="https://api.themoviedb.org/3/"
parametros={"language":"es-ES","page":"1","region":"ES","api_key":api_key}
r=requests.get(URL_BASE+"movie/popular",params=parametros)
if r.status_code == 200:
    datos = r.json()
    cont = 1
    ids = []
    for peliculas in datos["results"]:
        print(cont,peliculas["title"],"->",peliculas["vote_average"])
        ids.append(peliculas["id"])
        cont+=1
else:
    print("Error en la consulta")