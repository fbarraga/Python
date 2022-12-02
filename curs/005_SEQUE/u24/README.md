# Tipus de dades seqüència: Tuples

Les tuples (`tuple`): Serveixen per lo mateix que les llistes (em permiten guardar un conjunt de dades que es poden repetir i que poden ser de diferents tipus), però en aquest cas és un tipus inmutable.

## Construcció de una tupla

Per crear una llista puc utilitzar varies formas:

* Amb els caràcters ( y ):

    	>>> tupla1 = ()
    	>>> tupla2 = ("a",1,True)

* Utilizant el constructor tuple, que pren com paràmetre un dada d'algún tipus seqüència.

		>>> tupla3=tuple()
		>>> tuple4=tuple([1,2,3])

## Empaquetat i desempaquetat de tuples

Si a una variable se li assigna una seqüència de valors separats per comes, el valor d'aquesta variable serà la tuple formada por tots els valors assignats. 

	>>> tuple = 1,2,3
	>>> tuple
	(1, 2, 3)

Si es té una tupla de longitud k, es po assignar la tupla a k variables diferents i en cada variable quedarà un dels components de la tupla. 

	>>> a,b,c=tuple
	>>> a
	1

## Operacions bàsiques amb tuplas

A les tuples es poden realitzar les següents operacions:

* Les tuples es poden recorrer.
* Operadors de pertanyença: `in` y `not in`.
* Concatenació: `+` 
* Repetició: `*`
* Indexació
* Slice

Entre les funcions definides podem utilitzar: `len`, `max`, `min`, `sum`, `sorted`.

## Las tuplas son inmutables

	>>> tupla = (1,2,3)
	>>> tupla[1]=5
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'tuple' object does not support item assignment

## Mètodes principales

Mètodos de cerca: `count`, `index`

	>>> tupla = (1,2,3,4,1,2,3)
	>>> tupla.count(1)
	2

	>>> tupla.index(2)
	1
	>>> tupla.index(2,2)
	5




