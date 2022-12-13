# Mètodes principals de cadenes

Quan creem una cadena de caràcters estem creant un objecte de la classe `str`, que te definit un conjunt de mètodes:

	cadena.capitalize    cadena.isalnum       cadena.join          cadena.rsplit
	cadena.casefold      cadena.isalpha       cadena.ljust         cadena.rstrip
	cadena.center        cadena.isdecimal     cadena.lower         cadena.split
	cadena.count         cadena.isdigit       cadena.lstrip        cadena.splitlines
	cadena.encode        cadena.isidentifier  cadena.maketrans     cadena.startswith
	cadena.endswith      cadena.islower       cadena.partition     cadena.strip
	cadena.expandtabs    cadena.isnumeric     cadena.replace       cadena.swapcase
	cadena.find          cadena.isprintable   cadena.rfind         cadena.title
	cadena.format        cadena.isspace       cadena.rindex        cadena.translate
	cadena.format_map    cadena.istitle       cadena.rjust         cadena.upper
	cadena.index         cadena.isupper       cadena.rpartition    cadena.zfill


## Mètodes de format

	>>> cad = "hola, com estás?"
	>>> print(cad.capitalize())
	Hola, com estás?

	>>> cad = "Hola Mundo" 
	>>> print(cad.lower())
	hola mundo

	>>> cad = "hola mundo"
	>>> print(cad.upper())
	HOLA MUNDO

	>>> cad = "Hola Mundo"
	>>> print(cad.swapcase())
	hOLA mUNDO

	>>> cad = "hola mundo"
	>>> print(cad.title())
	Hola Mundo

	>>> print(cad.center(50))
	                    hola mundo                    
	>>> print(cad.center(50,"="))
	====================hola mundo====================

	>>> print(cad.ljust(50,"="))
	hola mundo========================================
	>>> print(cad.rjust(50,"="))
	========================================hola mundo

	>>> num = 123
	>>> print(str(num).zfill(12))
	000000000123

## Mètodes de cerca

	>>> cad = "bienvenido a mi aplicación"
	>>> cad.count("a")
	3
	>>> cad.count("a",16)
	2
	>>> cad.count("a",10,16)
	1

	>>> cad.find("mi")
	13
	>>> cad.find("hola")
	-1

	>>> cad.rfind("a")
	21


El mètode `index()` i `rindex()` son similars als anteriors pero provoquen una excepció `ValueError` quan no troba la subcadena. 

## Mètodes de validació

	>>> cad.startswith("b")
	True
	>>> cad.startswith("m")
	False
	>>> cad.startswith("m",13)
	True

	>>> cad.endswith("ción")
	True
	>>> cad.endswith("ción",0,10)
	False
	>>> cad.endswith("nido",0,10)
	True

Altres funcions de validació `isalnum()`, `isalpha()`, `isdigit()`, `islower()`, `isupper()`, `isspace()`, `istitle()`,...

## Mètodes de substitució

### `format`

A la unitat **"Entrada i sortida estàndar"** ja vam introduir el concepte de formateig de cadenes. Vam veure que hi ha dos mètodes i vam veure alguns exemples del *no estil* com la funció predefinida `format()`.

L'ús del [estil nou](https://docs.python.org/3/library/string.html#string-formatting) es actualment el recomanat (pots obtenir més informació i exemples en alguns d'aquests enllaços: [enllaç1](http://www.python-course.eu/python3_formatted_output.php) i [enllaç2](https://pyformat.info/)) i obté tota la seva potencialitat usant el mètode `format()` de les cadenes. Veiem alguns exemples:

	>>> '{} {}'.format("a", "b")
	'a b'
	>>> '{1} {0}'.format("a", "b")
	'b a'
	>>> 'Coordenadas: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
	'Coordenadas: 37.24N, -115.81W'
	>>> '{0:b} {1:x} {2:.2f}'.format(123, 223,12.2345)
	'1111011 df 12.23'
	>>> '{:^10}'.format('test')
	'   test   '

### Altres mètodes de substitució

	>>> buscar = "nombre apellido"
	>>> reemplazar_por = "Juan Pérez" 
	>>> print ("Estimado Sr. nombre apellido:".replace(buscar, reemplazar_por)) 
	Estimado Sr. Juan Pérez:

	>>> cadena = "   www.eugeniabahit.com   " 
	>>> print(cadena.strip())
	www.eugeniabahit.com
	>>> cadena="00000000123000000000"
	>>> print(cadena.strip("0"))
	123

De manera similar `lstrip(["caracter"])` y `rstrip(["caracter"])`.

## Mètodes d'unió i divisió

	>>> formato_numero_factura = ("Nº 0000-0", "-0000 (ID: ", ")"
	>>> print("275".join(formato_numero_factura))
	Nº 0000-0275-0000 (ID: 275)

	>>> hora = "12:23"
	>>> print(hora.rpartition(":"))
	('12', ':', '23')
	>>> print(hora.partition(":"))
	('12', ':', '23')
	>>> hora = "12:23:12"
	>>> print(hora.partition(":"))
	('12', ':', '23:12')
	>>> print(hora.split(":"))
	['12', '23', '12']
	>>> print(hora.rpartition(":"))
	('12:23', ':', '12')
	>>> print(hora.rsplit(":",1))
	['12:23', '12']


	>>> texto = "Linea 1\nLinea 2\nLinea 3" 
	>>> print(texto.splitlines())
	['Linea 1', 'Linea 2', 'Linea 3']

***
[Index](../../../README.md)
