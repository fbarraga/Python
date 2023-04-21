import requests
import os

api_key=os.getenv("open_wheather_key")
# Associada a Francescbarragan@msn.com
# Es pot solicitar una apikey directament a traves del registre de openweathermap
# Despues de darse de alta no es usable hasta al cabo de unas horas

api_key ="b106289e4b4fcfdaa3d219da7118a2e1" #fbarraga@institutcampalans.net

ciudad=input("Dime el nombre de una ciudad:")

parametros={"q":ciudad,"mode":"json","units":"metric","APPID":api_key}
r=requests.get("http://api.openweathermap.org/data/2.5/weather",    params=parametros)
if r.status_code == 200:
    datos = r.json()
    print(datos)
    print("La temperatura actual es:",datos["main"]["temp"])
else:
    print("De esa ciudad no tengo datos.")