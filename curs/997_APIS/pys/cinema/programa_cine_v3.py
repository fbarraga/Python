import requests
import os
api_key=os.getenv("cine_key")
api_key="c8ac3185df63e1dcb1ffbd9e0411aed8"
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
    # Primero tengo que conseguir un id de sesión de invitado
    parametros={"api_key":api_key}
    r=requests.get(URL_BASE+"authentication/guest_session/new",params=parametros)
    if r.status_code == 200:
        datos = r.json()
        id_sesion=datos["guest_session_id"]
    # Ahora pido la pélicula y la puntuación
    indice=int(input("Indica la película de la que quieres votar:"))
    id=ids[indice-1]
    puntuacion=input("Indica la puntuación de la película:")
    parametros={"guest_session_id":id_sesion,"api_key":api_key}
    datos='{"value":%s}'%puntuacion
    cabeceras = {"Content-Type":"application/json;charset=utf-8"}
    
    r=requests.post(URL_BASE+"movie/"+str(id)+"/rating",params=parametros,headers=cabeceras,data=datos)
    if r.status_code == 201:
        datos = r.json()
        if datos["status_code"]==1:
            print("Has votado con éxito")
else:
    print("Error en la votación")