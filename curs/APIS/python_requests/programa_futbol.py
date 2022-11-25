import requests
import os
api_key=os.getenv("futbol_key")
URL_BASE="http://apiclient.resultados-futbol.com/scripts/api/api.php"
parametros={"league":2,"req":"tables","format":"json","key":api_key}
r=requests.get(URL_BASE,params=parametros)
if r.status_code == 200:
    datos = r.json()
    for equipos in datos["table"]:
        print(equipos["pos"],equipos["team"],equipos["points"])
else:
    print("Error en la consulta")