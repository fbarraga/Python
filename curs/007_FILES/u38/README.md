# Fitxers JSON

## Introducció

El mòdul [json](https://docs.python.org/3.11/library/json.html) ens permet gestionar fitxers amb format [JSON (JavaScript Object Notation)](https://www.json.org/json-es.html).

Els fitxers JSON son molt utilitzats per recuperar dades de diferents websites mitjançant REST APIs. Per exemple utilitzant les APIs de Twitter, Youtube, o Google maps.

Exemple de fitxer JSON que retorna **Google Maps**:
```json
{
  "markers": [
    {
      "name": "Rixos The Palm Dubai",
      "position": [25.1212, 55.1535],
    },
    {
      "name": "Shangri-La Hotel",
      "location": [25.2084, 55.2719]
    },
    {
      "name": "Grand Hyatt",
      "location": [25.2285, 55.3273]
    }
  ]
}
```

La correspondència entre JSON i Python la podem resumir en la següent taula:
<table>
	<tr><td>JSON</td><td>Python</td></tr>
	<tr><td>object</td><td>dict</td></tr>
	<tr><td>array</td><td>list</td></tr>
	<tr><td>string</td><td>str</td></tr>
	<tr><td>number (int)</td><td>int</td></tr>
	<tr><td>number (real)</td><td>float</td></tr>
	<tr><td>true</td><td>True</td></tr>
	<tr><td>false</td><td>False</td></tr>
	<tr><td>null</td><td>None</td></tr>
</table>

## Llegir fitxers json

Des d'una cadena de caràcters:

	>>> import json
	>>> datos_json='{
			"nombre":"carlos",
			"edad":23
			}'
	>>> datos = json.loads(datos_json)
	>>> type(datos)
	<class 'dict'>
	>>> print(datos)
	{'nombre': 'carlos', 'edad': 23}

Des de un fitxer:

	>>> with open("exemple1.json") as fitxer:
	...   datos=json.load(fitxer)
	>>> type(datos)
	<class 'dict'>
	>>> datos
	{'bookstore': {'book': [{'_category': 'COOKING', 'price': '30.00', 'author': 'Giada De Laurentiis', 'title': {'__text': 'Everyday Italian', '_lang': 'en'}, 'year': '2005'}, {'_category': 'CHILDREN', 'price': '29.99', 'author': 'J K. Rowling', 'title': {'__text': 'Harry Potter', '_lang': 'en'}, 'year': '2005'}, {'_category': 'WEB', 'price': '49.99', 'author': ['James McGovern', 'Per Bothner', 'Kurt Cagle', 'James Linn', 'Vaidyanathan Nagarajan'], 'title': {'__text': 'XQuery Kick Start', '_lang': 'en'}, 'year': '2003'}, {'_category': 'WEB', 'price': '39.95', 'author': 'Erik T. Ray', 'title': {'__text': 'Learning XML', '_lang': 'en'}, 'year': '2003'}]}}


Fixe'm nos que quan llegim d'una cadena de caràcters es json.loads i quan llegim d'un fitxer json.load

	
## Escriure fitxers json

	>>> datos = {
		     'isCat': True, 
		     'miceCaught': 0, 
		     'name': 'Zophie',
		     'felineIQ': None
		     }
	>>> fichero = open("exemple2.json","w")
	>>> json.dump(datos,fichero)
	>>> fichero.close()

	cat ejemplo2.json 
	{"miceCaught": 0, "name": "Zophie", "felineIQ": null, "isCat": true}

Fixe'm nos que quan escrivim en un fitxer és json.dump i quan ho fem a cadena de caràcters es json.dumps

## Mostrar fitxers json

Codificació de jerarquies bàsiques en Python.

	>>> import json
	>>>json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
	'["foo", {"bar": ["baz", null, 1.0, 2]}]'

	>>> print(json.dumps("\"foo\bar"))
	"\"foo\bar"

	>>> print(json.dumps('\u1234'))
	"\u1234"

	>>> print(json.dumps('\\'))
	"\\"

	>>> print(json.dumps({
				"c": 0, 
				"b": 0, 
				"a": 0
			      }, sort_keys=True))
	{"a": 0, "b": 0, "c": 0}

	>>> from io import StringIO
	>>> io = StringIO()
	>>> json.dump(['streaming API'], io)	
	>>> io.getvalue()
	'["streaming API"]'

Codificació compacta:

	>>> import json
	>>> json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
	'[1,2,3,{"4":5,"6":7}]'

Pretty printing:

	>>> import json
	>>> print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
	{
    	"4": 5,
    	"6": 7
	}


***


## Format JSON al núvol

JSON s’utilitza habitualment intercanviar dades entre un servidor i una aplicació web. Per exemple, a http://wservice.viabicing.cat/v2/stations podeu trobar la informació en temps real de les estacions de Bicing de la ciutat de Barcelona. Aquesta adreça conté un fitxer JSON amb la ubicació (coordenades longitud-latitud) de les estacions de bicing, la seva adreça (carrer i número), llistat de les estacions més pròximes, estat de l’estació, nombre d’aparcaments i nombre de bicicletes disponibles, mecàniques i elèctriques.

Aquí en teniu un fragment:
```
{
  "stations": [
    {
      "id": "1",
      "type": "BIKE",
      "latitude": "41.397952",
      "longitude": "2.180042",
      "streetName": "Gran Via Corts Catalanes",
      "streetNumber": "760",
      "altitude": "21",
      "slots": "14",
      "bikes": "14",
      "nearbyStations": "24, 369, 387, 426",
      "status": "OPN"
    },
    {
      "id": "2",
      "type": "BIKE",
      "latitude": "41.39553",
      "longitude": "2.17706",
      "streetName": "Roger de Flor/ Gran Vía",
      "streetNumber": "126",
      "altitude": "21",
      "slots": "8",
      "bikes": "18",
      "nearbyStations": "360, 368, 387, 414",
      "status": "OPN"
    },
    /* dades omeses */
  ],
  "updateTime": 1530802508
}
```

El programa següent (que després comentem) escriu el nombre de bicis i de llocs disponibles al Bicing de Barcelona:

```python
import json
import urllib.request

response = urllib.request.urlopen('http://wservice.viabicing.cat/v2/stations')
bicing = json.load(response)
bikes = 0
slots = 0
for station in bicing['stations']:
    bikes += int(station['bikes'])
    slots += int(station['slots'])
print(bikes, slots)

```python 

En aquest cas, com que les dades no són en un fitxer del propi ordinador, no usem open() sinó urllib.request.urlopen() que funciona de forma semblant a open(), però enlloc d’obrir un fitxer local obre una pàgina de web a través de la seva URL. El valor que retorna urlopen() és una reposta response que podem utilitzar, si fa no fa, com un fitxer. En particular, la podem passar a json.load() perquè descodifiqui les dades en JSON i les desi en una variable de Python anomenada bicing.

Després, ja només cal recórrer l’estructura de dades bicing per calcular la suma de bicis aparcades i llocs disponibles. Noteu que, en aquest cas, hem hagut de convertir a enters els valors numèrics perquè el proveïdor del fitxer els ha proporcionat com a textos (😱!).




[Index](../../../README.md)
