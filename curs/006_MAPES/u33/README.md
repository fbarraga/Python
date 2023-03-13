# Tipus de dades mapa: diccionari

Els [diccionaris](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) son tipus de dades que ens permeten guardar valors, als que es pot accedir mitjançant una clau. Son tipus de dades mutables i els camps no tenen assignat un ordre.

## Definició de diccionaris. Constructor dict

	>>> a = dict(one=1, two=2, three=3)
	>>> b = {'one': 1, 'two': 2, 'three': 3}
	>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
	>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
	>>> e = dict({'three': 3, 'one': 1, 'two': 2})
	>>> a == b == c == d == e
	True

Si tenim un diccionari buit, al ser un objecte mutable, també podem construir el diccionari de la següent manera:

	>>> dict1 = {}
	>>> dict1["one"]=1
	>>> dict1["two"]=2
	>>> dict1["three"]=3

## Operacions bàsiques amb diccionaris

	>>> a = dict(one=1, two=2, three=3)

* `len()`: Retorna número d'elements del diccionari.

		>>> len(a)
		3

* Indexació: Podem obtenir el valor d'un camp o canviar-lo (si no existeix el camp ens dona una excepció `KeyError`):

		>>> a["one"]
		1
		>>> a["one"]+=1
		>>> a
		{'three': 3, 'one': 2, 'two': 2}

* `del()`:Podem eliminar un element, si no existeix el camp ens dona una excepció `KeyError`:
		
		>>> del(a["one"])
		>>> a
		{'three': 3, 'two': 2}

* Operadors de pertanyença: `key in d` y `key not in d`.

		>>> "two" in a
		True

* `iter()`: Ens retorna un iterador de les claus. 

		>>> next(iter(a))
		'three'

## Els diccionaris son tipus mutables

Els diccionaris, al igual que les llistes, son tipus de dades mutables. Per lo tant podem trobar situacions similars a les que vam explicar amb les llistes.

	>>> a = dict(one=1, two=2, three=3)
	>>> a["one"]=2
	>>> del(a["three"])
	>>> a
	{'one': 2, 'two': 2}	
	

	>>> a = dict(one=1, two=2, three=3)
	>>> b = a
	>>> del(b["one"])
	>>> b
	{'three': 3, 'two': 2}	
	>>> a
	{'three': 3, 'two': 2, 'one': 1 }
	
En aquest cas per copiar diccionaris anem a utilitzar el mètode `copy()`:

	>>> a = dict(one=1, two=2, three=3)
	>>> b = a.copy()
	>>> a["one"]=1000
	>>> b
	{'three': 3, 'one': 1, 'two': 2}

***
[Index](../../../README.md)






