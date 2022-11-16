# Python2 vs Python3

## Python 2.x i Python 3.x

La darrera versió 2.x va ser la 2.7 de 2010, la qual ja no té suport, encara que hi ha moltes programes funcionant sobre aquesta versió.

La versió 3.x està en desenvolupament actiu, la darrera versió 3.11 va sortir 24 d'octubre de 2022, pots consultar totes les versions en el [post: Versions Python](https://www.python.org/doc/versions/). Les modificacions que s'han inclós en Python 3.x en sintaxis i módulos claus han fet que no sigui compatible amb Python 2.x.

Pots consultar els EOL de les diferents versions de Python en el [post: End of life versions Python](https://endoflife.date/python).

En el [post: What’s New In Python 3.0](https://docs.python.org/3.0/whatsnew/3.0.html) escrit per Guido van Rossum podem trobar els canvis introduits a la versió 3.x vs a la versió 2.0. 

A la documentació podeu trobar la página [What’s New in Python](https://docs.python.org/3/whatsnew/index.html) on podeu veure les millores que es van incorporant en cada nova versió.

## ¿Quina versió he d'utilitzar? 

Depenent del projecte que hagis de fer, hauràs de revisar si les biblioteques que has d'utilizar son compatibles amb la versió que utilizaràs. El problema en els darrers anys es que no totes les llibreries s'exporten a la darrera versió en el moment que surt aquesta.

De totes maneres la versión 3 està suficientment madura com per se utilitzada i moltes de les llibreries i software més utilitzat ja està soportat, per lo que si comences un projecte nou, fes-ho des de la darrera o penultima versió.

Si tens codi en una versió antiga, hi ha eines per fer la portabilitat a la darrera versió: [Porting Python Code to 3.x](https://wiki.python.org/moin/PortingPythonToPy3k).

## Les principals diferencies entre Python 2.x y 3.x

## Print es una funció en python3

Amb Python2:

	print "hola mundo"

Amb Python3:

	print ("Hola mundo")

### Divisió de números enters

A python 2 al dividir enters, sempre el resultat era un enter, amb python3 el resultat es un número real.

Amb Python2:

	>>> 4/3
	1

Amb Python3:

	>>> 3/2
	1.5

	>>> num = 3/2
	>>> type(num)
	<class 'float'>
	>>> num = 4/2
	>>> type(num)
	<class 'float'>

### Les "cadenes" (strings) son Unicode de forma predeterminada en Python 3

A python2 existeix dos tipus diferenciats de cadenes: str (ascii) i unicode, a python 3 totes las cadenes son unicodes.

Amb Python2:

	>>> cad = "piña"
	>>> cad
	'pi\xc3\xb1a'


Amb Python3: 

	>>> cad = "piña"
	>>> cad
	'piña'

### Generació de llistes de número

A python2 teníem dos funcions semblants: range que generava una llista de números, i xrange que era una funció que retornava un objecte de tipus xrange. La diferencia entre ambdues era que utilitzar aquesta darrera era molt més eficient. E python3 sólo tenemos range que ha pasado a ser un tipo de datos.

Amb Python2:

	>>> range(1,10)
	[1, 2, 3, 4, 5, 6, 7, 8, 9]
	>>> xrange(1,10)
	xrange(1, 10)
	>>> type(xrange(1,10))
	<type 'xrange'>

Amb Python3:

	>>> range(1,10)
	range(1, 10)
	>>> type(range(1,10))
	<class 'range'>

### Input és una cadena de texte en Python 3

En python 2 hi havien dos funcions per ingresar dades per un teclat raw_input() lo entrat es tractava com una cadena de texte i input() lo entrat s'evaluava i es tractava pel seu tipus. En python 3, es va eliminar  el input() de python 2 quedant el raw_input() como el nou input(). O sigui el input() de python 3 sempre retorna una cadena de texte.

Amb Python2:

	>>> cad=raw_input()
	123
	>>> `type(cad)`
	<type 'str'>
	>>> num=input()
	123
	>>> type(num)
	<type 'int'>

Amb Python3:

	>>> num=input()
	123
	>>> type(num)
	<class 'str'>

### Comparant tipus

Python 3 ens indica un error quan intentem comparar tipus de dades diferents.

Amb python2:

	>>> [1,2] > "hola"
	False

Amb python3:

	>>> [1,2] > "hola"
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: unorderable types: list() > str()


***
[Index](../../../README.md)