# El meu primer programa amb Python3

La documentació i els exemples estan basats en la distribució GNU/Linux Debian. Algunes particularitats poden canviar amb altres versions, o distribucions o sistemes operatius.

## Us de l'intèrpret

Al instal·lar Python3 l'executable de l'intèrpret el podem cercar a  `/usr/bin/python3`. Aquest directori per defecte està en el PATH, per lo que podem executar-ho directament des del terminal. Per tant per poder entrar en mode interactiu, on podem executar instrucció per instrucció interactivament, executem:

	$ which python
	/usr/bin/python3
	
	$ python3
	Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
	[GCC 4.9.1] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> 

En el mode interactiu, la darrera expressió impressa està assignada a la variable _.

	>>> 4 +3
	7
	>>> 3 + _
	10


Si tenim el nostre programa en un fitxer font (sol tenir extensió `py`), per exemple `programa.py`,l'executaríem de la següent manera:
	
	$ python3 programa.py

Por defecte la codificació del nostre codi font és UTF-8, per lo que no hauríem de tenir cap problema amb els caràcters utilitzats dintre del nostre programa. Si per qualsevol motiu haguéssim de canviar la codificació, ho podríem fer afegint a la primera línia del programa:

	# -*- coding: encoding -

Per exemple:

	# -*- coding: cp-1252 -*-

## Escrivim un programa

Un exemple del nostre primer programa, podría ser aquest "hola mon" un mica modificat:

	numero = 5
	if numero == 5:
		print ("Hola mon!!!")

La *indentació* de la darrera línea és important (es pot fer amb espais o amb tabulador), amb python s'utilitza la identació per indicar blocs de instruccions definides por les estructures de control (if, while, for, ...). 

Per executar aquest programa (guardat en `hola.py`):

	$ python3 hola.py
	$ Hola mon!!!

## Execució de programes utilitzant [shebang](https://es.wikipedia.org/wiki/Shebang)

Podem executar directament el fitxer utilizant a la primera línea el shebang, on s'indica el executable que anem a utilitzar.

	#!/usr/bin/python3

També podem utilitzar el programa `env` per preguntar al sistema per la ruta de l'intèrpret de python:

	#!/usr/bin/env python

Por suposat, al ser un entorn UNIX, haurem de donar permissos d'execució al fitxer.

	$ chmod +x hola.py

 	$ ./hola.py
	$ Hola mon!!!

## Guía de estil

Una de les idees clau del creador de Python és que el codi es llegeix molt més sovint del que s'escriu. Les directrius que es proporcionen en una guia d'estil estan destinades a millorar la llegibilitat del codi i fer-lo coherent en tot l'ampli espectre del codi Python. ** "La llegibilitat compta".**

Una guia d'estil tracta sobre la coherència. La coherència amb una guia d'estil és important. La coherència dins d'un projecte és més important. La coherència dins d'un mòdul o funció és el més important.
Tanmateix, sabeu quan s'ha de ser inconsistent, de vegades les recomanacions de guies d'estil no són aplicables. En cas de dubte, utilitzeu el vostre millor criteri. Mireu altres exemples i decidiu què es veu millor. 

Pots trobar la guía de estils para escriure codi python a [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/). La guia d'estil es un Python Enhancement Proposals (PEP). Pots consultar totes els [pep a la següent adreça](https://peps.python.org/pep-0000/)



***
[Index](../../../README.md)
