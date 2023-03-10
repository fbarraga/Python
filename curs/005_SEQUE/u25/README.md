# Tipus de dades seqüència: Rangs

Els rangs (`range`): és un tipus de seqüències que ens permet crear seqüències de números. Es un tipus inmutable i es sol utilitzar per realitzar bucles.

## Definició d'un rang. Constructor range

Al crear un rang (seqüència de números) obtenim un objecte que es de la classe `range`:

	>>> rang = range(0,10,2)
	>>> type(rang)
	<class 'range'>

Exemples, convertint el rang en llista per veure la seqüència:

	>>> list(range(10))
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	
	>>> list(range(1, 11))
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	
	>>> list(range(0, 30, 5))
	[0, 5, 10, 15, 20, 25]
	
	>>> list(range(0, 10, 3))
	[0, 3, 6, 9]
	
	>>> list(range(0, -10, -1))
	[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

## Recorregut d'un rang

Els rangs es solen utilitzar per ser recorregut, quan tinc que crear un bucle el número de iteracions del qual el sabem per avançat puc utilitzar una estructura com aquesta:

	>>> for i in range(11):
	...    print(i,end=" ")
	0 1 2 3 4 5 6 7 8 9 10  

## Operacions bàsiques amb range

En les tuples es poden realitzar les següents operacions:

* Els rangs es poden recorrer.
* Operadors de pertanyença: `in` i `not in`.
* Indexació
* Slice

Entre las funcions definides podem utilitzar: `len`, `max`, `min`,  `sum`, `sorted`.

A més un objecte `range` té tres atributs que ens emmagatzemen el començament, final i interval del rang:

	>>> rang = range(1,11,2)
	>>> rang.start
	1
	>>> rang.stop
	11
	>>> rang.step
	2
