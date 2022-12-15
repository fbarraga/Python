# Gestionar fitxers json

El mòdul [json](https://docs.python.org/3.11/library/json.html) ens permet gestionar fitxers amb format [JSON (JavaScript Object Notation)](http://json.org/).

La correspondència entre JSON i Python la podemos resumir en la següent taula:
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
	>>> datos_json='{"nombre":"carlos","edad":23}'
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

	>>> datos = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
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

	>>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
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