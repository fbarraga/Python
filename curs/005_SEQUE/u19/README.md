# Tipus de dades seqüència

Els tipus de dades sequència em permet guardar una successió de dades de diferents tipus. Els tipus de dades seqüències en python son: 

* Les llistes (`list`): Em permeten guardar un conjunt de dades que es poden repetir i que poden ser de diferents tipus. Es un tipus *mutable*.
* Les tuples (`tuple`): Serveixen per lo mateix que les llistes, per en aquest cas es un tipus inmutable.
* Els rangs (`range`): Es un tipus de seqüència que ens permet crear seqüències de números. Es un tipus inmutable i es sol utilitzar per realitzar bucles.
* Las cadenes de caràcters (`str`): Ens permeten guardar seqüències de caràcters. És un tipus inmutable. 
* Les seqüències de bytes (`byte`): Em permet guardar valors binaris representats per caracters ASCII.És un tipus inmutable.
* Les seqüències de bytes (`bytearray`): En aquest cas son iguals que les anteriors, pero son de tipus mutable.
* Els conjunts (`set`): Em permeten guardar conjunts de dades, en els que no existeixen repeticions. Es un tipo mutable.
* Els conjunt congelats (`frozenset`): Son iguals que els anteriors, pero son tipus inmutables.


## Característiques principals de las seqüències

Anem a veure diferents exemples partint d'una llista que és una seqüència mutable:

	llista = [1,2,3,4,5,6]

* Les seqüències es pueden recorrer
	
		>>> for num in llista:
		...   print(num,end="")
		123456

* *Operadors de pertanyença:* Es pot comprobar si un element pertany o no a una seqüència amb els operadores `in` i `not in`.

		>>> 2 in lista
		True
		>>> 8 not in lista
		True

* *Concatenació:* L'operador `+` em permet unir dades de tipus seqüèncials. No es poden concatenar seqüències de tipus `range` i de tipus conjunt.

		>>> lista + [7,8,9]
		[1, 2, 3, 4, 5, 6, 7, 8, 9]

* *Repetició:* L'operador `*` em permet repetir una dada d'un tipus seqüèncial. No es poden repetir seqüències de tipus `range` i de tipus conjunt.

		>>> llista * 2
		[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

* *Indexació:* Pot obtenir la dada d'una seqüència indicant la posició en la seqüència. Els conjunts no tenen implementat aquesta característica.

		>>> llista[3]
		4
	
* *Slice (rebanada):* Pots obtenir una subseqüència de les dades de una seqüència. En els conjunts no puc obtenir subconjunts. Aquesta característica la veurem más en detall dintre de la unitat on veurem les llistes.

		>>> llista[2:4]
		[3, 4]
		>>> llista[1:4:2]
		[2, 4]

* Amb la funció `len` puc obtenir el tamany de la seqüència, es a dir el número d'elements que conté.

		>>> len(llista)
		6

* Amb la funció `max` i `min` puc obtenir el valor màxim i mínim d'una seqüència.

		>>> max(llista)
		6
		>>> min(llista)
		1
	
A més en els tipus mutables puc realitzar les següents operacions:

* Puc modificar una dada de la seqüència indicant la seva posició.

		>>> llista[2]=99
		>>> llista
		[1, 2, 99, 4, 5, 6]
		
* Puc modificar un subconjunt d'elements de la seqüència fent slice.

		>>> llista[2:4]=[8,9,10]
		>>> llista
		[1, 2, 8, 9, 10, 5, 6]

* Puc esborrar un subconjunt d'elements amb la instrucció `del`.

		>>> del llista[5:]
		>>> llista
		[1, 2, 8, 9, 10]

* Puc actualitzar la seqüència amb l'operador `*=`

		>>> llista*=2
		>>> llista
		[1, 2, 8, 9, 10, 1, 2, 8, 9, 10]

***
[Index](../../../README.md)
