# Mòduls i paquets

* Mòdul: Cadascu dels fitxers `.py` que nosaltres creem es diu mòdul. Els elements creats en un mòdul (funcions, classes, ...) es poden importar per ser utilitzats en un altre mòdul. El nom que anem a utilitzar per importar un mòdul és el nom del fitxer.

* Paquet: Per estructurar els nostres mòduls podem crear paquets. Un paquet, es una carpeta que conté arxius `.py`. Però, per que una carpeta pugui ser considerada un paquet, aquesta ha de contenir un arxiu d'inici anomenat `__init__.py`. Aquest arxiu, no necessita contenir cap instrucció. Els paquets, a la vegada, també poden contener altres sub-paquets.

## Executant mòduls amb scripts

Si hem creat un mòdul, on hem definit dos funcions i hem fet un programa principal on s'utilitzen aquestes funcions, tenim dos opcions: executar aquest mòdul com un script o importar aquest mòdul des d'un altre, per utilitzar les seves funcions. Per exemple, si tenim un fitxer anomenat `potencias.py`:

	#!/usr/bin/env python	

	def cuadrado(n):
		return(n**2)
	def cubo(n):
		return(n**3)
	if __name__ == "__main__":
		print(cuadrado(3))
		print(cubo(3))

En aquest cas, quan l'executo com un script:

	$ python3 potencias.py

El nom que té el mòdul és `__main__`, per lo tant s'executarà el programa principal.

A més aquest mòdul es podrà importar (com veurem en el següent apartat) i el programa principal no es tindrá en compte.

## Important mòduls: import, from

Per importar un mòdul complet hem d'utilitzar les instruccions `import`. ho podem importar de la següent manera:

	>>> import potencias
	>>> potencias.cuadrado(3)
	9
	>>> potencias.cubo(3)
	27

## Namespace i alias

Per accedir (des de el mòdul on es va realitzar l'importació), a qualsevol element del mòdul importat, es realitza mitjançant el **namespace**, seguit d'un punt (.) i el nom de l'element que es vol obtenir. A Python, un **namespace**, es el nom que s'ha indicat després de la paraula import, és a dir la ruta (namespace) del mòdul.

És possible també, abreujar els **namespaces** mtijançant un **alias**. Per això, durant l'importació, s'assigna la paraula clau `as` seguida de l'alias amb el qual ens referirem en el futur a aquest namespace importat:

	>>> import potencias as p
	>>> p.cuadrado(3)
	9

## Important elements d'un mòdul: from...import

Per no utilitzar el **namespace** podem indicar els elements concrets que volem importar d'un mòdul:

	>>> from potencias import cubo
	>>> cubo(3)
	27

Podem importar varis elements separant-los amb comas:

	>>> from potencias import cubo,cuadrado

Podem tenir un problema a l'importar dos elements de dos mòduls que s'anomenin igual. En aquest cas s'ha d'utilitzar **alias**:

	>>> from potencias import cuadrado as pc
	>>> from dibujos import cuadrado as dc
	>>> pc(3)
	9
	>>> dc()
	Esto es un cuadrado

## Important mòduls des de paquets

Si tenim un mòdul dintre d'un paquet l'importació es faria de manera similar. Tenim un paquet anomenat `operaciones`:

	$ cd operaciones
	$ ls
	__init.py__  potencias.py

Per importar-lo:

	>>> import operaciones.potencias
	>>> operaciones.potencias.cubo(3)
	27

	>>> from operaciones.potencias import cubo
	>>> cubo(3)
	27

## Funció dir()

La funció `dir()` ens permet saber els elements definits en un mòdul:

	>>> import potencias
	>>> dir(potencias)
	['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'cuadrado', 'cubo']


## On es troben els mòduls estàndards?
	
Els  mòduls estàndar (com `math` o `sys` per motius d'eficiència están escrits en C e incorporats en el interpret (builtins).

Per obtenir la llista de mòduls builtins:

	>>> import sys
	>>> sys.builtin_module_names
	('_ast', '_bisect', '_codecs', '_collections', '_datetime', '_elementtree', '_functools', '_heapq', '_imp', '_io', '_locale', '_md5', '_operator', '_pickle', '_posixsubprocess', '_random', '_sha1', '_sha256', '_sha512', '_socket', '_sre', '_stat', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'array', 'atexit', 'binascii', 'builtins', 'errno', 'faulthandler', 'fcntl', 'gc', 'grp', 'itertools', 'marshal', 'math', 'posix', 'pwd', 'pyexpat', 'select', 'signal', 'spwd', 'sys', 'syslog', 'time', 'unicodedata', 'xxsubtype', 'zipimport', 'zlib')

Els altres mòduls que podem importar es troben guardats en fitxers, que es troben en els path indicats en l'intèrpret:

	>>> sys.path
	['', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages']


***
[Index](../../../README.md)
