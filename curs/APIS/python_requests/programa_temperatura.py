import requests
import os
api_key=os.getenv("open_wheather_key")
ciudad=input("Dime el nombre de una ciudad:")

parametros={"q":ciudad,"mode":"json","units":"metric","APPID":api_key}
r=requests.get("http://api.openweathermap.org/data/2.5/weather",    params=parametros)
if r.status_code == 200:
    datos = r.json()
    print("La temperatura actual es:",datos["main"]["temp"])
else:
    print("De esa ciudad no tengo datos.")