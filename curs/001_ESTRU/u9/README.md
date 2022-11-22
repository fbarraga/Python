# Tipus de dades

Podem concretar encara més els tipus de dades (o classes) dels objectes que gestionem en el llenguatge:

* Tipus númerics
	* Tipus enter (int)
	* Tipus real (float)
	* Tipus numéric (complex)
* Tipus booleans (bool)
* Tipus de dades seqüència
	* Tipus llista (list)
	* Tipus tuples (tuple)
	* Tipus rang (range)
* Tipus de dades cadenes de caràcters
	* Tipus cadena (str)
* Tipus de dades binaris
	* Tipus byte (bytes)
	* tipus bytearray (bytearray)
* Tipus de dades conjunts
	* Tipus conjunt (set)
	* Tipus conjunt inmutable (frozenset)
* Tipus de dades iterador i generador (iter)
* Tipus de dades mapes o diccionari (dict)

En realitat tot té definit el seu tipus o classe:

* Fitxers
* Mòduls
* Funcions
* Excepcions
* Classes 

## Funció type() 

La función `type` ens retorna el tipus de dades d'un objecte donat. Per exemple:

	>>> type(5)
	<class 'int'>
	>>> type(5.5)
	<class 'float'>
	>>> type([1,2])
	<class 'list'>
	>>> type(int)
	<class 'type'>

## Funció isinstance()

Aquesta funció retorna True si l'objecte indicat és del tipus indicat, en cas contrari retorna False.

	>>> isinstance(5,int)
	True
	>>> isinstance(5.5,float)
	True
	>>> isinstance(5,list)
	False

***
[Index](../../../README.md)
