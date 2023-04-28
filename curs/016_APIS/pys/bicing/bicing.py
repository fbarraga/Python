#!/usr/bin/python3
import csv
import pandas as pd
import json

# We use a simple library to render maps from OpenStreetMaps
# Short description here: https://github.com/komoot/staticmap/blob/master/README.md
from staticmap import StaticMap, CircleMarker

# We define the location of the csv file and the name of
# the columns we want to retrive. We ignore the other columns
#url = 'https://opendata-ajuntament.barcelona.cat/data/dataset/706e7507-7f84-480e-940d-23265bf5d853/resource/98b893c2-ac83-4f34-b40a-19a4911a066b/download/MERCATS_MUNICIPALS.csv'
# Hem descarregat directament el contingut a un fitxer json.
url="./download.json"
name = 'name'
lon = 'lon'
lat = 'lat'
address = 'address'

#Li fem un prettify

with open ("./download.json",encoding="utf8") as fitxer:
    datos=json.load(fitxer)
fichero=open("./download.json","w")
json.dump(datos,fichero,indent=4)


# Passem el json a csv. Agafem les estacions
data_file = open("./download.csv","w",encoding="utf8")
csv_writer=csv.writer(data_file)
count=0

bicing_data = datos["data"]["stations"]
for station in bicing_data:
    if count == 0: #headers
        header=station.keys()
        csv_writer.writerow(header)
        count+=1
    csv_writer.writerow(station.values())
data_file.close()


# Read the csv file and keep only few columns
df = pd.read_csv("./download.csv", usecols=[name, lon, lat, address])

# This is just for pretty printing
pd.set_option('display.max_rows', 20)
pd.set_option('display.width', 200)
print(df)

# Sort alphabetically by name of district
df.sort_values(by=[name], inplace=True)
print(df)

# Get some rows and print them
r8 = df.iloc[[8]]    # 8-th row
p8 = df.loc[[8]]     # row with index 8
print(r8)
print(p8)

# Treiem duplicats si existeixen
list_names = df.name.unique()
print(list_names)

# Crear un mapa amb totes les parades de bicing a Barcelona.
# Cada parada li posarem un cercle vermell
m_bcn = StaticMap(6000, 6000)
for index, row in df.iterrows():
    marker = CircleMarker((row[lon], row[lat]), 'red', 6)
    m_bcn.add_marker(marker)

# Render an image
image = m_bcn.render()
image.save('bicing.png')

